# -*- coding: utf-8 -*-
"""Builds the body of every page, then writes the files."""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import *          # noqa
from blogs import BLOGS        # noqa
from generate import (ic, page, page_head, section_head, cta_row, cta_band,
                      faq_block, photo, SITE)  # noqa
import datetime


# =========================================================================== #
# HOME                                                                        #
# =========================================================================== #
def home():
    tiles = ""
    for icn, label, value in HERO["highlights"]:
        tiles += ('        <div class="rounded-xl border border-white/12 bg-white/[0.07] px-3.5 py-3 transition hover:border-gold-400/50">\n'
                  '          <p class="flex items-center gap-1.5 text-[10px] font-bold uppercase leading-tight tracking-wider text-navy-200/70">%s%s</p>\n'
                  '          <p class="mt-1 text-[16px] font-extrabold leading-tight text-white">%s</p>\n        </div>\n'
                  % (ic(icn, "h-3.5 w-3.5 shrink-0 icon-gold"), label, value))

    chips = "".join('<li class="rounded-lg border border-gold-400/25 bg-gold-400/10 px-2.5 py-1.5 text-[12px] font-bold text-gold-200">%s</li>' % c
                    for c in HERO["includes"])

    creds = "".join('<li class="flex items-start gap-2 text-[12.5px] leading-snug text-navy-100/85">%s%s</li>'
                    % (ic("check", "mt-0.5 h-3.5 w-3.5 shrink-0 icon-gold"), c) for c in FACULTY["credentials"])

    feats = ""
    for i, (icn, title, text) in enumerate(FEATURES):
        b = "border-l border-t border-white/12"
        if i < 2: b += " border-t-0"
        if i % 2 == 0: b += " border-l-0"
        b += " sm:border-l"
        if i < 3: b += " sm:border-t-0"
        if i % 3 == 0: b += " sm:border-l-0"
        b += " lg:border-t-0 lg:border-l" if i else " lg:border-t-0 lg:border-l-0"
        feats += ('      <li class="flex flex-col items-center gap-3 px-5 py-8 text-center transition-colors hover:bg-white/[0.06] sm:px-6 sm:py-10 %s">\n'
                  '        <span class="grid h-14 w-14 shrink-0 place-items-center rounded-2xl bg-gold-400/15 ring-1 ring-gold-400/30 sm:h-16 sm:w-16">%s</span>\n'
                  '        <p class="text-[16px] font-extrabold leading-tight text-white sm:text-[17.5px]">%s</p>\n'
                  '        <p class="max-w-[19ch] text-[13px] font-semibold leading-snug text-navy-200/80 sm:text-[13.5px]">%s</p>\n'
                  '      </li>\n' % (b, ic(icn, "icon-gold h-8 w-8 sm:h-9 sm:w-9"), title, text))

    hero = ('<section class="relative overflow-hidden bg-navy-950 text-white">\n'
            '  <div class="grid-paper absolute inset-0 opacity-50" aria-hidden="true"></div>\n'
            '  <div class="absolute -right-40 -top-40 h-[560px] w-[560px] rounded-full bg-gold-500/15 blur-3xl" aria-hidden="true"></div>\n'
            '  <div class="absolute -bottom-48 -left-32 h-[420px] w-[420px] rounded-full bg-navy-400/20 blur-3xl" aria-hidden="true"></div>\n'
            '  <div class="container-x relative grid items-start gap-10 py-10 lg:grid-cols-[60fr_40fr] lg:gap-12 lg:py-14">\n'
            '    <div>\n'
            '      <p class="text-[10.5px] font-extrabold uppercase tracking-[0.22em] text-gold-400 sm:text-[11px]">%s</p>\n'
            '      <h1 class="h-display mt-3 text-[42px] leading-[0.92] sm:text-[56px] lg:text-[64px]">JRF <span class="text-gold-400">@ ₹500</span><span class="block">— MISSION 2026</span></h1>\n'
            '      <p class="mt-3.5 text-[15px] font-extrabold uppercase leading-snug tracking-wide text-white sm:text-[17px]">%s</p>\n'
            '      <p class="mt-1.5 text-[13.5px] font-semibold text-gold-300">%s</p>\n'
            '      <p class="hind mt-4 text-[16px] font-semibold leading-relaxed text-navy-100">%s</p>\n'
            '      <div class="mt-6 grid grid-cols-2 gap-2.5 sm:grid-cols-3">\n%s      </div>\n'
            '      <ul class="mt-4 flex flex-wrap gap-1.5">%s</ul>\n'
            '      <p class="mt-5 flex flex-wrap items-center gap-2 rounded-xl border border-brick/40 bg-brick/15 px-4 py-3 text-[13.5px] font-bold text-white">'
            '<span class="inline-flex items-center gap-1.5 rounded-md bg-brick px-2 py-0.5 text-[10.5px] font-extrabold uppercase tracking-wider">'
            '<span class="h-1.5 w-1.5 rounded-full bg-white"></span> Batch Status</span>%s</p>\n'
            '      <div class="mt-6">%s</div>\n'
            '      <p class="hind mt-4 text-[13.5px] font-semibold text-navy-200/75">%s</p>\n'
            '    </div>\n'
            '    <div class="mx-auto w-full max-w-[420px] lg:sticky lg:top-24">\n'
            '      <div class="rounded-3xl border border-white/12 bg-white/[0.05] p-4 backdrop-blur-sm sm:p-5">\n'
            '        <div class="relative">%s\n'
            '          <span class="absolute left-3 top-3 rounded-lg bg-gold-400 px-2.5 py-1 text-[10.5px] font-extrabold uppercase tracking-wider text-navy-950">Faculty</span>\n'
            '        </div>\n'
            '        <p class="mt-3.5 font-display text-[24px] font-extrabold uppercase leading-none tracking-tight text-gold-400">%s</p>\n'
            '        <ul class="mt-3 grid gap-1.5 border-t border-white/10 pt-3">%s</ul>\n'
            '        <a href="enroll.html" class="btn-primary mt-4 w-full">%s Enroll @ ₹500</a>\n'
            '      </div>\n    </div>\n  </div>\n'
            '  <div class="container-x relative pb-12 lg:pb-16">\n'
            '    <div class="overflow-hidden rounded-3xl border border-white/12 bg-navy-900/80 backdrop-blur">\n'
            '      <ul class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6">\n%s      </ul>\n'
            '    </div>\n  </div>\n</section>\n'
            % (BRAND_EXAMS, HERO["subtitle"], DESIGNED_BY, HERO["line1"], tiles, chips,
               HERO["batch_strip"], cta_row("dark"), HERO["note"],
               photo(FACULTY["photo"], FACULTY["name"], "aspect-[4/5] w-full rounded-2xl object-cover",
                     "Add the photo at " + FACULTY["photo"]),
               FACULTY["name"], creds, ic("rupee", "h-4 w-4"), feats))

    # approach
    steps = ""
    for i, (n, title, text) in enumerate(APPROACH):
        steps += ('    <li class="relative flex-1"><div class="card h-full p-5 text-center">\n'
                  '      <p class="text-[10.5px] font-extrabold uppercase tracking-[0.16em] text-gold-600">Step %s</p>\n'
                  '      <p class="mt-1.5 text-[16px] font-extrabold text-navy-900">%s</p>\n'
                  '      <p class="hind mt-2 text-[12.5px] leading-relaxed text-navy-700">%s</p>\n    </div>%s</li>\n'
                  % (n, title, text,
                     ('<span class="absolute -right-3 top-1/2 hidden -translate-y-1/2 text-navy-300 lg:block">%s</span>'
                      % ic("arrow", "h-5 w-5")) if i < len(APPROACH) - 1 else ""))
    approach = ('<section class="bg-cream py-14 lg:py-16"><div class="container-x">\n'
                '  <span class="eyebrow">%s GS Net Academy Approach</span>\n'
                '  <h2 class="h-display mt-4 max-w-3xl text-[30px] sm:text-[40px]">Concept → PYQ → Practice → Test → Analysis → Revision → Mentorship</h2>\n'
                '  <div class="rule-gold mt-4"></div>\n'
                '  <ul class="mt-8 grid gap-4 sm:grid-cols-2 lg:flex lg:gap-5">\n%s  </ul>\n'
                '</div></section>\n' % (ic("spark", "h-3.5 w-3.5"), steps))

    # results — CSS-only tabs (radio inputs + labels), no script
    groups = [g for g in RESULTS if g[2]]
    tabs, panels, radios = "", "", ""
    for i, (key, label, files) in enumerate(groups):
        radios += '  <input type="radio" name="results" id="tab-%s" class="tab-radio"%s>\n' % (key, " checked" if i == 0 else "")
        tabs += ('      <label for="tab-%s" class="tab-label rounded-xl px-5 py-2.5 text-[14px] font-extrabold sm:text-[15px]">%s'
                 '<span class="tab-count ml-2 rounded-md px-1.5 py-0.5 text-[11.5px] font-extrabold">%d</span></label>\n'
                 % (key, label, len(files)))
        cards = "".join('        <li class="w-[82%%] shrink-0 snap-start sm:w-[46%%] lg:w-[31.5%%]">'
                        '<div class="overflow-hidden rounded-2xl border border-navy-900/12 bg-white shadow-card">'
                        '<img src="assets/results/%s/%s" alt="GS Net Academy result" loading="lazy" '
                        'class="block aspect-square w-full object-cover"></div></li>\n' % (key, f) for f in files)
        panels += ('    <ul class="tab-panel panel-%s no-scrollbar flex snap-x snap-mandatory gap-5 overflow-x-auto pb-2">\n%s    </ul>\n'
                   % (key, cards))

    results = ('<section class="bg-white py-14 lg:py-16"><div class="container-x">\n'
               '%s'
               '  <div class="results">\n%s'
               '    <div class="mt-8 flex justify-center"><div class="inline-flex flex-wrap justify-center gap-1.5 rounded-2xl border border-navy-900/12 bg-cream p-1.5">\n%s    </div></div>\n'
               '    <div class="mt-8">\n%s    </div>\n'
               '  </div>\n'
               '  <p class="mt-4 text-center text-[12.5px] font-semibold text-navy-500">Posters अपने आप चलते रहते हैं — रोकने के लिए ऊपर mouse ले जाइए, या हाथ से swipe कीजिए।</p>\n'
               '  <div class="mt-6 text-center"><a href="enroll.html" class="btn-primary">%s Join Batch @ ₹500</a></div>\n'
               '</div></section>\n'
               % (section_head("Student Voices", "Our Students' Results",
                               "GS Net Academy के students के official NTA results."),
                  radios, tabs, panels, ic("rupee", "h-4 w-4")))

    # batch status
    bpoints = "".join('<li class="flex items-start gap-2.5 text-[14px] font-semibold text-navy-800">%s%s</li>'
                      % (ic("check", "mt-0.5 h-4 w-4 shrink-0 text-gold-600"), p) for p in BATCH["points"])
    batch = ('<section class="border-b border-navy-900/8 bg-white py-10 lg:py-12"><div class="container-x">\n'
             '  <div class="rounded-2xl border border-navy-900/10 bg-cream p-6 sm:p-8">\n'
             '    <div class="grid gap-8 lg:grid-cols-[1.3fr_.7fr] lg:items-center">\n      <div>\n'
             '        <span class="eyebrow"><span class="h-1.5 w-1.5 rounded-full bg-brick"></span> %s</span>\n'
             '        <p class="hind mt-4 text-[15px] leading-relaxed text-navy-800">%s</p>\n'
             '        <ul class="mt-6 grid gap-2.5 sm:grid-cols-2">%s</ul>\n      </div>\n'
             '      <a href="enroll.html" class="btn-primary w-full py-4 text-[15px]">%s %s</a>\n'
             '    </div>\n  </div>\n</div></section>\n'
             % (BATCH["heading"], BATCH["body"], bpoints, BATCH["cta"], ic("arrow", "h-4 w-4")))

    # why join
    probs = "".join('    <li class="card flex items-start gap-3 p-4">'
                    '<span class="grid h-7 w-7 shrink-0 place-items-center rounded-lg bg-brick/10 text-[12px] font-extrabold text-brick">%d</span>'
                    '<span class="hind text-[13.5px] leading-relaxed text-navy-800">%s</span></li>\n'
                    % (i + 1, p) for i, p in enumerate(WHY_JOIN["problems"]))
    boost = "".join('<li class="rounded-lg border border-gold-300/60 bg-gold-50 px-3 py-2 text-[13px] font-bold text-gold-700">%s</li>' % b
                    for b in WHY_JOIN["booster_points"])
    whyjoin = ('<section class="bg-cream py-14 lg:py-16"><div class="container-x">\n%s'
               '  <ul class="mt-9 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">\n%s  </ul>\n'
               '  <div class="card mt-8 p-7 sm:p-9">\n'
               '    <h3 class="text-[21px] font-extrabold text-navy-900">%s</h3>\n'
               '    <p class="hind mt-3 text-[15px] leading-relaxed text-navy-800">%s</p>\n'
               '    <ul class="mt-5 flex flex-wrap gap-2">%s</ul>\n'
               '    <p class="hind mt-6 flex items-start gap-2.5 rounded-xl bg-navy-50 p-4 text-[13.5px] leading-relaxed text-navy-700">%s%s</p>\n'
               '  </div>\n</div></section>\n'
               % (section_head("Why now", WHY_JOIN["heading"], WHY_JOIN["intro"]), probs,
                  WHY_JOIN["booster_heading"], WHY_JOIN["booster_body"], boost,
                  ic("shield", "mt-0.5 h-4 w-4 shrink-0 text-navy-500"), WHY_JOIN["disclaimer"]))

    # coverage
    cov = "".join('    <div class="card card-hover flex h-full items-start gap-4 p-5">'
                  '<span class="grid h-11 w-11 shrink-0 place-items-center rounded-xl bg-navy-900 font-display text-[18px] font-extrabold text-gold-400">%s</span>'
                  '<div><h3 class="text-[16px] font-extrabold text-navy-900">%s</h3>'
                  '<p class="hind mt-1.5 text-[13px] leading-relaxed text-navy-700">%s</p></div></div>\n'
                  % (n, t, d) for n, t, d in COVERAGE)
    coverage = ('<section class="bg-white py-14 lg:py-16"><div class="container-x">\n%s'
                '  <div class="mt-9 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s  </div>\n'
                '  <div class="mt-8 flex justify-center">%s</div>\n</div></section>\n'
                % (section_head("Syllabus", "What Will You Study?", "10 units — हर unit से 5 questions और 10 marks."),
                   cov, cta_row("light", True)))

    # different
    dif = "".join('    <div class="card card-hover h-full p-6">'
                  '<span class="grid h-9 w-9 place-items-center rounded-lg bg-gold-400 font-display text-[15px] font-extrabold text-navy-950">%s</span>'
                  '<h3 class="mt-4 text-[17px] font-extrabold text-navy-900">%s</h3>'
                  '<p class="hind mt-2 text-[13.5px] leading-relaxed text-navy-700">%s</p></div>\n'
                  % (n, t, d) for n, t, d in DIFFERENT)
    different = ('<section class="bg-cream py-14 lg:py-16"><div class="container-x">\n%s'
                 '  <div class="mt-9 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s  </div>\n</div></section>\n'
                 % (section_head("The difference", "What Makes This Program Different?"), dif))

    # demo
    dpoints = "".join('<li class="hind flex items-start gap-2.5 text-[14.5px] text-navy-100/85">%s%s</li>'
                      % (ic("check", "mt-0.5 h-4 w-4 shrink-0 icon-gold"), p) for p in DEMO["points"])
    demo = ('<section id="free-demo" class="scroll-mt-24 bg-navy-950 py-16 text-white lg:py-20">\n'
            '  <div class="container-x grid gap-8 lg:grid-cols-2 lg:items-center">\n    <div>\n'
            '      <span class="eyebrow">%s Free Demo Class</span>\n'
            '      <h2 class="h-display mt-4 text-[30px] sm:text-[38px]">%s</h2>\n'
            '      <div class="rule-gold mt-4"></div>\n'
            '      <p class="hind mt-4 text-[15px] leading-relaxed text-navy-100/80">%s</p>\n'
            '      <ul class="mt-6 grid gap-2.5">%s</ul>\n    </div>\n'
            '    <div class="overflow-hidden rounded-2xl border border-white/15 bg-black shadow-lift">\n'
            '      <div class="relative w-full pb-[56.25%%]">\n'
            '        <iframe class="absolute inset-0 h-full w-full" src="https://www.youtube.com/embed/%s?rel=0&amp;modestbranding=1&amp;playsinline=1" '
            'title="Free demo class" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>\n'
            '      </div>\n    </div>\n  </div>\n</section>\n'
            % (ic("play", "h-3.5 w-3.5"), DEMO["heading"], DEMO["body"], dpoints, SITE["demo_video"]))

    # faculty
    fwhy = "".join('<li class="flex items-start gap-2.5 text-[14px] text-navy-800">%s%s</li>'
                   % (ic("check", "mt-0.5 h-4 w-4 shrink-0 text-gold-600"), w) for w in FACULTY["why"])
    fac = ('<section class="bg-white py-14 lg:py-16"><div class="container-x grid gap-8 lg:grid-cols-[.8fr_1.2fr] lg:items-center">\n'
           '  <div>%s</div>\n  <div>\n'
           '    <span class="eyebrow">%s Faculty</span>\n'
           '    <h2 class="h-display mt-4 text-[30px] sm:text-[38px]">%s</h2>\n'
           '    <div class="rule-gold mt-4"></div>\n'
           '    <ul class="mt-6 grid gap-2.5 sm:grid-cols-2">%s</ul>\n'
           '    <p class="hind mt-6 rounded-xl border-l-4 border-gold-400 bg-gold-50 px-5 py-4 text-[14.5px] font-semibold leading-relaxed text-navy-900">%s</p>\n'
           '  </div>\n</div></section>\n'
           % (photo(FACULTY["photo"], FACULTY["name"], "aspect-[4/5] w-full rounded-2xl object-cover shadow-lift",
                    "Add the photo at " + FACULTY["photo"]),
              ic("cap", "h-3.5 w-3.5"), FACULTY["why_heading"], fwhy, FACULTY["quote"]))

    # why academy
    wpoints = "".join('    <li class="card card-hover flex items-center gap-3 p-4">'
                      '<span class="grid h-9 w-9 shrink-0 place-items-center rounded-lg bg-navy-900 font-display text-[14px] font-extrabold text-gold-400">%02d</span>'
                      '<span class="text-[13.5px] font-bold text-navy-900">%s</span></li>\n'
                      % (i + 1, p) for i, p in enumerate(WHY_ACADEMY["points"]))
    whyac = ('<section class="bg-cream py-14 lg:py-16"><div class="container-x">\n%s'
             '  <div class="mt-8 flex items-center gap-4 rounded-2xl bg-navy-950 p-5 text-white sm:p-6">'
             '<span class="grid h-11 w-11 shrink-0 place-items-center rounded-xl bg-gold-400/15 ring-1 ring-gold-400/30">%s</span>'
             '<p class="text-[13px] font-extrabold uppercase leading-relaxed tracking-wider text-gold-300 sm:text-[14px]">%s</p></div>\n'
             '  <ul class="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">\n%s  </ul>\n</div></section>\n'
             % (section_head("Why us", WHY_ACADEMY["heading"], WHY_ACADEMY["body"]),
                ic("trophy", "icon-gold h-6 w-6"), WHY_ACADEMY["formula"], wpoints))

    # who should
    def panel(title, items, good):
        icn = "check" if good else "close"
        color = "text-emerald-700" if good else "text-brick"
        box = "border-emerald-200 bg-emerald-50/60" if good else "border-brick/30 bg-brick/5"
        lis = "".join('<li class="hind flex items-start gap-2.5 text-[13.5px] leading-relaxed text-navy-800">%s%s</li>'
                      % (ic(icn, "mt-1 h-3.5 w-3.5 shrink-0 " + ("text-emerald-600" if good else "text-brick")), i)
                      for i in items)
        return ('    <div class="rounded-2xl border p-6 sm:p-7 %s">'
                '<h3 class="flex items-center gap-2.5 text-[19px] font-extrabold %s">%s%s</h3>'
                '<ul class="mt-5 grid gap-2.5">%s</ul></div>\n'
                % (box, color, ic(icn, "h-5 w-5"), title, lis))
    who = ('<section class="bg-white py-14 lg:py-16"><div class="container-x">\n%s'
           '  <div class="mt-9 grid gap-5 lg:grid-cols-2">\n%s%s  </div>\n</div></section>\n'
           % (section_head("Fit check", "Who Should Join?"),
              panel(WHO["join_heading"], WHO["join"], True),
              panel(WHO["not_heading"], WHO["not_join"], False)))

    # program
    prows = "".join('    <div class="card flex items-center gap-3.5 p-4">'
                    '<span class="grid h-10 w-10 shrink-0 place-items-center rounded-xl bg-gold-50 text-gold-600 ring-1 ring-gold-200">%s</span>'
                    '<div><p class="text-[10.5px] font-extrabold uppercase tracking-[0.14em] text-navy-500">%s</p>'
                    '<p class="text-[14.5px] font-extrabold text-navy-900">%s</p></div></div>\n'
                    % (ic(i, "h-5 w-5"), l, v) for i, l, v in PROGRAM_ROWS)
    prog = ('<section class="bg-cream py-14 lg:py-16"><div class="container-x">\n%s'
            '  <div class="mt-9 grid gap-6 lg:grid-cols-[1.4fr_1fr] lg:items-start">\n'
            '    <div class="grid gap-3 sm:grid-cols-2">\n%s    </div>\n'
            '    <div class="relative overflow-hidden rounded-2xl bg-navy-950 p-7 text-white sm:p-8">\n'
            '      <div class="grid-paper absolute inset-0 opacity-50" aria-hidden="true"></div>\n'
            '      <div class="absolute -right-16 -top-16 h-56 w-56 rounded-full bg-gold-500/20 blur-3xl" aria-hidden="true"></div>\n'
            '      <div class="relative">\n'
            '        <p class="font-display text-[28px] font-extrabold text-gold-400">%s</p>\n'
            '        <p class="mt-4 text-[13px] font-bold uppercase tracking-wider text-navy-200/80">%s</p>\n'
            '        <p class="font-display text-[40px] font-extrabold leading-none">%s</p>\n'
            '        <p class="hind mt-3 text-[13.5px] leading-relaxed text-navy-100/75">%s</p>\n'
            '        <div class="mt-6">%s</div>\n      </div>\n    </div>\n  </div>\n</div></section>\n'
            % (section_head("Program", "Program Details &amp; Fee"), prows,
               FEE["heading"], FEE["label"], FEE["amount"], FEE["note"], cta_row("dark")))

    # join process
    jsteps = ""
    for i, s in enumerate(JOIN_STEPS):
        pts = ('<ul class="mt-4 grid gap-2 sm:grid-cols-2">%s</ul>'
               % "".join('<li class="flex items-center gap-2.5 text-[13.5px] font-semibold text-navy-800">%s%s</li>'
                         % (ic("check", "h-4 w-4 shrink-0 text-gold-600"), p) for p in s["points"])) if s["points"] else ""
        cta = ('<a href="enroll.html" class="btn-primary mt-5">%s %s</a>' % (s["cta"], ic("arrow", "h-4 w-4"))) if s["cta"] else ""
        jsteps += ('    <div class="card p-6 sm:p-7">'
                   '<span class="grid h-10 w-10 place-items-center rounded-full bg-gold-400 font-display text-[16px] font-extrabold text-navy-950">%02d</span>'
                   '<h3 class="mt-4 text-[18px] font-extrabold text-navy-900">%s</h3>'
                   '<p class="hind mt-2.5 text-[14px] leading-relaxed text-navy-800">%s</p>%s%s</div>\n'
                   % (i + 1, s["title"], s["body"], pts, cta))
    ffields = "".join('<li class="hind flex items-start gap-2.5 text-[13.5px] leading-relaxed text-navy-800">%s%s</li>'
                      % (ic("check", "mt-1 h-3.5 w-3.5 shrink-0 text-gold-600"), f) for f in FORM_FIELDS)
    joinp = ('<section class="bg-white py-14 lg:py-16"><div class="container-x">\n%s'
             '  <div class="mt-9 grid gap-5 lg:grid-cols-2">\n%s  </div>\n'
             '  <div class="card mt-6 p-7"><h3 class="text-[18px] font-extrabold text-navy-900">Registration Form Fields</h3>'
             '<ul class="mt-4 grid gap-2 sm:grid-cols-2">%s</ul></div>\n</div></section>\n'
             % (section_head("Admission", "How to Join?", "केवल 2 Simple Steps"), jsteps, ffields))

    # journey
    jrn = "".join('    <li class="flex items-center gap-3 rounded-xl border border-white/12 bg-white/[0.06] px-4 py-3">'
                  '<span class="font-display text-[15px] font-extrabold text-gold-400">%02d</span>'
                  '<span class="text-[12.5px] font-bold uppercase tracking-wider text-white">%s</span></li>\n'
                  % (i + 1, s) for i, s in enumerate(JOURNEY))
    journey = ('<section class="relative overflow-hidden bg-navy-950 py-14 text-white lg:py-16">\n'
               '  <div class="grid-paper absolute inset-0 opacity-50" aria-hidden="true"></div>\n'
               '  <div class="container-x relative">\n%s'
               '    <ul class="mt-9 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">\n%s    </ul>\n'
               '  </div>\n</section>\n'
               % (section_head("Journey", "Student Learning Journey", "", True), jrn))

    faqs = ('<section class="bg-cream py-14 lg:py-16"><div class="container-x max-w-4xl">\n%s%s</div></section>\n'
            % (section_head("FAQ", "Frequently Asked Questions"), faq_block(FAQS)))

    final = ('<section class="bg-white py-14 lg:py-16"><div class="container-x">\n'
             '  <div class="relative overflow-hidden rounded-2xl bg-navy-950 p-8 text-center text-white sm:p-12">\n'
             '    <div class="grid-paper absolute inset-0 opacity-50" aria-hidden="true"></div>\n'
             '    <div class="absolute -right-20 -top-20 h-64 w-64 rounded-full bg-gold-500/20 blur-3xl" aria-hidden="true"></div>\n'
             '    <div class="relative">\n'
             '      <h2 class="h-display mx-auto max-w-3xl text-[30px] sm:text-[40px]">%s</h2>\n'
             '      <p class="hind mx-auto mt-4 max-w-2xl text-[15px] leading-relaxed text-navy-100/80">%s</p>\n'
             '      <p class="mt-5 text-[16px] font-extrabold text-gold-400">%s</p>\n'
             '      <div class="mt-7 flex justify-center">%s</div>\n'
             '      <p class="mt-7 text-[13.5px] font-semibold text-navy-200/75">%s</p>\n'
             '    </div>\n  </div>\n</div></section>\n'
             % (FINAL_CTA["heading"], FINAL_CTA["body"], FINAL_CTA["join"], cta_row("dark", True), STRAPLINE))

    page("index.html",
         "JRF @ ₹500 — Mission 2026 | UGC NET Paper-1 Mentorship | GS Net Academy",
         "UGC NET Paper-1 Special Mentorship + Foundation Program. Course fee FREE with a ₹500 registration contribution. Live classes on Google Meet at 6:30 PM, notes, PYQs, tests and mentorship.",
         hero + approach + results + batch + whyjoin + coverage + different + demo + fac +
         whyac + who + prog + joinp + journey + faqs + final,
         "index.html")


