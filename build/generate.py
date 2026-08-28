# -*- coding: utf-8 -*-
"""
Writes every page of the site as finished, static HTML.

    python3 build/generate.py

You only need this if you want to change the shared header/footer or the page
layout in one place. The HTML it produces is plain and readable — you can also
just edit the .html files directly and never run this again.
"""

import os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from content import *          # noqa
from blogs import BLOGS        # noqa

ROOT = os.path.join(os.path.dirname(__file__), "..")
YEAR = datetime.date.today().year

# --------------------------------------------------------------------------- #
# icons                                                                        #
# --------------------------------------------------------------------------- #
P = {
 "cap": '<path d="M12 4 2.5 8.6 12 13.2l9.5-4.6L12 4Z"/><path d="M6.4 10.6V16c0 1.4 2.5 2.8 5.6 2.8s5.6-1.4 5.6-2.8v-5.4"/><path d="M21.5 8.6v5"/>',
 "book": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H19v15H6.5A2.5 2.5 0 0 0 4 20.5v-15Z"/><path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H19v3H6.5A2.5 2.5 0 0 1 4 20.5Z"/>',
 "notes": '<path d="M6 3h8l4 4v14H6V3Z"/><path d="M14 3v4h4"/><path d="M9 12h6M9 16h6"/>',
 "pdf": '<path d="M6 3h8l4 4v14H6V3Z"/><path d="M14 3v4h4"/><path d="M9 13.5h1.4a1.1 1.1 0 0 1 0 2.2H9v-2.2Zm0 2.2V18"/><path d="M13.4 13.5h1.2a1.4 1.4 0 0 1 1.4 1.4v1.7a1.4 1.4 0 0 1-1.4 1.4h-1.2v-4.5Z"/>',
 "download": '<path d="M12 3v12"/><path d="m7.5 11 4.5 4.5 4.5-4.5"/><path d="M4 20h16"/>',
 "play": '<path d="M7 4.5 19 12 7 19.5v-15Z"/>',
 "phone": '<path d="M5 3h3.5l1.6 4-2 1.4a12 12 0 0 0 5.5 5.5l1.4-2 4 1.6V19a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 3 5.2 2 2 0 0 1 5 3Z"/>',
 "mail": '<rect x="2.5" y="4.5" width="19" height="15" rx="2.5"/><path d="m3.5 6.5 8.5 6 8.5-6"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5.2l3.2 2"/>',
 "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
 "trophy": '<path d="M7 4h10v5a5 5 0 0 1-10 0V4Z"/><path d="M7 5.5H4.5V7a3 3 0 0 0 3 3M17 5.5h2.5V7a3 3 0 0 1-3 3"/><path d="M12 14v4M8.5 21h7l-.7-3h-5.6l-.7 3Z"/>',
 "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>',
 "mentor": '<circle cx="9" cy="8" r="3.2"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0"/><path d="M16.5 8.5h5M16.5 12h5M16.5 15.5h3"/>',
 "test": '<rect x="4" y="3" width="16" height="18" rx="2.5"/><path d="m8 10 1.6 1.6L13 8.2"/><path d="M8 16h8"/>',
 "clipboard": '<rect x="5" y="4.5" width="14" height="16" rx="2.5"/><path d="M9 4.5a3 3 0 0 1 6 0"/><path d="M9 11h6M9 15h4"/>',
 "layers": '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 13 9 5 9-5"/>',
 "spark": '<path d="M12 3.5 13.8 9l5.5 1.8-5.5 1.8L12 18.1l-1.8-5.5L4.7 10.8 10.2 9 12 3.5Z"/>',
 "check": '<path d="m5 12.5 4.5 4.5L19 7"/>',
 "arrow": '<path d="M4 12h15"/><path d="m13 6 6 6-6 6"/>',
 "search": '<circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/>',
 "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 "refresh": '<path d="M20 12a8 8 0 1 1-2.6-5.9"/><path d="M20 4v4.5h-4.5"/>',
 "flask": '<path d="M9.5 3v6.2L4.7 18a2 2 0 0 0 1.7 3h11.2a2 2 0 0 0 1.7-3l-4.8-8.8V3"/><path d="M8.5 3h7M7.5 15h9"/>',
 "pen": '<path d="M4 20l1-4.5L16.2 4.3a2 2 0 0 1 2.8 2.8L7.8 18.3 4 20Z"/>',
 "users": '<circle cx="9" cy="8" r="3.2"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 5.4a3.2 3.2 0 0 1 0 5.2M18 20a6.4 6.4 0 0 0-2-4.6"/>',
 "rupee": '<path d="M7 4h10M7 8.5h10M16.5 4c0 3-2.2 4.5-5 4.5H7l7.5 11.5"/>',
 "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17"/><path d="M12 3.5c2.4 2.6 3.5 5.4 3.5 8.5S14.4 17.9 12 20.5c-2.4-2.6-3.5-5.4-3.5-8.5S9.6 6.1 12 3.5Z"/>',
 "shield": '<path d="M12 3 20 6v6c0 4.4-3.2 7.9-8 9-4.8-1.1-8-4.6-8-9V6l8-3Z"/><path d="m8.8 12 2.2 2.2 4.2-4.4"/>',
 "megaphone": '<path d="M4 10v4a2 2 0 0 0 2 2h1l9 4V4L7 8H6a2 2 0 0 0-2 2Z"/><path d="M19 9.5a3.5 3.5 0 0 1 0 5"/>',
 "monitor": '<rect x="3" y="4.5" width="18" height="12" rx="2"/><path d="M9 20.5h6M12 16.5v4"/>',
 "videocam": '<rect x="3" y="6.5" width="12" height="11" rx="2.5"/><path d="m15 11 5.5-3v8L15 13"/>',
 "library": '<rect x="3.5" y="4" width="4" height="16" rx="1.2"/><rect x="9.5" y="4" width="4" height="16" rx="1.2"/><path d="m16 5.5 3.8 1-3 14.2-3.8-1"/>',
 "signal": '<path d="M5 19v-5M10 19V9M15 19V5M20 19v-8"/>',
 "settings": '<circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.2 5.2l2.1 2.1M16.7 16.7l2.1 2.1M18.8 5.2l-2.1 2.1M7.3 16.7l-2.1 2.1"/>',
 "chevron": '<path d="m6 9 6 6 6-6"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "close": '<path d="m6 6 12 12M18 6 6 18"/>',
 "external": '<path d="M14 4h6v6"/><path d="M20 4 10 14"/><path d="M18 14v5a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 4 19V8a1.5 1.5 0 0 1 1.5-1.5H10"/>',
 "whatsapp": '<path d="M3.2 20.8 4.6 16A8.4 8.4 0 1 1 8 19.4l-4.8 1.4Z"/><path d="M9 8.4c.3-.7.6-.7.9-.7h.6c.2 0 .5 0 .7.6l.8 1.9c.1.2.1.4 0 .6l-.5.7c-.1.2-.2.4 0 .7a7 7 0 0 0 3 2.6c.3.1.5.1.7-.1l.7-.8c.2-.2.4-.2.6-.1l1.8.9c.3.1.5.3.5.5v.6c0 .4-.2.9-.9 1.2-.6.3-1.5.4-2.5.1a10 10 0 0 1-6.5-6.2c-.3-1-.1-1.9.1-2.5Z"/>',
 "user": '<circle cx="12" cy="8" r="3.5"/><path d="M4.5 20.5a7.5 7.5 0 0 1 15 0"/>',
}

