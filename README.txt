OLIVE BRANCH LANDING PAGE — GOOGLE ADS
=======================================

URL when uploaded: odysseylawncarellc.com/olive-branch-quote/

WHAT TO UPLOAD:
  1. Bluehost File Manager -> public_html
  2. Create new folder: olive-branch-quote
  3. Upload index.html into that folder
  4. Test: odysseylawncarellc.com/olive-branch-quote/

THIS IS A CONVERSION-FOCUSED LANDING PAGE designed for Google Ads
traffic. Different from your other pages:
  - No nav menu (just logo + phone)
  - Form is in the hero — visitors can convert without scrolling
  - Minimal footer
  - All content focused on getting a lead

WHAT'S BUILT IN:
  - Formspree integration (same endpoint as other forms)
  - UTM parameter tracking — captures which Google Ad/keyword brought
    each visitor and includes it in the form submission email
  - GCLID capture for Google Ads conversion attribution
  - GA4 lead event tracking
  - Placeholder spots for Google Ads conversion tag (see HTML comments)
  - noindex tag — won't show in organic search

GOOGLE ADS SETUP:

  Final URL in your ads:
    https://odysseylawncarellc.com/olive-branch-quote/

  Tracking template (paste in Google Ads campaign settings):
    {lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_term={keyword}&utm_content={creative}&gclid={gclid}

  Geographic targeting: Olive Branch, MS - 5 mile radius

  Suggested starting keywords:
    - lawn care olive branch
    - lawn mowing olive branch ms
    - lawn service olive branch
    - weekly lawn mowing olive branch

  Suggested negative keywords:
    - free
    - cheap
    - DIY / diy
    - jobs
    - equipment

ADDING GOOGLE ADS CONVERSION TRACKING (when you set up the campaign):
  1. Create "Submit lead form" conversion action in Google Ads
  2. Google gives you 2 snippets:
     - Global Site Tag -> paste in <head> (look for "PASTE GLOBAL SITE TAG HERE")
     - Event Snippet -> paste in form success handler (look for "PASTE EVENT SNIPPET HERE")
  3. Both have HTML comments showing exactly where to paste
  4. Re-upload the file
  5. Test: submit form, check Google Ads to see conversion fire
