/** Basic server-side validation for a lead submission. Never trust the client alone. */
export function validateLead(req, res, next) {
  const body = req.body || {};
  const name = String(body.name || "").trim();
  const phone = String(body.phone || "").trim();
  const email = String(body.email || "").trim();

  if (name.length < 2 || name.length > 100) {
    return res.status(400).json({ ok: false, error: "Please enter a valid name" });
  }
  const phoneDigits = phone.replace(/\D/g, "").slice(-10);
  if (!/^[0-9]{10}$/.test(phoneDigits)) {
    return res.status(400).json({ ok: false, error: "Please enter a valid 10-digit mobile number" });
  }
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return res.status(400).json({ ok: false, error: "Please enter a valid email" });
  }

  // Normalise + drop anything not in the schema (basic injection hardening —
  // Mongoose strict mode already ignores unknown fields, this is belt & braces).
  req.body = {
    name,
    phone: phoneDigits,
    whatsapp: String(body.whatsapp || "").replace(/\D/g, "").slice(-10),
    email: email.toLowerCase(),
    course: String(body.course || "").slice(0, 200),
    resourceTitle: String(body.resourceTitle || "").slice(0, 200),
    formType: String(body.formType || "download").slice(0, 40),
    pageUrl: String(body.pageUrl || "").slice(0, 500),
    source: String(body.source || "website").slice(0, 60),
    message: String(body.message || "").slice(0, 1000),
  };

  next();
}