def ic(name, cls="h-5 w-5", filled=False):
    d = P.get(name, P["spark"])
    return ('<svg viewBox="0 0 24 24" class="%s" fill="%s" stroke="%s" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
            % (cls, "currentColor" if filled else "none", "none" if filled else "currentColor", d))

# --------------------------------------------------------------------------- #
# header / footer                                                              #
# --------------------------------------------------------------------------- #
def navbar(current):
    top = ('<div class="hidden bg-navy-950 text-white lg:block">\n'
           '  <div class="container-wide flex h-9 items-center justify-between text-[12px]">\n'
           '    <p class="flex min-w-0 items-center gap-2 truncate font-semibold text-navy-100/80">%s'
           '<span class="truncate">Target %s Exam — Paper-I Batch Started %s</span></p>\n'
           '    <div class="flex shrink-0 items-center gap-5 font-semibold">\n'
           % (ic("target", "h-3.5 w-3.5 shrink-0 icon-gold"), SITE["exam_target"], SITE["batch_start"]))
    for p in SITE["phones"]:
        top += ('      <a href="tel:+91%s" class="flex items-center gap-1.5 hover:text-gold-300">%s +91 %s</a>\n'
                % (p, ic("phone", "h-3.5 w-3.5", True), p))
    top += ('      <a href="mailto:%s" class="flex items-center gap-1.5 hover:text-gold-300">%s %s</a>\n'
            % (SITE["email"], ic("mail", "h-3.5 w-3.5"), SITE["email"]))
    top += ('      <a href="%s" target="_blank" rel="noreferrer noopener" class="flex items-center gap-1.5 '
            'rounded-md bg-white/10 px-2.5 py-1 transition hover:bg-emerald-500/25 hover:text-white">%s WhatsApp Group</a>\n'
            % (SITE["whatsapp_group"], ic("whatsapp", "h-3.5 w-3.5")))
    top += "    </div>\n  </div>\n</div>\n"

    links = ""
    for label, href, soon in NAV:
        if soon:
            links += ('      <li><span title="Coming soon" class="flex cursor-default items-center gap-1.5 whitespace-nowrap '
                      'rounded-lg px-3 py-2 text-[13.5px] font-bold text-navy-400">%s'
                      '<span class="rounded-md bg-navy-900/8 px-1.5 py-0.5 text-[9.5px] font-extrabold uppercase tracking-wider">'
                      'Coming soon</span></span></li>\n' % label)
        else:
            on = href == current
            links += ('      <li><a href="%s" class="relative block whitespace-nowrap rounded-lg px-3 py-2 text-[13.5px] '
                      'font-bold transition-colors %s">%s<span class="absolute inset-x-3 -bottom-0.5 h-0.5 rounded-full '
                      'bg-gold-400 %s"></span></a></li>\n'
                      % (href, "text-navy-900" if on else "text-navy-700/75 hover:text-navy-900",
                         label, "scale-x-100" if on else "scale-x-0"))

    portal = (('<a href="%s" target="_blank" rel="noreferrer noopener" class="btn-outline btn-sm hidden whitespace-nowrap lg:inline-flex">%s Exam Portal</a>'
               % (SITE["exam_portal"], ic("clipboard", "h-3.5 w-3.5")))
              if SITE["exam_portal"] else
              ('<span title="Coming soon" class="hidden items-center gap-1.5 whitespace-nowrap rounded-lg border '
               'border-navy-900/12 px-3 py-2 text-[13px] font-bold text-navy-400 lg:inline-flex">%s Exam Portal</span>'
               % ic("clipboard", "h-3.5 w-3.5")))
    broch = ('<a href="%s" download class="btn-outline btn-sm hidden 2xl:inline-flex">Brochure</a>' % SITE["brochure"]) if SITE["brochure"] else ""

    header = ('<header class="sticky top-0 z-50 border-b border-navy-900/8 bg-white/95 backdrop-blur-md">\n'
              '  <nav class="container-wide flex h-[76px] items-center gap-4" aria-label="Main">\n'
              '    <a href="index.html" class="flex shrink-0 items-center gap-3" aria-label="Home">\n'
              '      <span class="inline-flex shrink-0 items-center justify-center overflow-hidden rounded-lg bg-navy-950 ring-1 ring-navy-900/10">\n'
              '        <img src="assets/images/logo.png" alt="GS Net Academy" class="h-11 w-auto" width="120" height="44">\n'
              '      </span>\n'
              '      <img src="assets/images/tagline.png" alt="#1 A Premier institute for UGC NET Paper-1" class="hidden h-11 w-auto lg:block">\n'
              '    </a>\n'
              '    <ul class="mx-auto hidden items-center gap-5 xl:flex">\n%s    </ul>\n'
              '    <div class="ml-auto flex items-center gap-2 xl:ml-0">\n'
              '      %s\n'
              '      <a href="index.html#free-demo" class="btn-outline btn-sm hidden 2xl:inline-flex">Demo</a>\n'
              '      %s\n'
              '      <a href="enroll.html" class="btn-primary btn-sm hidden sm:inline-flex">Join Now</a>\n'
              '      <label for="nav-toggle" class="cursor-pointer rounded-lg border border-navy-900/12 p-2 text-navy-800 xl:hidden" aria-label="Menu">%s</label>\n'
              '    </div>\n  </nav>\n</header>\n' % (links, portal, broch, ic("menu", "h-5 w-5")))

    drawer_links = '      <li><a href="index.html" class="flex items-center justify-between rounded-xl px-4 py-3.5 text-[15px] font-bold %s">Home</a></li>\n' % (
        "bg-navy-50 text-navy-900" if current == "index.html" else "text-navy-700")
    for label, href, soon in NAV:
        if soon:
            drawer_links += ('      <li><span class="flex items-center justify-between rounded-xl px-4 py-3.5 text-[15px] '
                             'font-bold text-navy-400">%s<span class="rounded-md bg-navy-50 px-2 py-0.5 text-[10.5px] '
                             'font-extrabold uppercase tracking-wider">Coming soon</span></span></li>\n' % label)
        else:
            on = href == current
            drawer_links += ('      <li><a href="%s" class="flex items-center justify-between rounded-xl px-4 py-3.5 '
                             'text-[15px] font-bold %s">%s</a></li>\n'
                             % (href, "bg-navy-50 text-navy-900" if on else "text-navy-700", label))

    drawer = ('<div class="drawer xl:hidden">\n'
              '  <label for="nav-toggle" class="drawer-scrim" aria-hidden="true"></label>\n'
              '  <div class="drawer-panel">\n'
              '    <div class="flex h-[72px] shrink-0 items-center justify-between border-b border-navy-900/10 px-5">\n'
              '      <img src="assets/images/logo.png" alt="GS Net Academy" class="h-9 w-auto rounded-lg bg-navy-950">\n'
              '      <label for="nav-toggle" class="cursor-pointer p-2 text-navy-800" aria-label="Close">%s</label>\n'
              '    </div>\n'
              '    <div class="flex-1 overflow-y-auto p-5">\n'
              '      <ul class="flex flex-col gap-1">\n%s      </ul>\n'
              '      <p class="mt-3 rounded-xl bg-gold-50 px-4 py-3 text-[12.5px] font-extrabold uppercase tracking-wider text-gold-700">'
              'AI-Powered Career Guidance — Coming soon</p>\n'
              '      <div class="mt-5 grid gap-2.5">\n'
              '        <a href="enroll.html" class="btn-primary w-full">✓ JOIN BATCH @ ₹500</a>\n'
              '        <a href="index.html#free-demo" class="btn-outline w-full">▶ WATCH FREE DEMO</a>\n'
              '        <a href="%s" target="_blank" rel="noreferrer noopener" class="btn-outline w-full">%s WhatsApp Group</a>\n'
              '        <a href="tel:+91%s" class="btn-dark w-full">%s Call %s</a>\n'
              '      </div>\n    </div>\n  </div>\n</div>\n'
              % (ic("close", "h-5 w-5"), drawer_links, SITE["whatsapp_group"], ic("whatsapp", "h-4 w-4"),
                 SITE["phones"][0], ic("phone", "h-4 w-4", True), SITE["phones"][0]))

    return '<input type="checkbox" id="nav-toggle" class="nav-toggle">\n' + top + header + drawer


