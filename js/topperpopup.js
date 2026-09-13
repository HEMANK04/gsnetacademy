/* ============================================================
   GS Net Academy — Poster Popup (Poster + 2 Buttons)
   ------------------------------------------------------------
   Kaise use karein:
   1) Ye file site ke  js/  folder me rakh dein.
   2) index.html me </body> se theek pehle ye line add karein:

        <script src="js/topper-popup.js"></script>

   3) Poster image yahan rakhein:
        assets/results/toppers/top1_Bheru_Dan.jpeg

   Naya poster aane par sirf niche wale POPUP object ko badal dein.
   ============================================================ */
(function () {
  "use strict";

  /* ---------- YAHAN DATA BADLEIN ---------- */
  var POPUP = {
    poster:   "assets/results/toppers/top1_Bheru_Dan.jpeg",
    joinUrl:  "enroll.html",      // JRF @ ₹500 page
    readMore: "bherudan.html",    // Read More page
    delayMs:  1200                // popup kitni der baad khule
  };
  /* ---------------------------------------- */

  if (window.__gsTopperPopup) return; 
  window.__gsTopperPopup = true;

  var CSS = ''
  + '.gs-pop{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;padding:16px;opacity:0;visibility:hidden;transition:opacity .28s ease,visibility .28s ease}'
  + '.gs-pop.is-open{opacity:1;visibility:visible}'
  + '.gs-pop__scrim{position:absolute;inset:0;background:rgba(6,15,30,.85);backdrop-filter:blur(4px)}'
  + '.gs-pop__box{position:relative;width:100%;max-width:500px;max-height:calc(100vh - 32px);overflow-y:auto;border-radius:16px;background:#0B1B34;'
  +   'box-shadow:0 24px 60px rgba(0,0,0,.5);transform:translateY(14px) scale(.97);transition:transform .3s cubic-bezier(.2,.8,.3,1);'
  +   '-webkit-overflow-scrolling:touch;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;display:flex;flex-direction:column;'
  +   'scrollbar-width:none;-ms-overflow-style:none}'
  + '.gs-pop__box::-webkit-scrollbar{display:none}'
  + '.gs-pop.is-open .gs-pop__box{transform:translateY(0) scale(1)}'
  + '.gs-pop__x{position:absolute;top:12px;right:12px;z-index:10;width:32px;height:32px;display:flex;align-items:center;justify-content:center;border:0;border-radius:50%;'
  +   'background:rgba(255, 0, 0, 0.79);color:#fff;font-size:28px;line-height:1;cursor:pointer;transition:background .2s,transform .2s;backdrop-filter:blur(4px)}'
  + '.gs-pop__x:hover{background:rgba(0,0,0,.75);transform:scale(1.05)}'
  + '.gs-pop__poster{width:100%;height:auto;display:block;border-radius:16px 16px 0 0}'
  + '.gs-pop__footer{padding:16px 24px 24px;background:#0B1B34;border-radius:0 0 16px 16px}'
  + '.gs-pop__btns{display:grid;gap:10px}'
  + '.gs-pop__btn{display:flex;align-items:center;justify-content:center;gap:7px;border-radius:12px;padding:14px 16px;'
  +   'font-size:16px;font-weight:800;text-decoration:none;transition:transform .15s ease,filter .2s ease;text-align:center}'
  + '.gs-pop__btn:active{transform:translateY(1px)}'
  + '.gs-pop__btn--gold{background:#F5C518;color:#0B1B34}'
  + '.gs-pop__btn--gold:hover{filter:brightness(1.08)}'
  + '.gs-pop__btn--ghost{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.32)}'
  + '.gs-pop__btn--ghost:hover{background:rgba(255,255,255,.1)}'
  + '@media(max-width:380px){.gs-pop__btn{font-size:14px;padding:13px 14px}}'
  + '@media(prefers-reduced-motion:reduce){.gs-pop,.gs-pop__box{transition:none}}';

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function build() {
    var style = document.createElement("style");
    style.textContent = CSS;
    document.head.appendChild(style);

    var wrap = document.createElement("div");
    wrap.className = "gs-pop";
    wrap.setAttribute("role", "dialog");
    wrap.setAttribute("aria-modal", "true");
    wrap.setAttribute("aria-label", "Special Announcement");
    wrap.innerHTML =
      '<div class="gs-pop__scrim" data-close></div>' +
      '<div class="gs-pop__box">' +
        '<button class="gs-pop__x" type="button" data-close aria-label="Close">&times;</button>' +
        '<img class="gs-pop__poster" src="' + esc(POPUP.poster) + '" alt="Rank 1 Poster">' +
        '<div class="gs-pop__footer">' +
          '<div class="gs-pop__btns">' +
            '<a class="gs-pop__btn gs-pop__btn--gold" href="' + esc(POPUP.joinUrl) + '">JRF @ &#8377;500 &mdash; Join Now</a>' +
            '<a class="gs-pop__btn gs-pop__btn--ghost" href="' + esc(POPUP.readMore) + '">Read More &rarr;</a>' +
          '</div>' +
        '</div>' +
      '</div>';

    document.body.appendChild(wrap);

    function close() {
      wrap.classList.remove("is-open");
      document.documentElement.style.overflow = "";
      document.removeEventListener("keydown", onKey);
    }
    function onKey(e) { if (e.key === "Escape") close(); }

    wrap.addEventListener("click", function (e) {
      if (e.target.closest("[data-close]")) { e.preventDefault(); close(); }
    });

    setTimeout(function () {
      wrap.classList.add("is-open");
      document.documentElement.style.overflow = "hidden";
      document.addEventListener("keydown", onKey);
      var x = wrap.querySelector(".gs-pop__x");
      if (x) x.focus();
    }, POPUP.delayMs);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", build);
  } else {
    build();
  }
})();