# =========================================================================== #
# ABOUT                                                                       #
# =========================================================================== #
def about():
    creds = "".join('<li class="flex items-start gap-2.5 text-[14px] text-navy-800">%s%s</li>'
                    % (ic("check", "mt-0.5 h-4 w-4 shrink-0 text-gold-600"), c) for c in FACULTY["credentials"])
    why = "".join('    <li class="card flex items-start gap-3 p-4">%s<span class="text-[13.5px] font-semibold text-navy-800">%s</span></li>\n'
                  % (ic("spark", "mt-0.5 h-4 w-4 shrink-0 text-gold-600"), w) for w in FACULTY["why"])
    points = "".join('    <li class="card card-hover flex items-center gap-3 p-4">'
                     '<span class="grid h-9 w-9 shrink-0 place-items-center rounded-lg bg-navy-900 font-display text-[14px] font-extrabold text-gold-400">%02d</span>'
                     '<span class="text-[13.5px] font-bold text-navy-900">%s</span></li>\n'
                     % (i + 1, p) for i, p in enumerate(WHY_ACADEMY["points"]))
    dif = "".join('    <div class="card card-hover h-full p-6">'
                  '<span class="grid h-9 w-9 place-items-center rounded-lg bg-gold-400 font-display text-[15px] font-extrabold text-navy-950">%s</span>'
                  '<h3 class="mt-4 text-[17px] font-extrabold text-navy-900">%s</h3>'
                  '<p class="hind mt-2 text-[13.5px] leading-relaxed text-navy-700">%s</p></div>\n'
                  % (n, t, d) for n, t, d in DIFFERENT)

    body = (page_head("About", 'About <span class="text-gold-400">GS Net Academy</span>',
                      SITE["subtitle"] + " — " + STRAPLINE,
                      '<div class="flex flex-wrap gap-3"><a href="enroll.html" class="btn-primary">✓ JOIN BATCH @ ₹500</a>'
                      '<a href="contact.html" class="btn-ghost-light">Contact us</a></div>') +
            '<section class="bg-cream py-14 lg:py-16"><div class="container-x">\n%s'
            '  <div class="mt-8 flex items-center gap-4 rounded-2xl bg-navy-950 p-5 text-white sm:p-6">'
            '<span class="grid h-11 w-11 shrink-0 place-items-center rounded-xl bg-gold-400/15 ring-1 ring-gold-400/30">%s</span>'
            '<p class="text-[13px] font-extrabold uppercase leading-relaxed tracking-wider text-gold-300 sm:text-[14px]">%s</p></div>\n'
            '  <ul class="mt-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">\n%s  </ul>\n</div></section>\n'
            % (section_head("Our mission", WHY_ACADEMY["heading"], WHY_ACADEMY["body"]),
               ic("trophy", "icon-gold h-6 w-6"), WHY_ACADEMY["formula"], points) +

            '<section class="bg-white py-14 lg:py-16"><div class="container-x grid gap-8 lg:grid-cols-[.8fr_1.2fr] lg:items-start">\n'
            '  <div>%s</div>\n  <div>\n'
            '    <span class="eyebrow">%s Faculty</span>\n'
            '    <h2 class="h-display mt-4 text-[30px] sm:text-[38px]">%s</h2>\n'
            '    <div class="rule-gold mt-4"></div>\n'
            '    <ul class="mt-6 grid gap-2.5">%s</ul>\n'
            '    <h3 class="mt-8 text-[19px] font-extrabold text-navy-900">%s</h3>\n'
            '    <ul class="mt-4 grid gap-3 sm:grid-cols-2">\n%s    </ul>\n'
            '    <p class="hind mt-6 rounded-xl border-l-4 border-gold-400 bg-gold-50 px-5 py-4 text-[14.5px] font-semibold leading-relaxed text-navy-900">%s</p>\n'
            '  </div>\n</div></section>\n'
            % (photo(FACULTY["photo"], FACULTY["name"], "aspect-[4/5] w-full rounded-2xl object-cover shadow-lift",
                     "Add the photo at " + FACULTY["photo"]),
               ic("cap", "h-3.5 w-3.5"), FACULTY["name"], creds, FACULTY["why_heading"], why, FACULTY["quote"]) +

            '<section class="bg-cream py-14 lg:py-16"><div class="container-x">\n%s'
            '  <div class="mt-9 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s  </div>\n'
            '  <p class="hind mt-8 flex items-start gap-2.5 rounded-xl border border-navy-900/10 bg-white p-5 text-[13.5px] leading-relaxed text-navy-700">%s%s</p>\n'
            '</div></section>\n'
            % (section_head("How we teach", "What Makes This Program Different?"), dif,
               ic("shield", "mt-0.5 h-4 w-4 shrink-0 text-navy-500"), WHY_JOIN["disclaimer"]) +
            cta_band())

    page("about.html", "About GS Net Academy | UGC NET Paper-1 Mentorship",
         "About GS Net Academy — faculty, teaching approach and the JRF @ ₹500 Mission 2026 initiative.",
         body, "about.html")


