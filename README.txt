GS NET ACADEMY — pure static website
=====================================

Plain HTML + CSS + Tailwind. Every word on a page is written directly inside
that page's .html file — nothing is generated at run time.

There are two JavaScript files:
  js/testimonial.js  — drives the result carousel (smooth, never-ending
                        auto-scroll). Remove its <script> tag and the site
                        still works, the carousel just becomes a swipe strip.
  js/lead-gate.js     — the "fill a form, then download" popup used on the
                        Brochure button (index.html), every Notes PDF
                        (notes.html) and the Tutorials study plan
                        (tutorials.html). It POSTs to server/ (Node.js +
                        Express + MongoDB Atlas) — see server/README.txt.

No React, no admin panel. There IS now a small database-backed server —
see the "LEADS API" section below.


HOW TO RUN
----------
Double-click index.html. That's all.


HOW TO PUT IT ONLINE
--------------------
Upload the whole folder to any hosting — cPanel public_html, Hostinger,
Netlify, Vercel, GitHub Pages. Nothing needs to be installed on the server.


THE PAGES
---------
index.html                 Home
about.html                 About
courses.html               Courses + exam pattern + 10 units
tutorials.html             All 10 units
unit-1.html … unit-10.html One page per unit, with its modules
notes.html                 Paper-I notes
blog.html                  Blog list
blog-<article>.html        One finished page per article (5 of them)
contact.html               Contact + enquiry form
enroll.html                Registration steps


HOW TO EDIT
-----------
Open the .html file in Notepad, VS Code or any editor, find the text, change
it, save. That is the whole workflow.

Two things live in more than one page — the top menu and the footer. If you
change a menu link, change it in every .html file (Find &amp; Replace across
files does this in seconds in VS Code: Ctrl+Shift+H).

If you would rather change such things in ONE place, this folder also ships
the small generator that produced these files — see "REBUILDING" below. You
never have to use it.


COMMON EDITS
------------
1. PHONE / EMAIL
   Search for 9266511505 or gsnetacademy@gmail.com and replace everywhere.

2. BROCHURE PDF
   Put the file in assets/pdf/. Then in each page change the Brochure button's
   href from contact.html to assets/pdf/brochure.pdf and add  download.

3. DEMO VIDEO
   In index.html search for youtube.com/embed/ and replace the ID after it.

4. FACULTY PHOTO
   Save the photo as  assets/images/faculty.jpg  (that exact name and path).
   Until you do, the box shows a note telling you where to put it.

5. NEW RESULT POSTER
   Put the image in assets/results/netjrf/ (or /phd/ or /teacher/), then in
   index.html copy one <li> inside the matching list and change the file name.
   Also bump the number in that tab's little count badge.

6. NEW BLOG ARTICLE
   Copy an existing blog-*.html, rename it, edit the text inside. Then add one
   card for it in blog.html (copy an existing card and change the link, title
   and date).


WHAT WORKS WITHOUT JAVASCRIPT
-----------------------------
- Mobile menu       — a hidden checkbox plus CSS
- Result tabs       — hidden radio buttons plus CSS
- FAQ open/close    — the plain HTML <details> tag
- Result carousel   — swipe / scroll works on its own; js/testimonial.js adds
                      the smooth endless auto-scroll on top
- Contact form      — opens the visitor's email app with the message ready


THE ONE SCRIPT — js/testimonial.js
----------------------------------
It finds every row with class "tab-panel" (the result strips already have it),
quietly duplicates the posters once, and glides the row sideways for ever. The
copy is what makes the loop seamless — you never see it restart.

  • pauses while the mouse is over it, or a finger is on it
  • pauses when the browser tab is in the background
  • stays still for visitors who have "reduce motion" switched on
  • the visitor can still swipe or scroll by hand any time

To change the speed, open the file and edit one line near the top:

      var SPEED = 34;      // pixels per second — higher is faster

To auto-scroll some other row, give that row class="tab-panel" too.


STYLES
------
css/style.css     Colours, buttons, cards, the no-JS interactions.
                  Edit freely — it is ordinary CSS, no build needed.
css/tailwind.css  The pre-built Tailwind classes. Already included; you only
                  rebuild it if you add a Tailwind class the site doesn't use
                  yet:

                      npm install
                      npm run css

                  Colours and fonts for that build: tailwind.config.js


REBUILDING (optional — you can ignore this folder entirely)
----------------------------------------------------------
build/ holds the small Python script that wrote these HTML files:

    build/content.py   all the page text
    build/blogs.py     all the articles
    build/generate.py  header, footer, shared pieces
    build/pages.py     the page layouts

    python3 build/pages.py      → rewrites every .html file

Useful if you ever want to change the header or footer once instead of in
every file. WARNING: it overwrites the .html files, so any edit you made
directly in them would be lost.


LEADS API — form data → MongoDB Atlas
--------------------------------------
See server/README.txt for full setup. Short version:

    cd server
    npm install
    cp .env.example .env      → paste your MongoDB Atlas URI here
    npm start

Every time someone clicks Download Brochure (index.html), a unit's
Download PDF (notes.html) or Download Study Plan (tutorials.html),
js/lead-gate.js pops up a small form (Name, Mobile, WhatsApp, Email),
POSTs it to this server, saves it to your MongoDB Atlas database, and
THEN starts the download — the file never opens before the form is filled.
Once someone has filled it once, their browser remembers and skips the
form on later downloads.

To add the same gate to a new button anywhere else on the site:

    <a href="#" class="btn-primary gate-btn"
       data-gate-title="What this download is"
       data-gate-type="brochure"                (or "note" / "tutorial" / anything)
       data-gate-file="assets/pdf/your-file.pdf">
      Download
    </a>

and make sure js/lead-gate.js is loaded on that page (it already is on
index.html, notes.html and tutorials.html).

Actual PDF files: put them at the exact paths referenced in each button's
data-gate-file (assets/pdf/brochure.pdf, assets/pdf/unit-1-notes.pdf …
assets/pdf/unit-10-notes.pdf, assets/pdf/syllabus-study-plan.pdf). Until you
upload the real files there, the download step will 404 — the lead is still
saved either way.


NOTES
-----
- Fonts come from Google Fonts, so the very first load wants internet.
  Everything else works fully offline.
- The demo video is a YouTube embed and needs internet to play.
- The Leads API needs internet (to reach MongoDB Atlas) once it's deployed.