def footer():
    quick = [("Blog", "blog.html"), ("UGC NET Paper-I", "courses.html"), ("Tutorials", "tutorials.html"),
             ("About", "about.html"), ("Contact", "contact.html")]
    res = [("Notes", "notes.html"), ("Courses", "courses.html"), ("Register for ₹500", "enroll.html"),
           ("Student Community", SITE["whatsapp_group"])]

    def col(title, items):
        out = ('    <div><p class="text-[11px] font-extrabold uppercase tracking-[0.18em] text-gold-400">%s</p>\n'
               '      <ul class="mt-4 grid gap-2.5">\n' % title)
        for label, href in items:
            ext = ' target="_blank" rel="noreferrer noopener"' if href.startswith("http") else ""
            out += ('        <li><a href="%s"%s class="text-[14px] text-navy-100/75 transition hover:text-gold-300">%s</a></li>\n'
                    % (href, ext, label))
        return out + "      </ul>\n    </div>\n"

    contact = '    <div><p class="text-[11px] font-extrabold uppercase tracking-[0.18em] text-gold-400">Contact</p>\n      <ul class="mt-4 grid gap-2.5 text-[14px] text-navy-100/75">\n'
    for p in SITE["phones"]:
        contact += ('        <li><a href="tel:+91%s" class="flex items-center gap-2 hover:text-gold-300">%s +91 %s</a></li>\n'
                    % (p, ic("phone", "h-4 w-4 icon-gold", True), p))
    contact += ('        <li><a href="mailto:%s" class="flex items-center gap-2 break-all hover:text-gold-300">%s %s</a></li>\n'
                % (SITE["email"], ic("mail", "h-4 w-4 icon-gold"), SITE["email"]))
    contact += ('        <li><a href="%s" target="_blank" rel="noreferrer noopener" class="flex items-center gap-2 hover:text-gold-300">%s WhatsApp Group</a></li>\n'
                % (SITE["whatsapp_group"], ic("whatsapp", "h-4 w-4 icon-gold")))
    contact += '      </ul>\n      <a href="enroll.html" class="btn-primary mt-6 w-full">Join for ₹500</a>\n    </div>\n'

    return ('<footer class="relative overflow-hidden bg-navy-950 text-white">\n'
            '  <div class="grid-paper absolute inset-0 opacity-50" aria-hidden="true"></div>\n'
            '  <div class="container-x relative py-12 lg:py-14">\n'
            '    <div class="grid gap-10 lg:grid-cols-[1.4fr_1fr_1fr_1.1fr]">\n'
            '    <div>\n'
            '      <div class="flex items-center gap-3">\n'
            '        <img src="assets/images/logo.png" alt="GS Net Academy" class="h-11 w-auto rounded-lg bg-white p-1">\n'
            '        <img src="assets/images/tagline.png" alt="" class="h-11 w-auto brightness-0 invert">\n'
            '      </div>\n'
            '      <p class="mt-5 text-[14px] text-navy-100/75">%s</p>\n'
            '      <span class="eyebrow mt-5">%s %s</span>\n'
            '    </div>\n'
            '%s%s%s'
            '    </div>\n'
            '    <div class="mt-10 flex flex-col gap-3 border-t border-white/10 pt-6 text-[13px] text-navy-100/60 sm:flex-row sm:items-center sm:justify-between">\n'
            '      <p>© %s GS Net Academy. All Rights Reserved.</p>\n'
            '      <p>A Premier institute for UGC NET Paper-1</p>\n'
            '    </div>\n  </div>\n</footer>\n'
            % (SITE["subtitle"], ic("target", "h-3.5 w-3.5"), SITE["mission"],
               col("Quick Links", quick), col("Resources", res), contact, YEAR))