# =========================================================================== #
# COURSES                                                                     #
# =========================================================================== #
def courses():
    cards = ""
    for status, icn, href, title, tagline, badge, desc, points in COURSES:
        soon = status == "soon"
        pts = "".join('<li class="flex items-start gap-2 text-[13px] text-navy-700">%s%s</li>'
                      % (ic("check", "mt-0.5 h-3.5 w-3.5 shrink-0 text-gold-600"), p) for p in points)
        inner = ('<span class="grid h-12 w-12 place-items-center rounded-xl bg-navy-900 text-gold-400">%s</span>'
                 '<span class="mt-4 flex flex-wrap items-center gap-2">'
                 '<span class="text-[11px] font-extrabold uppercase tracking-[0.14em] text-gold-600">%s</span>%s</span>'
                 '<h2 class="mt-1 text-[19px] font-extrabold text-navy-900">%s</h2>'
                 '<p class="mt-2 text-[13.5px] leading-relaxed text-navy-700">%s</p>'
                 '<ul class="mt-4 grid flex-1 gap-2">%s</ul>%s'
                 % (ic(icn, "h-6 w-6"), tagline,
                    ('<span class="rounded-md bg-gold-50 px-2 py-0.5 text-[10.5px] font-extrabold text-gold-700">%s</span>' % badge) if badge else "",
                    title, desc, pts,
                    ('<span class="mt-5 inline-flex items-center gap-2 rounded-lg bg-navy-50 px-3 py-2 text-[12.5px] font-bold text-navy-500">%s Coming soon</span>' % ic("clock", "h-3.5 w-3.5"))
                    if soon else
                    ('<span class="mt-5 inline-flex items-center gap-1.5 border-t border-navy-900/8 pt-4 text-[13.5px] font-bold text-navy-800 transition group-hover:gap-2.5 group-hover:text-gold-600">View course %s</span>' % ic("arrow", "h-4 w-4"))))
        cards += ('    <div class="card flex h-full flex-col p-6 opacity-90">%s</div>\n' % inner) if soon \
                 else ('    <a href="%s" class="card card-hover group flex h-full flex-col p-6">%s</a>\n' % (href, inner))

    rows = "".join('        <tr class="border-t border-navy-900/8 %s">'
                   '<th scope="row" class="px-5 py-4 text-left font-bold text-navy-900">%s</th>'
                   '<td class="px-5 py-4 font-display text-[22px] font-extrabold text-navy-800">%s</td>'
                   '<td class="px-5 py-4 font-display text-[22px] font-extrabold text-gold-600">%s</td>'
                   '<td class="px-5 py-4 text-navy-700">%s</td></tr>\n'
                   % ("bg-gold-50 font-extrabold" if total else "", p, q, m, f)
                   for p, q, m, f, total in EXAM_PATTERN)

    facts = "".join('    <div class="card h-full p-5">%s'
                    '<p class="mt-3 text-[11px] font-extrabold uppercase tracking-[0.14em] text-navy-500">%s</p>'
                    '<p class="mt-1 text-[15px] font-extrabold text-navy-900">%s</p></div>\n'
                    % (ic(i, "h-5 w-5 text-gold-600"), l, v) for i, l, v in EXAM_FACTS)

    units = ""
    for (no, title, icn, blurb), (n, _t, desc) in zip(UNITS, COVERAGE):
        units += ('    <a href="unit-%d.html" class="card card-hover group flex h-full items-start gap-4 p-5">'
                  '<span class="grid h-11 w-11 shrink-0 place-items-center rounded-xl bg-navy-900 font-display text-[18px] font-extrabold text-gold-400">%s</span>'
                  '<div><h3 class="text-[16px] font-extrabold text-navy-900">%s</h3>'
                  '<p class="mt-1 text-[12.5px] font-bold text-navy-500">05 Questions · 10 Marks</p>'
                  '<p class="hind mt-1.5 text-[13px] leading-relaxed text-navy-700">%s</p></div></a>\n'
                  % (no, n, title, desc))

    body = (page_head("Courses", 'Our <span class="text-gold-400">Courses</span>',
                      "UGC NET Paper-I foundation and JRF mentorship — plus the tracks we are building next.",
                      '<div class="flex flex-wrap gap-3"><a href="enroll.html" class="btn-primary">✓ JOIN BATCH @ ₹500</a>'
                      '<a href="#paper-1" class="btn-ghost-light">Paper-I syllabus</a></div>') +
            '<section class="bg-cream py-14 lg:py-16"><div class="container-x">\n%s'
            '  <div class="mt-9 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">\n%s  </div>\n</div></section>\n'
            % (section_head("Catalogue", "What You Can Study With Us"), cards) +

            '<section id="paper-1" class="scroll-mt-24 bg-white py-14 lg:py-16"><div class="container-x">\n%s'
            '  <div class="mt-9 overflow-x-auto rounded-2xl border border-navy-900/10 shadow-card">\n'
            '    <table class="w-full min-w-[620px] bg-white text-left">\n'
            '      <thead><tr><th scope="col" class="px-5 py-4 text-[12px] font-extrabold uppercase tracking-[0.14em]">Paper</th>'
            '<th scope="col" class="px-5 py-4 text-[12px] font-extrabold uppercase tracking-[0.14em]">Questions</th>'
            '<th scope="col" class="px-5 py-4 text-[12px] font-extrabold uppercase tracking-[0.14em]">Marks</th>'
            '<th scope="col" class="px-5 py-4 text-[12px] font-extrabold uppercase tracking-[0.14em]">Focus</th></tr></thead>\n'
            '      <tbody class="text-[14.5px]">\n%s      </tbody>\n    </table>\n  </div>\n'
            '  <div class="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">\n%s  </div>\n</div></section>\n'
            % (section_head("Exam pattern", "Understand the Pattern. Plan Your Preparation.",
                            "Both papers are compulsory and the exam is conducted by NTA in CBT mode."), rows, facts) +

            '<section class="bg-cream py-14 lg:py-16"><div class="container-x">\n%s'
            '  <div class="mt-9 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s  </div>\n'
            '  <div class="mt-8 flex flex-wrap justify-center gap-3">'
            '<a href="notes.html" class="btn-dark">Open Paper-I Notes</a>'
            '<a href="tutorials.html" class="btn-outline">Tutorial Modules</a></div>\n</div></section>\n'
            % (section_head("Syllabus", "10 Units — 5 Questions Each",
                            "हर unit में 5 questions और 10 marks होते हैं। Batch सभी दस units को fixed sequence में cover करता है।"), units) +
            cta_band())

    page("courses.html", "Courses &amp; UGC NET Paper-1 Syllabus | GS Net Academy",
         "All GS Net Academy courses plus the complete UGC NET Paper-1 exam pattern, 10 units and preparation plan.",
         body, "courses.html")


