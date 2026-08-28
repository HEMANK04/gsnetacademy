/* ===========================================================================
 * GS NET ACADEMY — lead-gate.js
 * ---------------------------------------------------------------------------
 * ONE common script for every "form bharo, phir download/access karo" button
 * on the site — Brochure, Notes PDFs, Tutorial material, anything else you
 * add later. Drop the same <script src="js/lead-gate.js"></script> tag on
 * any page and mark a button like this:
 *
 *   <a href="#"
 *      class="btn-primary gate-btn"
 *      data-gate-title="UGC NET Paper-1 Brochure"
 *      data-gate-type="brochure"
 *      data-gate-file="assets/pdf/brochure.pdf">
 *     Download Brochure
 *   </a>
 *
 * data-gate-file  → the file/page opened AFTER the form is submitted
 * data-gate-type  → "brochure" | "note" | "tutorial" | anything you like
 *                    (saved as formType on the lead so you know which
 *                    button someone clicked)
 * data-gate-title → shown inside the popup ("You're downloading: ...")
 *
 * On submit the form is POSTed to the backend's /api/leads endpoint (MongoDB
 * Atlas), then the file opens in a new tab. If the server is unreachable the
 * download still happens — a visitor is never blocked by a server hiccup.
 * ========================================================================= */

(function () {
  "use strict";

  /* ---- point this at your backend once it's deployed ------------------- */
  /* Example after deploy: "https://api.gsnetacademy.com/api/leads"          */
  /* Left as a relative path so it also works if the API is served from     */
  /* the same domain as the site (e.g. reverse-proxied under /api).         */
  var API_URL = window.GSNET_API_URL || "/api/leads";

  var DONE_KEY = "gsnet_gate_done_v1";
  var already = function () {
    try {
      return localStorage.getItem(DONE_KEY) === "1";
    } catch (e) {
      return false;
    }
  };
  var remember = function () {
    try {
      localStorage.setItem(DONE_KEY, "1");
    } catch (e) {
      /* ignore */
    }
  };

  var overlay = null;

  function openFile(url) {
    if (!url || url === "#") return;
    var a = document.createElement("a");
    a.href = url;
    a.target = "_blank";
    a.rel = "noreferrer noopener";
    document.body.appendChild(a);
    a.click();
    a.remove();
  }

  function closeModal() {
    if (overlay) {
      overlay.remove();
      overlay = null;
      document.body.style.overflow = "";
    }
  }

  function buildModal(btn) {
    var title = btn.getAttribute("data-gate-title") || "Study Material";
    var file = btn.getAttribute("data-gate-file") || "#";
    var type = btn.getAttribute("data-gate-type") || "download";

    overlay = document.createElement("div");
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.className = "gate-overlay";
    overlay.innerHTML =
      '<div class="gate-scrim"></div>' +
      '<div class="gate-panel">' +
      '<button type="button" class="gate-close" aria-label="Close">&times;</button>' +
      '<p class="gate-eyebrow">' +
      escapeHtml(title) +
      "</p>" +
      '<h2 class="gate-title">पहले details भरें, फिर download शुरू होगा</h2>' +
      '<form class="gate-form" novalidate>' +
      '<label class="gate-field"><span>Full Name *</span><input type="text" name="name" required></label>' +
      '<label class="gate-field"><span>Mobile Number *</span><input type="tel" name="phone" required></label>' +
      '<label class="gate-field"><span>WhatsApp Number</span><input type="tel" name="whatsapp"></label>' +
      '<label class="gate-field"><span>Email ID</span><input type="email" name="email"></label>' +
      '<p class="gate-error" hidden></p>' +
      '<button type="submit" class="btn-primary gate-submit">Submit &amp; Download</button>' +
      '<p class="gate-note">आपकी details सिर्फ study material और class updates भेजने के लिए use होंगी।</p>' +
      "</form>" +
      "</div>";

    document.body.appendChild(overlay);
    document.body.style.overflow = "hidden";

    overlay.querySelector(".gate-scrim").addEventListener("click", closeModal);
    overlay.querySelector(".gate-close").addEventListener("click", closeModal);

    var form = overlay.querySelector(".gate-form");
    var errorBox = overlay.querySelector(".gate-error");
    var submitBtn = overlay.querySelector(".gate-submit");

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      errorBox.hidden = true;

      var data = {
        name: form.name.value.trim(),
        phone: form.phone.value.trim(),
        whatsapp: form.whatsapp.value.trim(),
        email: form.email.value.trim(),
      };

      if (data.name.length < 2) return showError("कृपया अपना नाम लिखें");
      if (!/^[0-9]{10}$/.test(data.phone.replace(/\D/g, "").slice(-10)))
        return showError("कृपया valid 10-digit mobile number डालें");

      submitBtn.disabled = true;
      submitBtn.textContent = "Submitting…";

      submitLead({
        ...data,
        formType: type,
        resourceTitle: title,
        source: "website",
        pageUrl: window.location.href,
      })
        .catch(function () {
          /* Never block the download because the server hiccupped. */
        })
        .then(function () {
          remember();
          closeModal();
          openFile(file);
        });
    });

    function showError(msg) {
      errorBox.textContent = msg;
      errorBox.hidden = false;
    }

    form.querySelector('input[name="name"]').focus();
  }

  function submitLead(payload) {
    if (!window.fetch) return Promise.resolve();
    return fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    }).catch(function () {
      /* offline / CORS / server down — swallow, download still proceeds */
    });
  }

  function escapeHtml(s) {
    var d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".gate-btn");
    if (!btn) return;
    e.preventDefault();

    /* Already filled once on this device? Skip straight to the file. */
    if (already()) {
      openFile(btn.getAttribute("data-gate-file") || "#");
      return;
    }
    buildModal(btn);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeModal();
  });
})();