def page(filename, title, desc, body, current):
    html = ('<!doctype html>\n<html lang="en">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>%s</title>\n'
            '<meta name="description" content="%s">\n'
            '<link rel="icon" href="assets/images/logo.png">\n'
            '<link rel="stylesheet" href="css/tailwind.css">\n'
            '<link rel="stylesheet" href="css/style.css">\n'
            '</head>\n<body>\n\n%s\n<main id="main">\n%s</main>\n\n%s\n'
            '<script src="js/testimonial.js"></script>\n</body>\n</html>\n'
            % (title, desc, navbar(current), body, footer()))
    open(os.path.join(ROOT, filename), "w").write(html)


# --------------------------------------------------------------------------- #
# shared blocks                                                                #
# --------------------------------------------------------------------------- #
def page_head(eyebrow, title, sub="", extra=""):
    return ('<section class="relative overflow-hidden bg-navy-950 text-white">\n'
            '  <div class="grid-paper absolute inset-0 opacity-50" aria-hidden="true"></div>\n'
            '  <div class="absolute -right-24 -top-28 h-[380px] w-[380px] rounded-full bg-gold-500/15 blur-3xl" aria-hidden="true"></div>\n'
            '  <div class="container-x relative py-12 lg:py-14">\n    <div class="max-w-3xl">\n'
            '      <span class="eyebrow">%s %s</span>\n'
            '      <h1 class="h-display mt-5 text-[42px] sm:text-[58px] lg:text-[66px]">%s</h1>\n'
            '%s%s'
            '    </div>\n  </div>\n</section>\n'
            % (ic("spark", "h-3.5 w-3.5"), eyebrow, title,
               ('      <p class="mt-5 max-w-2xl text-[16px] leading-relaxed text-navy-100/80">%s</p>\n' % sub) if sub else "",
               ('      <div class="mt-8">%s</div>\n' % extra) if extra else ""))