# =========================================================================== #
# TUTORIALS + one page per unit                                               #
# =========================================================================== #
def tutorials():
    total = sum(len(MODULES[u[0]]) for u in UNITS)
    cards = ""
    for no, title, icn, blurb in UNITS:
        mods = MODULES[no]
        bars = "".join('<span class="h-1.5 flex-1 rounded-full bg-navy-900/12"></span>' for _ in mods)
        cards += ('    <a href="unit-%d.html" class="card card-hover group relative flex h-full flex-col overflow-hidden p-6">\n'
                  '      <span class="pointer-events-none absolute -right-5 -top-7 font-display text-[86px] font-extrabold leading-none text-navy-900/[0.045]" aria-hidden="true">%02d</span>\n'
                  '      <div class="relative flex items-center gap-3">'
                  '<span class="grid h-11 w-11 shrink-0 place-items-center rounded-xl bg-navy-900 text-gold-400 transition-colors group-hover:bg-gold-400 group-hover:text-navy-950">%s</span>'
                  '<div><p class="text-[10.5px] font-extrabold uppercase tracking-[0.16em] text-gold-600">Unit %d</p>'
                  '<p class="text-[12px] font-bold text-navy-500">05 Questions · 10 Marks</p></div></div>\n'
                  '      <h2 class="relative mt-4 text-[18px] font-extrabold leading-snug text-navy-900">%s</h2>\n'
                  '      <p class="relative mt-2 flex-1 text-[13.5px] leading-relaxed text-navy-700">%s</p>\n'
                  '      <div class="relative mt-5"><div class="flex items-center justify-between text-[12px] font-bold text-navy-600">'
                  '<span>%d Modules</span><span class="text-navy-400">0/%d ready</span></div>'
                  '<div class="mt-2 flex gap-1" aria-hidden="true">%s</div></div>\n'
                  '      <span class="relative mt-5 inline-flex items-center gap-1.5 border-t border-navy-900/8 pt-4 text-[13.5px] font-bold text-navy-800 transition group-hover:gap-2.5 group-hover:text-gold-600">Open unit %s</span>\n'
                  '    </a>\n'
                  % (no, no, ic(icn, "h-5 w-5"), no, title, blurb, len(mods), len(mods), bars, ic("arrow", "h-4 w-4")))

    body = (page_head("Tutorials", 'Units &amp; <span class="text-gold-400">Tutorial Modules</span>',
                      "सभी 10 Paper-I units, हर unit के छोटे-छोटे modules में बँटे हुए।",
                      '<div class="flex flex-wrap gap-3 text-[13.5px] font-bold text-white">'
                      '<span class="inline-flex items-center gap-2 rounded-lg border border-white/15 bg-white/10 px-3.5 py-2">%s 10 Units</span>'
                      '<span class="inline-flex items-center gap-2 rounded-lg border border-white/15 bg-white/10 px-3.5 py-2">%s %d Modules</span></div>'
                      % (ic("layers", "h-4 w-4 icon-gold"), ic("book", "h-4 w-4 icon-gold"), total)) +
            '<section class="bg-cream py-12 lg:py-14"><div class="container-x">\n'
            '  <div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">\n%s  </div>\n'
            '  <div class="card mt-9 flex flex-col items-center gap-4 p-8 text-center sm:flex-row sm:justify-between sm:text-left">\n'
            '    <div><h2 class="text-[19px] font-extrabold text-navy-900">Want these topics taught live?</h2>'
            '<p class="mt-1.5 text-[14.5px] text-navy-700">Every unit is covered in the Paper-I batch at <strong>%s</strong> daily.</p></div>\n'
            '    <a href="enroll.html" class="btn-primary shrink-0">✓ JOIN BATCH @ ₹500</a>\n  </div>\n</div></section>\n'
            % (cards, SITE["class_time"]) + cta_band())

    page("tutorials.html", "UGC NET Paper-I Units &amp; Tutorial Modules | GS Net Academy",
         "All 10 UGC NET Paper-I units broken into short tutorial modules.", body, "tutorials.html")

    # one finished page per unit
    for idx, (no, title, icn, blurb) in enumerate(UNITS):
        mods = MODULES[no]
        items = ""
        for i, m in enumerate(mods):
            items += ('    <li><article class="card card-hover flex flex-col gap-4 p-5 sm:flex-row sm:items-center sm:p-6">'
                      '<span class="grid h-12 w-12 shrink-0 place-items-center rounded-xl bg-navy-50 font-display text-[18px] font-extrabold text-navy-400">%02d</span>'
                      '<div class="min-w-0 flex-1">'
                      '<p class="text-[10.5px] font-extrabold uppercase tracking-[0.16em] text-gold-600">Module %d · Unit %d</p>'
                      '<h2 class="mt-1 text-[16.5px] font-extrabold leading-snug text-navy-900">%s</h2></div>'
                      '<span class="inline-flex shrink-0 items-center gap-1.5 rounded-lg bg-navy-50 px-3 py-2 text-[12.5px] font-bold text-navy-500">%s Coming soon</span>'
                      '</article></li>\n' % (i + 1, i + 1, no, m, ic("clock", "h-3.5 w-3.5")))

        prev = UNITS[idx - 1] if idx > 0 else None
        nxt = UNITS[idx + 1] if idx < len(UNITS) - 1 else None
        nav = '  <div class="mt-8 flex flex-col gap-3 sm:flex-row sm:justify-between">\n'
        nav += ('    <a href="unit-%d.html" class="btn-outline">← Unit %d · %s</a>\n' % (prev[0], prev[0], prev[1])) if prev else "    <span></span>\n"
        nav += ('    <a href="unit-%d.html" class="btn-dark">Unit %d · %s →</a>\n' % (nxt[0], nxt[0], nxt[1])) if nxt else ""
        nav += "  </div>\n"

        body = (page_head("Unit %d · 05 Questions · 10 Marks" % no, title, blurb,
                          '<div class="flex flex-wrap items-center gap-3">'
                          '<a href="tutorials.html" class="btn-ghost-light btn-sm">%s All units</a>'
                          '<span class="inline-flex items-center gap-2 rounded-lg border border-white/15 bg-white/10 px-3.5 py-2 text-[13px] font-bold text-white">%s %d Modules</span></div>'
                          % (ic("layers", "h-3.5 w-3.5"), ic("book", "h-4 w-4 icon-gold"), len(mods))) +
                '<section class="bg-cream py-10 lg:py-12"><div class="container-x">\n'
                '  <ol class="grid gap-4">\n%s  </ol>\n%s</div></section>\n' % (items, nav) + cta_band())

        page("unit-%d.html" % no, "Unit %d: %s — Paper-I Modules | GS Net Academy" % (no, title),
             "%s — %d tutorial modules for UGC NET Paper-I." % (title, len(mods)), body, "tutorials.html")


