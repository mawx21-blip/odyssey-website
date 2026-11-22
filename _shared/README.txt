SHARED HEADER, FOOTER AND FONTS
===============================

The header (menu), footer and font block are the same on every page.
The one true copy of each lives in this folder:

  header.html   the top menu
  footer.html   the footer
  fonts.html    the font loading block in each page's <head>

HOW TO CHANGE THEM
  1. Edit the file in this folder (for example, add a service to header.html
     and footer.html).
  2. Run:  python3 tools/sync_shared.py
     That copies the change into every page.
  3. Commit everything and open a pull request as usual.

Do not edit the header or footer inside an individual page. Anything between
the "shared:" comment markers is overwritten the next time the script runs.
A check on every pull request fails if a page is out of step with this folder.

PER-PAGE OPTIONS
  The header's green button says "Get Estimate" and jumps to #quote by default.
  A page can override it on its opening marker, like the careers page does:
    <!-- shared:header cta_href="#apply" cta_label="Apply Now" -->

NOT SHARED
  - The Olive Branch ad landing page (olive-branch-quote) keeps its own short footer.
  - The new-home folder is an old draft and is skipped.

This folder and the tools folder are not uploaded to the live site.