def section_head(eyebrow, title, sub="", light=False):
    return ('  <div class="mx-auto max-w-3xl text-center">\n'
            '    <span class="eyebrow">%s %s</span>\n'
            '    <h2 class="h-display mt-4 text-[30px] sm:text-[38px]%s">%s</h2>\n'
            '    <div class="rule-gold mx-auto mt-4"></div>\n%s  </div>\n'
            % (ic("spark", "h-3.5 w-3.5"), eyebrow, " text-white" if light else "", title,
               ('    <p class="hind mt-4 text-[15px] leading-relaxed %s">%s</p>\n'
                % ("text-navy-100/80" if light else "text-navy-700", sub)) if sub else ""))


def cta_row(tone="light", center=False):
    sec = "btn-ghost-light" if tone == "dark" else "btn-outline"
    broch = ('<a href="%s" download class="%s">⬇ DOWNLOAD BROCHURE</a>' % (SITE["brochure"], sec)) if SITE["brochure"] \
            else ('<a href="contact.html" class="%s">⬇ DOWNLOAD BROCHURE</a>' % sec)
    return ('<div class="flex flex-col gap-3 sm:flex-row sm:flex-wrap%s">'
            '<a href="index.html#free-demo" class="%s">▶ WATCH FREE DEMO</a>%s'
            '<a href="enroll.html" class="btn-primary">✓ JOIN BATCH @ ₹500</a></div>'
            % (" sm:justify-center" if center else "", sec, broch))