# =========================================================================== #
# NOTES                                                                       #
# =========================================================================== #
def notes():
    cards = ""
    for i, (no, title, icn, blurb) in enumerate(UNITS):
        cards += ('    <article class="card card-hover flex h-full flex-col p-6">\n'
                  '      <div class="flex items-center gap-3">'
                  '<span class="grid h-11 w-11 shrink-0 place-items-center rounded-xl bg-navy-900 font-display text-[18px] font-extrabold text-gold-400">%02d</span>'
                  '<div><p class="text-[10.5px] font-extrabold uppercase tracking-[0.16em] text-gold-600">Unit %d</p>'
                  '<p class="text-[12px] font-bold text-navy-500">Free</p></div></div>\n'
                  '      <h2 class="mt-4 text-[17px] font-extrabold leading-snug text-navy-900">%s</h2>\n'
                  '      <p class="mt-2 flex-1 text-[13.5px] leading-relaxed text-navy-700">%s</p>\n'
                  '      <span class="mt-5 inline-flex items-center justify-center gap-1.5 rounded-xl bg-navy-50 px-3 py-3 text-[12.5px] font-bold text-navy-500">%s Coming soon</span>\n'
                  '    </article>\n' % (i + 1, no, title, blurb, ic("clock", "h-3.5 w-3.5")))

    body = (page_head("Paper-I Notes", 'Unit-wise <span class="text-gold-400">PDF Notes</span>',
                      "हर unit के exam-oriented notes.",
                      '<div class="flex flex-wrap gap-3"><a href="enroll.html" class="btn-primary">✓ JOIN BATCH @ ₹500</a>'
                      '<a href="tutorials.html" class="btn-ghost-light">Tutorial modules</a></div>') +
            '<section class="bg-cream py-12 lg:py-14"><div class="container-x">\n%s'
            '  <div class="mt-9 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">\n%s  </div>\n'
            '  <div class="card mt-8 flex flex-col gap-5 p-8 sm:flex-row sm:items-center sm:justify-between">\n'
            '    <div><span class="eyebrow">%s Individual PDF — %s</span>\n'
            '      <h2 class="mt-3 text-[19px] font-extrabold text-navy-900">Need only a specific Paper-I note?</h2>\n'
            '      <p class="mt-1.5 max-w-lg text-[14.5px] text-navy-700">एक unit की PDF %s में request कीजिए। Support को unit का नाम बताइए, payment details आपको भेज दी जाएँगी।</p></div>\n'
            '    <a href="tel:+91%s" class="btn-primary shrink-0">Get PDF for %s</a>\n  </div>\n</div></section>\n'
            % (section_head("Study material", "Paper-I Notes",
                            "PDF तैयार होते ही यहाँ download link आ जाएगा।"),
               cards, ic("pdf", "h-3.5 w-3.5"), SITE["pdf_price"], SITE["pdf_price"],
               SITE["phones"][0], SITE["pdf_price"]) + cta_band())

    page("notes.html", "UGC NET Paper-I PDF Notes | GS Net Academy",
         "Unit-wise UGC NET Paper-I PDF notes from GS Net Academy.", body, "notes.html")


