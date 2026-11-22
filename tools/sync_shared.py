#!/usr/bin/env python3
"""Keep the header, footer and font block identical on every page.

The single copies live in _shared/. Each page has marked regions like

    <!-- shared:footer --> ... <!-- /shared:footer -->

and this script rewrites what is between the markers from the matching file
in _shared/.

    python3 tools/sync_shared.py          update every page
    python3 tools/sync_shared.py --check  change nothing; exit 1 if any page is out of date

Header options go on the opening marker of a page that needs them:

    <!-- shared:header cta_href="#apply" cta_label="Apply Now" -->

The header link that points at the page itself gets aria-current="page" automatically.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHARED = ROOT / "_shared"
SKIP_DIRS = {"new-home", "_shared", "tools", ".git", "node_modules"}
HEADER_DEFAULTS = {"cta_href": "#quote", "cta_label": "Get Estimate"}
REGION = re.compile(
    r"(<!-- shared:(?P<name>[a-z]+)(?P<attrs>(?: [a-z_]+=\"[^\"]*\")*) -->)"
    r"(?P<body>.*?)"
    r"(<!-- /shared:(?P=name) -->)",
    re.S,
)


def pages():
    for path in sorted(ROOT.rglob("index.html")):
        rel = path.relative_to(ROOT)
        if not SKIP_DIRS.intersection(rel.parts):
            yield path


def page_url(path):
    rel = path.relative_to(ROOT).parent.as_posix()
    return "/" if rel == "." else "/" + rel + "/"


def partial(name):
    return (SHARED / (name + ".html")).read_text(encoding="utf-8").rstrip("\n")


def render(name, attrs, url):
    html = partial(name)
    if name == "header":
        opts = dict(HEADER_DEFAULTS)
        opts.update(dict(re.findall(r'([a-z_]+)="([^"]*)"', attrs)))
        for key, value in opts.items():
            html = html.replace("{{" + key + "}}", value)

        def mark_current(match):
            tag = match.group(0)
            return tag[:-1] + ' aria-current="page">' if match.group(1) == url else tag

        html = re.sub(r'<a href="([^"]*)"[^>]*>', mark_current, html)
    if "{{" in html:
        raise SystemExit("Unfilled placeholder in _shared/%s.html" % name)
    return html


def sync(path):
    text = path.read_text(encoding="utf-8")
    url = page_url(path)

    def replace(match):
        return match.group(1) + render(match.group("name"), match.group("attrs"), url) + match.group(5)

    return text, REGION.sub(replace, text)


def main():
    check = "--check" in sys.argv[1:]
    stale = []
    for path in pages():
        old, new = sync(path)
        if old != new:
            stale.append(path.relative_to(ROOT).as_posix())
            if not check:
                path.write_text(new, encoding="utf-8")
    if check and stale:
        print("Out of date (run: python3 tools/sync_shared.py):")
        for name in stale:
            print("  " + name)
        return 1
    print(("Would update" if check else "Updated") + " %d page(s)." % len(stale))
    return 0


if __name__ == "__main__":
    sys.exit(main())
