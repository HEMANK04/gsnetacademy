/*
===========================================================================
 * GS NET ACADEMY — lead-gate.js  (v3)
 * ---------------------------------------------------------------------------
 * ONE common script for every "form bharo, phir download/access karo" button
 * — Brochure, Notes PDFs, Tutorial modules, kuch bhi.
 *
 * v3 me kya naya:
 *   - Pehli baar form bharne par pura data (name/phone/whatsapp/email +
 *     consent) localStorage me save hota hai (sirf "done" flag nahi).
 *   - Agle kisi bhi gate-btn click par form dobara NAHI dikhta — seedha
 *     file open ho jaati hai — but saved data DB ko silently phir bhej diya
 *     jaata hai (resourceTitle/type ke saath) taaki server par bhi latest
 *     record/click history rahe.
 *   - Agar kabhi localStorage clear ho jaaye ya corrupt ho, form phir se
 *     dikh jaata hai (graceful fallback).
 * ========================================================================= */

(function () {
  "use strict";

  var API_URL = window.GSNET_API_URL || "/api/leads";
  var POLICY_TERMS = "terms-of-enrollment.html";
  var POLICY_PRIVACY = "privacy-policy.html";
  var POLICY_REFUND = "refund-policy.html";

  var LEAD_KEY = "gsnet_lead_v3"; // stores the actual submitted lead object
  var overlay = null;
  var lastFocused = null;

  var CSS = [
    ".gate-overlay{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;padding:16px}",
    ".gate-scrim{position:absolute;inset:0;background:rgba(8,17,33,.72);backdrop-filter:blur(3px)}",
    ".gate-panel{position:relative;width:100%;max-width:440px;max-height:92vh;overflow-y:auto;",
    "background:#fff;border-radius:20px;padding:26px 22px 22px;box-shadow:0 24px 60px rgba(8,17,33,.35);",
    "font-family:inherit;-webkit-overflow-scrolling:touch}",
    ".gate-close{position:absolute;top:10px;right:12px;border:0;background:transparent;font-size:28px;",
    "line-height:1;color:#64748b;cursor:pointer;padding:4px 8px;border-radius:8px}",
    ".gate-close:hover{background:#f1f5f9;color:#0f172a}",
    ".gate-eyebrow{margin:0;font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#B8860B}",
    ".gate-title{margin:8px 0 18px;font-size:19px;line-height:1.35;font-weight:800;color:#0B1B34}",
    ".gate-field{display:block;margin-bottom:12px}",
    ".gate-field>span{display:block;margin-bottom:5px;font-size:12.5px;font-weight:700;color:#334155}",
    ".gate-field input{width:100%;box-sizing:border-box;border:1px solid #cbd5e1;border-radius:10px;",
    "padding:11px 12px;font-size:15px;color:#0f172a;background:#fff;outline:none;transition:border-color .15s,box-shadow .15s}",
    ".gate-field input:focus{border-color:#F5C518;box-shadow:0 0 0 3px rgba(245,197,24,.25)}",
    ".gate-check{display:flex;gap:10px;align-items:flex-start;margin:10px 0;font-size:12.5px;line-height:1.5;color:#334155}",
    ".gate-check input{margin:2px 0 0;width:17px;height:17px;flex:0 0 auto;accent-color:#0B1B34;cursor:pointer}",
    ".gate-check a{color:#0B1B34;font-weight:700;text-decoration:underline}",
    ".gate-check a:hover{color:#B8860B}",
    ".gate-error{margin:8px 0 0;padding:9px 11px;border-radius:9px;background:#fee2e2;color:#991b1b;",
    "font-size:12.5px;font-weight:700}",
    ".gate-submit{width:100%;margin-top:14px;border:0;border-radius:12px;background:#F5C518;color:#0B1B34;",
    "font-size:15px;font-weight:800;padding:13px 16px;cursor:pointer;transition:filter .15s}",
    ".gate-submit:hover{filter:brightness(.95)}",
    ".gate-submit:disabled{opacity:.6;cursor:not-allowed}",
    ".gate-note{margin:12px 0 0;font-size:11.5px;line-height:1.55;color:#64748b}",
    "@media (max-width:420px){.gate-panel{padding:22px 16px 18px;border-radius:16px}.gate-title{font-size:17px}}"
  ].join("");

  function injectStyles() {
    if (document.getElementById("gate-styles")) return;
    var s = document.createElement("style");
    s.id = "gate-styles";
    s.appendChild(document.createTextNode(CSS));
    (document.head || document.documentElement).appendChild(s);
  }

  /* ------------------------------------------------------------------ *
   *  localStorage helpers
   * ------------------------------------------------------------------ */
  function getSavedLead() {
    try {
      var raw = localStorage.getItem(LEAD_KEY);
      if (!raw) return null;
      var obj = JSON.parse(raw);
      if (obj && obj.name && obj.phone) return obj;
      return null;
    } catch (e) { return null; }
  }
  function saveLead(obj) {
    try { localStorage.setItem(LEAD_KEY, JSON.stringify(obj)); } catch (e) { /* ignore */ }
  }

  function escapeHtml(s) {
    var d = document.createElement("div");
    d.textContent = s == null ? "" : String(s);
    return d.innerHTML;
  }
//   function openFile(url, filename) {
//   if (!url || url === "#") return;
//   var a = document.createElement("a");
//   a.href = url;
//   a.download = filename || "";   // ★ download force, custom naam optional
//   a.rel = "noreferrer noopener";
//   document.body.appendChild(a);
//   a.click();
//   a.remove();
// }

function openFile(url, filename) {
  if (!url || url === "#") return;

  var link = document.createElement("a");

  link.href = url;
  link.download = filename || "UGC-NET-Brochure.pdf";

  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
  function closeModal() {
    if (!overlay) return;
    overlay.remove();
    overlay = null;
    document.body.style.overflow = "";
    if (lastFocused && lastFocused.focus) lastFocused.focus();
  }

  /* ------------------------------------------------------------------ *
   *  Modal
   * ------------------------------------------------------------------ */
  function buildModal(btn) {
    injectStyles();
    lastFocused = document.activeElement;

    var title = btn.getAttribute("data-gate-title") || "Study Material";
    var file = btn.getAttribute("data-gate-file") || "#";
    var type = btn.getAttribute("data-gate-type") || "download";

    overlay = document.createElement("div");
    overlay.className = "gate-overlay";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", title + " — details form");

    overlay.innerHTML =
      '<div class="gate-scrim"></div>' +
      '<div class="gate-panel">' +
        '<button type="button" class="gate-close" aria-label="Close">&times;</button>' +
        '<p class="gate-eyebrow">' + escapeHtml(title) + "</p>" +
        '<h2 class="gate-title">पहले details भरें, फिर access खुलेगा</h2>' +
        '<form class="gate-form" novalidate>' +
          '<label class="gate-field"><span>Full Name *</span>' +
            '<input type="text" name="name" autocomplete="name" required></label>' +
          '<label class="gate-field"><span>Mobile Number *</span>' +
            '<input type="tel" name="phone" inputmode="numeric" autocomplete="tel" required></label>' +
          '<label class="gate-field"><span>WhatsApp Number</span>' +
            '<input type="tel" name="whatsapp" inputmode="numeric"></label>' +
          '<label class="gate-field"><span>Email ID</span>' +
            '<input type="email" name="email" autocomplete="email"></label>' +

          '<label class="gate-check">' +
            '<input type="checkbox" name="consentPolicies" required>' +
            '<span>मैंने <a href="' + POLICY_TERMS + '" target="_blank" rel="noreferrer noopener">Terms of Enrollment</a>, ' +
            '<a href="' + POLICY_PRIVACY + '" target="_blank" rel="noreferrer noopener">Privacy Policy</a> और ' +
            '<a href="' + POLICY_REFUND + '" target="_blank" rel="noreferrer noopener">Refund &amp; Cancellation Policy</a> ' +
            'पढ़ ली हैं और मैं इनसे सहमत हूँ। *</span>' +
          "</label>" +

          '<label class="gate-check">' +
            '<input type="checkbox" name="consentMarketing" checked>' +
            "<span>मैं GS Net Academy से course, class और academic updates WhatsApp / email पर पाना चाहता/चाहती हूँ।</span>" +
          "</label>" +

          '<p class="gate-error" hidden role="alert"></p>' +
          '<button type="submit" class="gate-submit">Submit &amp; Continue</button>' +
          '<p class="gate-note">आपकी details सिर्फ study material और class updates भेजने के लिए use होंगी। ' +
          'ये form सिर्फ एक बार भरना है — अगली बार सीधे content खुलेगा।</p>' +
        "</form>" +
      "</div>";

    document.body.appendChild(overlay);
    document.body.style.overflow = "hidden";

    overlay.querySelector(".gate-scrim").addEventListener("click", closeModal);
    overlay.querySelector(".gate-close").addEventListener("click", closeModal);

    var form = overlay.querySelector(".gate-form");
    var errorBox = overlay.querySelector(".gate-error");
    var submitBtn = overlay.querySelector(".gate-submit");

    function showError(msg) {
      errorBox.textContent = msg;
      errorBox.hidden = false;
      return false;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      errorBox.hidden = true;

      var name = form.name.value.trim();
      var phone = form.phone.value.trim();
      var digits = phone.replace(/\D/g, "");

      if (name.length < 2) return showError("कृपया अपना नाम लिखें।");
      if (digits.length < 10) return showError("कृपया valid 10-digit mobile number डालें।");
      if (!form.consentPolicies.checked) {
        return showError("आगे बढ़ने के लिए Terms, Privacy और Refund Policy accept करना ज़रूरी है।");
      }

      submitBtn.disabled = true;
      submitBtn.textContent = "Submitting…";

      var leadData = {
        name: name,
        phone: phone,
        whatsapp: form.whatsapp.value.trim(),
        email: form.email.value.trim(),
        consentPolicies: true,
        consentMarketing: !!form.consentMarketing.checked,
        consentAt: new Date().toISOString()
      };

      // sendToServer(leadData, type, title)["catch"](function () {
      //   /* server down ho to bhi content khulna chahiye */
      // }).then(function () {
      //   saveLead(leadData);   // ★ ab agli baar form nahi dikhega
      //   closeModal();
      //   openFile(file);
      // });

      sendToServer(leadData, type, title)["catch"](function () {
  // Lead API fail ho tab bhi PDF download hogi
}).then(function () {

  saveLead(leadData);

  closeModal();

  var filename = file.split("/").pop();

  openFile(file, filename);
});
    });

    overlay.addEventListener("keydown", function (e) {
      if (e.key !== "Tab") return;
      var f = overlay.querySelectorAll('button, input, a[href], [tabindex]:not([tabindex="-1"])');
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    form.querySelector('input[name="name"]').focus();
  }

  /* ------------------------------------------------------------------ *
   *  Backend
   * ------------------------------------------------------------------ */
  function sendToServer(leadData, formType, resourceTitle) {
    if (!window.fetch) return Promise.resolve();
    var payload = {};
    for (var k in leadData) payload[k] = leadData[k];
    payload.formType = formType;
    payload.resourceTitle = resourceTitle;
    payload.source = "website";
    payload.pageUrl = window.location.href;
    payload.referrer = document.referrer || "";
    return fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    })["catch"](function () { /* offline / CORS / server down */ });
  }

  /* ------------------------------------------------------------------ *
   *  Wiring
   * ------------------------------------------------------------------ */
//   document.addEventListener("click", function (e) {
//     var t = e.target;
//     var btn = t && t.closest ? t.closest(".gate-btn") : null;
//     if (!btn) return;
//     e.preventDefault();

//     var saved = getSavedLead();
//     var file = btn.getAttribute("data-gate-file") || "#";

//     if (saved) {
//       // pehle se details bhari hui hain — form dobara mat dikhao,
//       // seedha file kholo, aur DB ko is naye click ka bhi record bhej do.
//       sendToServer(saved, btn.getAttribute("data-gate-type") || "download", btn.getAttribute("data-gate-title") || "Study Material");
//       openFile(file);
//       return;
//     }
//     buildModal(btn);
//   });

//   document.addEventListener("keydown", function (e) {
//     if (e.key === "Escape") closeModal();
//   });
document.addEventListener("click", function (e) {
  var t = e.target;
  var btn = t && t.closest ? t.closest(".gate-btn") : null;

  if (!btn) return;

  e.preventDefault();

  // Download Brochure button click hone par
  // hamesha form/modal open hoga
  buildModal(btn);
});

 })();