# =========================================================================== #
# CONTACT                                                                     #
# =========================================================================== #
def contact():
    phones = "".join('    <a href="tel:+91%s" class="card card-hover flex items-center gap-4 p-5">'
                     '<span class="grid h-11 w-11 shrink-0 place-items-center rounded-xl bg-navy-900 text-gold-400">%s</span>'
                     '<span><span class="block text-[11px] font-extrabold uppercase tracking-[0.14em] text-navy-500">Call now</span>'
                     '<span class="block font-display text-[22px] font-extrabold text-navy-900">+91 %s</span></span></a>\n'
                     % (p, ic("phone", "h-5 w-5", True), p) for p in SITE["phones"])

    quick = [("mail", "Email", SITE["email"], "mailto:" + SITE["email"]),
             ("whatsapp", "WhatsApp Group", "Join the student community", SITE["whatsapp_group"]),
             ("clock", "Class time", SITE["class_time"] + " daily", ""),
             ("globe", "Platform", "Google Meet (online)", "")]
    qhtml = ""
    for icn, label, value, href in quick:
        inner = ('<span class="grid h-10 w-10 shrink-0 place-items-center rounded-xl bg-gold-50 text-gold-600 ring-1 ring-gold-200">%s</span>'
                 '<span class="min-w-0"><span class="block text-[11px] font-extrabold uppercase tracking-[0.14em] text-navy-500">%s</span>'
                 '<span class="block break-all text-[14.5px] font-extrabold text-navy-900">%s</span></span>'
                 % (ic(icn, "h-5 w-5"), label, value))
        if href:
            ext = ' target="_blank" rel="noreferrer noopener"' if href.startswith("http") else ""
            qhtml += '    <a href="%s"%s class="card card-hover flex items-center gap-3.5 p-5">%s</a>\n' % (href, ext, inner)
        else:
            qhtml += '    <div class="card flex items-center gap-3.5 p-5">%s</div>\n' % inner

    bpoints = "".join('<li class="flex items-start gap-2.5 text-[14px] text-navy-100/85">%s%s</li>'
                      % (ic("check", "mt-0.5 h-4 w-4 shrink-0 icon-gold"), p) for p in BATCH["points"])

    body = (page_head("Contact", 'Talk to <span class="text-gold-400">GS Net Academy</span>',
                      "Batch, notes, registration — किसी भी सवाल के लिए सीधे call या WhatsApp कीजिए।",
                      '<div class="flex flex-wrap gap-3"><a href="tel:+91%s" class="btn-primary">%s Call %s</a>'
                      '<a href="%s" target="_blank" rel="noreferrer noopener" class="btn-ghost-light">%s WhatsApp Group</a></div>'
                      % (SITE["phones"][0], ic("phone", "h-4 w-4", True), SITE["phones"][0],
                         SITE["whatsapp_group"], ic("whatsapp", "h-4 w-4"))) +
            '<section class="bg-cream py-14 lg:py-16"><div class="container-x">\n'
            '  <div class="grid gap-4 sm:grid-cols-2">\n%s  </div>\n'
            '  <div class="mt-4 grid gap-4 sm:grid-cols-2">\n%s  </div>\n'
            '  <div class="mt-8 grid gap-6 lg:grid-cols-[1.1fr_.9fr] lg:items-start">\n'
            '    <div class="card p-7 sm:p-8">\n'
            '      <h2 class="text-[21px] font-extrabold text-navy-900">Send an enquiry</h2>\n'
            '      <p class="mt-1.5 text-[14px] text-navy-700">Form भरिए — यह आपके email app में एक ready message खोल देगा।</p>\n'
            '      <form action="mailto:%s" method="post" enctype="text/plain" class="mt-6 grid gap-4">\n'
            '        <label><span class="field-label">Full name</span><input type="text" name="Name" required class="field" autocomplete="name"></label>\n'
            '        <div class="grid gap-4 sm:grid-cols-2">\n'
            '          <label><span class="field-label">Mobile / WhatsApp</span><input type="tel" name="Phone" required class="field" autocomplete="tel"></label>\n'
            '          <label><span class="field-label">Email</span><input type="email" name="Email" class="field" autocomplete="email"></label>\n'
            '        </div>\n'
            '        <label><span class="field-label">Your subject (Paper-2)</span><input type="text" name="Subject" class="field"></label>\n'
            '        <label><span class="field-label">Message</span><textarea name="Message" rows="4" required class="field"></textarea></label>\n'
            '        <button type="submit" class="btn-primary mt-1">%s Send enquiry</button>\n'
            '        <p class="text-[12px] text-navy-500">Form आपका email app खोलता है। सीधे भी लिख सकते हैं: %s</p>\n'
            '      </form>\n    </div>\n'
            '    <div class="relative overflow-hidden rounded-2xl bg-navy-950 p-7 text-white sm:p-8">\n'
            '      <div class="grid-paper absolute inset-0 opacity-50" aria-hidden="true"></div>\n'
            '      <div class="absolute -right-20 -top-20 h-64 w-64 rounded-full bg-gold-500/15 blur-3xl" aria-hidden="true"></div>\n'
            '      <div class="relative">\n'
            '        <span class="inline-flex items-center gap-2 rounded-full bg-emerald-500/15 px-3.5 py-1.5 text-[11px] font-extrabold uppercase tracking-[0.16em] text-emerald-300 ring-1 ring-emerald-400/30">'
            '<span class="h-1.5 w-1.5 rounded-full bg-emerald-400"></span> Direct call available</span>\n'
            '        <h2 class="h-display mt-4 text-[30px] sm:text-[36px]">Need Help Before Joining?</h2>\n'
            '        <p class="mt-3 text-[14.5px] text-navy-100/80">Registration, payment, notes या class schedule — किसी भी बात के लिए हमें call कीजिए।</p>\n'
            '        <ul class="mt-6 grid gap-2.5">%s</ul>\n'
            '        <div class="mt-7">%s</div>\n'
            '        <p class="mt-5 break-all text-[13.5px] text-navy-200/70">%s · %s</p>\n'
            '      </div>\n    </div>\n  </div>\n</div></section>\n'
            % (phones, qhtml, SITE["email"], ic("mail", "h-4 w-4"), SITE["email"],
               bpoints, cta_row("dark"), SITE["email"], SITE["website"]))

    page("contact.html", "Contact GS Net Academy | Phone, Email &amp; WhatsApp",
         "Talk to the GS Net Academy team about the UGC NET Paper-1 batch, notes and registration.",
         body, "contact.html")


# =========================================================================== #
# ENROLL                                                                      #
# =========================================================================== #
def enroll():
    summary = "".join('    <div class="flex items-center gap-3.5 rounded-xl border border-navy-900/10 bg-cream px-5 py-4">%s'
                      '<div><p class="text-[11px] font-extrabold uppercase tracking-[0.14em] text-navy-500">%s</p>'
                      '<p class="text-[16px] font-extrabold text-navy-900">%s</p></div></div>\n'
                      % (ic(i, "h-5 w-5 shrink-0 text-gold-600"), l, v)
                      for i, l, v in [("calendar", "Batch started", SITE["batch_start"]),
                                      ("clock", "Class time", SITE["class_time"] + " daily"),
                                      ("cap", "Course fee", "FREE"),
                                      ("rupee", "Contribution", SITE["contribution"] + " only")])

    steps = [("01", "clipboard", "Registration",
              "Google Form में अपनी details भरिए। इसी से आप Paper-I batch के लिए register होते हैं।",
              "", ("Open Google Form", SITE["google_form"], "btn-primary")),
             ("02", "rupee", "Payment",
              SITE["contribution"] + " — Registration &amp; Academic/Logistics Contribution. Course बिल्कुल FREE है।",
              "Payment details form submit करने के बाद आपको भेजी जाती हैं — ये कभी इस page पर नहीं दिखाई जातीं।", None),
             ("03", "notes", "Payment screenshot भेजिए",
              "Form / confirmation message में बताए तरीके से payment screenshot share कीजिए ताकि seat verify हो सके।",
              "", None),
             ("04", "users", "Class community join कीजिए",
              "Confirmation के बाद class link, PDF notes, announcements और study material class community में मिलते हैं।",
              "", ("Join WhatsApp Group", SITE["whatsapp_group"], "btn-dark"))]

    shtml = ""
    for n, icn, title, text, note, cta in steps:
        shtml += ('    <li class="relative"><div class="flex gap-5">'
                  '<span class="relative z-10 hidden h-14 w-14 shrink-0 place-items-center rounded-2xl bg-navy-950 font-display text-[20px] font-extrabold text-gold-400 shadow-card sm:grid">%s</span>'
                  '<div class="card w-full p-7">'
                  '<div class="flex items-center gap-3">'
                  '<span class="grid h-10 w-10 place-items-center rounded-xl bg-gold-50 text-gold-600 ring-1 ring-gold-200">%s</span>'
                  '<div><p class="text-[11px] font-extrabold uppercase tracking-[0.16em] text-gold-600">Step %s</p>'
                  '<h2 class="text-[19px] font-extrabold text-navy-900">%s</h2></div></div>'
                  '<p class="hind mt-4 text-[15px] leading-relaxed text-navy-800">%s</p>%s%s'
                  '</div></div></li>\n'
                  % (n, ic(icn, "h-5 w-5"), n, title, text,
                     ('<p class="hind mt-4 flex items-start gap-2.5 rounded-xl bg-navy-50 p-4 text-[13.5px] leading-relaxed text-navy-700">%s%s</p>'
                      % (ic("shield", "mt-0.5 h-4 w-4 shrink-0 text-navy-500"), note)) if note else "",
                     ('<a href="%s" target="_blank" rel="noreferrer noopener" class="%s mt-5">%s %s</a>'
                      % (cta[1], cta[2], cta[0], ic("external", "h-4 w-4"))) if cta else ""))

    fields = "".join('<li class="hind flex items-start gap-2.5 text-[13.5px] leading-relaxed text-navy-800">%s%s</li>'
                     % (ic("check", "mt-1 h-3.5 w-3.5 shrink-0 text-gold-600"), f) for f in FORM_FIELDS)

    callcards = "".join('        <a href="tel:+91%s" class="flex items-center gap-4 rounded-xl border border-white/12 bg-white/[0.07] px-5 py-4 transition hover:border-gold-400/60 hover:bg-white/10">'
                        '<span class="grid h-11 w-11 shrink-0 place-items-center rounded-xl bg-gold-400 text-navy-950">%s</span>'
                        '<span><span class="block text-[11px] font-bold uppercase tracking-[0.14em] text-navy-200/70">Call now</span>'
                        '<span class="block font-display text-[22px] font-extrabold">+91 %s</span></span></a>\n'
                        % (p, ic("phone", "h-5 w-5", True), p) for p in SITE["phones"])

    body = (page_head("Registration", 'Join JRF <span class="text-gold-400">@ ₹500</span> Mission 2026',
                      "Course fee FREE — ₹500 सिर्फ registration और academic/logistics support के लिए।",
                      '<div class="flex flex-wrap gap-3">'
                      '<a href="%s" target="_blank" rel="noreferrer noopener" class="btn-primary">Start registration</a>'
                      '<a href="tel:+91%s" class="btn-ghost-light">%s Call %s</a></div>'
                      % (SITE["google_form"], SITE["phones"][0], ic("phone", "h-4 w-4", True), SITE["phones"][0])) +
            '<section class="border-b border-navy-900/8 bg-white py-8"><div class="container-x grid gap-4 sm:grid-cols-2 lg:grid-cols-4">\n%s</div></section>\n' % summary +
            '<section class="bg-cream py-14 lg:py-16"><div class="container-x max-w-4xl">\n'
            '  <ol class="grid gap-6">\n%s  </ol>\n'
            '  <div class="card mt-8 p-7"><h2 class="text-[19px] font-extrabold text-navy-900">Registration Form Fields</h2>'
            '<p class="mt-1.5 text-[14px] text-navy-700">Form में ये details माँगी जाती हैं:</p>'
            '<ul class="mt-4 grid gap-2 sm:grid-cols-2">%s</ul></div>\n'
            '  <div class="relative mt-8 overflow-hidden rounded-2xl bg-navy-950 p-8 text-white sm:p-10">\n'
            '    <div class="grid-paper absolute inset-0 opacity-50" aria-hidden="true"></div>\n'
            '    <div class="absolute -right-20 -top-20 h-64 w-64 rounded-full bg-gold-500/15 blur-3xl" aria-hidden="true"></div>\n'
            '    <div class="relative">\n'
            '      <h2 class="h-display text-[30px] sm:text-[38px]">Need Help With Registration?</h2>\n'
            '      <p class="mt-3 max-w-lg text-[15px] text-navy-200/80">Call या email कीजिए — form, payment और community के steps हम समझा देंगे।</p>\n'
            '      <div class="mt-7 grid gap-3 sm:grid-cols-2">\n%s      </div>\n'
            '      <div class="mt-3 flex flex-col gap-3 sm:flex-row">'
            '<a href="mailto:%s" class="btn-primary w-full sm:w-auto">%s Email support</a>'
            '<a href="%s" target="_blank" rel="noreferrer noopener" class="btn-ghost-light w-full sm:w-auto">%s WhatsApp Group</a></div>\n'
            '      <p class="mt-4 break-all text-[13.5px] text-navy-200/70">%s</p>\n'
            '    </div>\n  </div>\n</div></section>\n'
            % (shtml, fields, callcards, SITE["email"], ic("mail", "h-4 w-4"),
               SITE["whatsapp_group"], ic("whatsapp", "h-4 w-4"), SITE["email"]))

    page("enroll.html", "Enroll — JRF @ ₹500 Mission 2026 | GS Net Academy",
         "Register for the UGC NET Paper-1 Foundation Program. Course fee FREE, ₹500 registration contribution.",
         body, "enroll.html")