def cta_band():
    return ('<section class="bg-cream py-12 lg:py-14"><div class="container-x">\n'
            '  <div class="relative overflow-hidden rounded-2xl bg-navy-950 p-8 text-white sm:p-10">\n'
            '    <div class="grid-paper absolute inset-0 opacity-50" aria-hidden="true"></div>\n'
            '    <div class="absolute -right-16 -top-16 h-56 w-56 rounded-full bg-gold-500/20 blur-3xl" aria-hidden="true"></div>\n'
            '    <div class="relative flex flex-col gap-6 sm:flex-row sm:items-center sm:justify-between">\n'
            '      <div>\n        <h2 class="h-display text-[28px] sm:text-[34px]">Join the Paper-1 Batch</h2>\n'
            '        <p class="mt-2 max-w-lg text-[14.5px] text-navy-100/80">Course fee FREE — %s registration &amp; '
            'academic/logistics contribution. Classes daily at %s.</p>\n      </div>\n'
            '      <a href="enroll.html" class="btn-primary shrink-0">✓ JOIN BATCH @ ₹500</a>\n'
            '    </div>\n  </div>\n</div></section>\n' % (SITE["contribution"], SITE["class_time"]))


def faq_block(items, first_open=True):
    """Plain <details> — opens and closes with no JavaScript at all."""
    out = '  <ul class="mt-6 grid gap-2.5">\n'
    for i, (q, a) in enumerate(items):
        op = " open" if (first_open and i == 0) else ""
        out += ('    <li><details class="faq card overflow-hidden"%s>\n'
                '      <summary class="flex cursor-pointer items-center justify-between gap-4 px-5 py-4">\n'
                '        <span class="text-[14.5px] font-bold text-navy-900">%d. %s</span>\n'
                '        <span class="faq-mark grid h-6 w-6 shrink-0 place-items-center rounded-md bg-navy-50 text-[16px] font-extrabold text-navy-700"></span>\n'
                '      </summary>\n'
                '      <p class="border-t border-navy-900/8 px-5 py-4 text-[14px] leading-relaxed text-navy-700">%s</p>\n'
                '    </details></li>\n' % (op, i + 1, q, a))
    return out + "  </ul>\n"


def photo(src, alt, cls, note):
    """Real <img>; if the file is missing the caption below still explains where to put it."""
    return ('<span class="ph-wrap relative block">'
            '<img src="%s" alt="%s" class="%s">'
            '<span class="ph-note">%s</span></span>' % (src, alt, cls, note))