# =========================================================================== #
# BLOG — list page + one finished HTML file per article                       #
# =========================================================================== #
def fmt_date(d):
    y, m, dd = d.split("-")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return "%d %s %s" % (int(dd), months[int(m) - 1], y)


def post_file(slug):
    return "blog-" + slug + ".html"


def block_html(b):
    if "stats" in b:
        return ('<div class="mt-5 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">%s</div>'
                % "".join('<div class="rounded-xl border border-navy-900/10 bg-navy-50 px-4 py-3.5">'
                          '<p class="flex items-center gap-1.5 text-[11px] font-extrabold uppercase tracking-wider text-navy-500">%s%s</p>'
                          '<p class="mt-1.5 text-[14.5px] font-extrabold leading-snug text-navy-900">%s</p></div>'
                          % (ic(s.get("icon", "spark"), "h-3.5 w-3.5 text-gold-600"), s["label"], s["value"])
                          for s in b["stats"]))
    if "chips" in b:
        return ('<div class="mt-5 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">%s</div>'
                % "".join('<div class="flex items-center gap-3 rounded-xl border border-navy-900/10 bg-navy-50 px-4 py-3">'
                          '<span class="grid h-9 w-9 shrink-0 place-items-center rounded-lg bg-white text-gold-600 ring-1 ring-navy-900/10">%s</span>'
                          '<span class="text-[13.5px] font-bold leading-snug text-navy-900">%s</span></div>'
                          % (ic(c.get("icon", "book"), "h-[18px] w-[18px]"), c["label"]) for c in b["chips"]))
    if "phases" in b:
        out = ""
        for i, p in enumerate(b["phases"]):
            pts = "".join('<li class="flex items-start gap-2 text-[13.5px] leading-relaxed text-navy-800">%s%s</li>'
                          % (ic("check", "mt-0.5 h-3.5 w-3.5 shrink-0 text-emerald-600"), t) for t in p["points"])
            arrow = ('<span class="absolute -right-3 top-1/2 hidden -translate-y-1/2 text-navy-300 lg:block">%s</span>'
                     % ic("arrow", "h-5 w-5")) if i < len(b["phases"]) - 1 else ""
            out += ('<div class="relative rounded-2xl border border-navy-900/10 bg-navy-50 p-5">'
                    '<p class="text-[15.5px] font-extrabold text-navy-900">%s</p>'
                    '<p class="text-[13px] font-extrabold uppercase tracking-wider text-gold-600">%s</p>'
                    '<ul class="mt-3.5 grid gap-2">%s</ul>%s</div>' % (p["title"], p["sub"], pts, arrow))
        return '<div class="mt-5 grid gap-4 lg:grid-cols-3">%s</div>' % out
    if "plan" in b:
        return ('<div class="mt-5 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">%s</div>'
                % "".join('<div class="flex items-center gap-2.5 rounded-xl border border-navy-900/10 bg-navy-50 px-4 py-3.5">%s'
                          '<span class="text-[13.5px] font-bold text-navy-900">%s</span></div>'
                          % (ic(p.get("icon", "check"), "h-[18px] w-[18px] shrink-0 text-emerald-600"), p["label"])
                          for p in b["plan"]))
    if "tips" in b:
        return ('<ul class="mt-5 grid gap-3 rounded-2xl border border-gold-200 bg-gold-50 p-5">%s</ul>'
                % "".join('<li class="flex items-start gap-3">'
                          '<span class="mt-0.5 grid h-5 w-5 shrink-0 place-items-center rounded-md bg-gold-400 text-navy-950">%s</span>'
                          '<span class="text-[14px] leading-relaxed text-navy-900"><strong class="font-extrabold">%s:</strong> %s</span></li>'
                          % (ic("check", "h-3.5 w-3.5"), t["title"], t["text"]) for t in b["tips"]))
    if "book" in b:
        bk = b["book"]
        return ('<div class="mt-5 flex flex-col gap-4 rounded-2xl border border-navy-900/10 bg-navy-50 p-5 sm:flex-row sm:items-center">'
                '<span class="grid h-14 w-14 shrink-0 place-items-center rounded-xl bg-navy-950">%s</span><div>'
                '<p class="text-[15.5px] font-extrabold leading-snug text-navy-900">&ldquo;%s&rdquo;</p>'
                '<p class="mt-0.5 text-[13px] font-bold text-gold-600">by %s</p>'
                '<p class="mt-2 text-[14px] leading-relaxed text-navy-700">%s</p></div></div>'
                % (ic("book", "icon-gold h-7 w-7"), bk["title"], bk["author"], bk["text"]))
    if "quote" in b:
        return ('<p class="mt-5 rounded-xl border-l-4 border-gold-400 bg-gold-50 px-5 py-4 text-[15px] font-semibold leading-relaxed text-navy-900">%s</p>'
                % b["quote"])
    if "list" in b:
        return ('<ul class="mt-4 grid gap-2.5">%s</ul>'
                % "".join('<li class="flex items-start gap-2.5 text-[14.5px] leading-relaxed text-navy-800">%s%s</li>'
                          % (ic("check", "mt-1 h-4 w-4 shrink-0 text-gold-600"), li) for li in b["list"]))
    return '<p class="mt-4 text-[15px] leading-relaxed text-navy-800">%s</p>' % b["p"]


CTA_MAP = {"/enroll": "enroll.html", "/notes": "notes.html",
           "/tutorials": "tutorials.html", "/contact": "contact.html"}


def blog():
    posts = sorted(BLOGS, key=lambda b: b["date"], reverse=True)

    # ------------------------------ list page ------------------------------ #
    cards = ""
    for p in posts:
        cover = ('<img src="%s" alt="%s" loading="lazy" class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105">'
                 % (p["cover"], p["title"])) if p.get("cover") else \
                ('<span class="relative grid h-full w-full place-items-center bg-navy-950">'
                 '<span class="grid-paper absolute inset-0 opacity-60"></span>'
                 '<span class="absolute -right-10 -top-10 h-40 w-40 rounded-full bg-gold-500/20 blur-2xl"></span>%s</span>'
                 % ic("notes", "icon-gold relative h-10 w-10"))
        cards += ('    <a href="%s" class="card card-hover group flex h-full flex-col overflow-hidden">\n'
                  '      <span class="block aspect-[16/9] w-full overflow-hidden">%s</span>\n'
                  '      <span class="flex flex-1 flex-col p-6">\n'
                  '        <span class="flex flex-wrap items-center gap-2.5 text-[11px] font-extrabold uppercase tracking-[0.14em]">'
                  '<span class="rounded-md bg-gold-50 px-2 py-1 text-gold-600">%s</span>'
                  '<span class="text-navy-500">%s</span><span class="text-navy-500">· %s</span></span>\n'
                  '        <h2 class="mt-3 text-[18px] font-extrabold leading-snug text-navy-900">%s %s</h2>\n'
                  '        <p class="mt-2 flex-1 text-[14px] leading-relaxed text-navy-700">%s</p>\n'
                  '        <span class="mt-5 inline-flex items-center gap-1.5 border-t border-navy-900/8 pt-4 text-[13.5px] font-bold text-navy-800 transition group-hover:gap-2.5 group-hover:text-gold-600">Read article %s</span>\n'
                  '      </span>\n    </a>\n'
                  % (post_file(p["slug"]), cover, p["tag"], fmt_date(p["date"]), p.get("readTime", ""),
                     p["title"], p.get("titleHighlight", ""), p["excerpt"], ic("arrow", "h-4 w-4")))

    body = (page_head("Blog", 'Articles &amp; <span class="text-gold-400">Study Tips</span>',
                      "UGC NET Paper-1 की strategy, exam pattern aur preparation se judi articles — ek jagah.") +
            '<section class="bg-cream py-12 lg:py-14"><div class="container-x">\n'
            '  <div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">\n%s  </div>\n</div></section>\n' % cards +
            cta_band())
    page("blog.html", "Blog — UGC NET Paper-1 Tips, Strategy &amp; Exam Updates | GS Net Academy",
         "Preparation strategy, exam pattern, JRF planning and study tips for UGC NET Paper-1 aspirants.",
         body, "blog.html")

    # --------------------------- one page per post -------------------------- #
    for p in posts:
        others = [b for b in posts if b["slug"] != p["slug"]][:3]
        secs = p.get("sections", [])
        au = p["author"]
        initials = "".join(w[0] for w in au["name"].replace("Er.", "").replace("Dr.", "").split()[:2])

        author_card = ('<div class="card p-6 text-center">'
                       '<p class="text-left text-[15.5px] font-extrabold text-navy-900">About the Author</p>'
                       '<span class="mx-auto mt-4 block aspect-square w-full max-w-[190px] overflow-hidden rounded-xl bg-navy-50">'
                       '<span class="grid h-full w-full place-items-center bg-navy-950 font-display text-[44px] font-extrabold text-gold-400">%s</span></span>'
                       '<p class="mt-4 text-[16px] font-extrabold text-navy-900">%s</p>'
                       '<p class="text-[13px] font-semibold text-navy-600">%s</p>'
                       '<p class="mt-3 inline-block rounded-lg bg-gold-50 px-3 py-1.5 text-[12px] font-extrabold text-gold-700">%s</p>'
                       '<p class="mt-3 text-[13px] leading-relaxed text-navy-700">%s</p></div>'
                       % (initials, au["name"], au["role"], au.get("experience", ""), au.get("note", "")))

        toc = ('<div class="card p-6"><p class="text-[15.5px] font-extrabold text-navy-900">Table of Contents</p>'
               '<ul class="mt-4 grid gap-1">%s</ul></div>'
               % "".join('<li><a href="#%s" class="flex items-start gap-2.5 rounded-lg px-2 py-2 text-[13.5px] font-semibold text-navy-600 transition hover:bg-gold-50 hover:text-navy-900">'
                         '<span class="mt-1.5 h-2 w-2 shrink-0 rounded-full bg-navy-900/20"></span>%s</a></li>'
                         % (s["id"], s["title"]) for s in secs)) if secs else ""

        latest = ('<div class="card p-6"><p class="text-[15.5px] font-extrabold text-navy-900">Latest Articles</p>'
                  '<ul class="mt-4 grid gap-4">%s</ul></div>'
                  % "".join('<li><a href="%s" class="group flex gap-3">'
                            '<span class="grid h-12 w-12 shrink-0 place-items-center rounded-lg bg-navy-950">%s</span>'
                            '<span class="min-w-0"><span class="block text-[13px] font-bold leading-snug text-navy-900 transition group-hover:text-gold-600">%s</span>'
                            '<span class="mt-1 block text-[11.5px] font-semibold text-navy-500">%s</span></span></a></li>'
                            % (post_file(b["slug"]), ic("notes", "icon-gold h-5 w-5"),
                               b.get("titleHighlight") or b["title"], fmt_date(b["date"])) for b in others))

        sidebar = ('<aside><div class="grid gap-5 lg:sticky lg:top-24">%s%s'
                   '<div class="rounded-2xl border border-gold-200 bg-gold-50 p-6">'
                   '<p class="text-[17px] font-extrabold leading-snug text-navy-900">Get UGC NET Study Material</p>'
                   '<p class="mt-2 text-[13.5px] leading-relaxed text-navy-700">Download FREE Notes, PYQs &amp; Sample PDFs to boost your prep.</p>'
                   '<a href="notes.html" class="btn-primary mt-4 w-full">%s Download Now</a></div>%s'
                   '<div class="relative overflow-hidden rounded-2xl bg-navy-950 p-6 text-center text-white">'
                   '<div class="grid-paper absolute inset-0 opacity-50"></div><div class="relative">%s'
                   '<p class="mt-3 text-[17px] font-extrabold">Stay Updated!</p>'
                   '<p class="mt-1.5 text-[13px] text-navy-100/80">Get latest exam updates, strategies &amp; free resources.</p>'
                   '<a href="tel:+91%s" class="btn-primary mt-4 w-full">%s Talk to us</a></div></div>'
                   '</div></aside>'
                   % (author_card, toc, ic("download", "h-4 w-4"), latest,
                      ic("cap", "icon-gold mx-auto h-7 w-7"), SITE["phones"][0], ic("phone", "h-4 w-4", True)))

        art = ""
        if p.get("callout"):
            art += ('<div class="flex gap-4 rounded-2xl border border-gold-200 bg-gold-50 p-5 sm:p-6">'
                    '<span class="grid h-11 w-11 shrink-0 place-items-center rounded-xl bg-white ring-1 ring-gold-200">%s</span><span>'
                    '<span class="block text-[16px] font-extrabold text-navy-900">%s</span>'
                    '<span class="mt-1 block text-[14px] leading-relaxed text-navy-800">%s</span></span></div>'
                    % (ic("target", "h-6 w-6 text-gold-600"), p["callout"]["title"], p["callout"]["text"]))
        for para in p.get("intro", []):
            art += '<p class="mt-5 text-[15px] leading-relaxed text-navy-800">%s</p>' % para
        for i, s in enumerate(secs):
            art += ('<div id="%s" class="card mt-5 scroll-mt-28 p-6 sm:p-7"><div class="flex items-center gap-3.5">'
                    '<span class="grid h-10 w-10 shrink-0 place-items-center rounded-full bg-gold-400 font-display text-[16px] font-extrabold text-navy-950">%02d</span>'
                    '<h2 class="text-[20px] font-extrabold leading-snug text-navy-900">%s</h2></div>%s%s</div>'
                    % (s["id"], i + 1, s["title"],
                       ('<p class="mt-4 text-[14.5px] leading-relaxed text-navy-800">%s</p>' % s["lead"]) if s.get("lead") else "",
                       "".join(block_html(b) for b in s["blocks"])))
        if p.get("cta"):
            c = p["cta"]
            chips = ('<ul class="mt-4 flex flex-wrap gap-2">%s</ul>'
                     % "".join('<li class="rounded-lg border border-gold-400/30 bg-gold-400/10 px-2.5 py-1.5 text-[11.5px] font-bold text-gold-200">%s</li>' % x
                               for x in c.get("chips", []))) if c.get("chips") else ""
            art += ('<div class="relative mt-6 overflow-hidden rounded-2xl bg-navy-950 p-7 text-white sm:p-8">'
                    '<div class="grid-paper absolute inset-0 opacity-50"></div>'
                    '<div class="absolute -right-16 -top-16 h-56 w-56 rounded-full bg-gold-500/20 blur-3xl"></div>'
                    '<div class="relative flex flex-col gap-5 sm:flex-row sm:items-center sm:justify-between"><div>'
                    '<span class="inline-block rounded-md bg-gold-400 px-2.5 py-1 text-[10.5px] font-extrabold uppercase tracking-wider text-navy-950">Prepare with Experts</span>'
                    '<p class="mt-3 font-display text-[24px] font-extrabold leading-tight sm:text-[28px]">%s</p>'
                    '<p class="mt-2 max-w-lg text-[14px] text-navy-100/80">%s</p>%s</div>'
                    '<a href="%s" class="btn-primary shrink-0">%s %s</a></div></div>'
                    % (c["title"], c["text"], chips, CTA_MAP.get(c.get("to"), "enroll.html"),
                       c["button"], ic("arrow", "h-4 w-4")))
        if p.get("faqs"):
            art += ('<div class="mt-8"><h2 class="flex items-center gap-2.5 text-[21px] font-extrabold text-navy-900">'
                    '<span class="grid h-7 w-7 place-items-center rounded-full bg-navy-950 text-[13px] font-extrabold text-gold-400">?</span>'
                    'Frequently Asked Questions</h2>%s</div>'
                    % faq_block([(f["q"], f["a"]) for f in p["faqs"]]))
        if others:
            art += ('<div class="mt-9"><div class="flex items-end justify-between">'
                    '<h2 class="text-[21px] font-extrabold text-navy-900">Related Posts</h2>'
                    '<a href="blog.html" class="text-[13px] font-bold text-gold-600 hover:text-gold-700">View All</a></div>'
                    '<div class="mt-4 grid gap-4 sm:grid-cols-3">%s</div></div>'
                    % "".join('<a href="%s" class="card card-hover group p-5">'
                              '<span class="inline-block rounded-md bg-gold-50 px-2 py-1 text-[10.5px] font-extrabold uppercase tracking-wider text-gold-700">%s</span>'
                              '<p class="mt-2.5 text-[15px] font-extrabold leading-snug text-navy-900">%s</p>'
                              '<span class="mt-3 flex items-center gap-1.5 text-[12px] font-bold text-navy-500">%s %s</span></a>'
                              % (post_file(b["slug"]), b["tag"], b.get("titleHighlight") or b["title"],
                                 ic("clock", "h-3.5 w-3.5"), b.get("readTime", "")) for b in others))

        body = ('<section class="bg-cream pb-14 pt-6 lg:pb-16"><div class="container-x">\n'
                '  <nav aria-label="Breadcrumb" class="flex flex-wrap items-center gap-2 text-[12.5px] font-bold text-navy-500">'
                '<a href="index.html" class="hover:text-navy-900">Home</a>%s'
                '<a href="blog.html" class="hover:text-navy-900">Blog</a>%s'
                '<span class="truncate text-navy-900">%s</span></nav>\n'
                '  <div class="relative mt-4 overflow-hidden rounded-2xl bg-navy-950 p-7 text-white sm:p-10">\n'
                '    <div class="grid-paper absolute inset-0 opacity-50"></div>\n'
                '    <div class="absolute -right-24 -top-24 h-[380px] w-[380px] rounded-full bg-gold-500/15 blur-3xl"></div>\n'
                '    <div class="relative max-w-3xl">'
                '<span class="inline-block rounded-md bg-gold-400 px-2.5 py-1 text-[11px] font-extrabold uppercase tracking-wider text-navy-950">%s</span>'
                '<h1 class="mt-4 font-display text-[30px] font-extrabold leading-[1.12] sm:text-[40px]">%s<span class="block text-gold-400">%s</span></h1>'
                '<p class="mt-4 max-w-2xl text-[14.5px] leading-relaxed text-navy-100/85">%s</p>'
                '<div class="mt-6 flex flex-wrap items-center gap-x-5 gap-y-2 text-[12.5px] font-bold text-navy-100/80">'
                '<span class="flex items-center gap-1.5">%s %s</span>'
                '<span class="flex items-center gap-1.5">%s %s</span><span>By %s</span></div>'
                '</div>\n  </div>\n'
                '  <div class="mt-6 grid gap-6 lg:grid-cols-[minmax(0,2fr)_minmax(280px,1fr)]">\n'
                '    <div>%s</div>\n    %s\n  </div>\n</div></section>\n'
                % (ic("chevron", "h-3.5 w-3.5 -rotate-90"), ic("chevron", "h-3.5 w-3.5 -rotate-90"),
                   p.get("titleHighlight") or p["title"], p["tag"], p["title"], p.get("titleHighlight", ""),
                   p["excerpt"], ic("calendar", "icon-gold h-4 w-4"), fmt_date(p["date"]),
                   ic("clock", "icon-gold h-4 w-4"), p.get("readTime", ""), au["name"], art, sidebar))

        page(post_file(p["slug"]),
             "%s %s | GS Net Academy" % (p["title"], p.get("titleHighlight", "")),
             p["excerpt"], body, "blog.html")


if __name__ == "__main__":
    home(); about(); courses(); tutorials(); notes(); contact(); enroll(); blog()
    print("All pages written.")
