import { Lead } from "../models/Lead.js";

export async function createLead(req, res) {
  try {
    const referer = req.get("referer") || "";
    const lead = await Lead.create({
      ...req.body,
      pageUrl: req.body.pageUrl || referer,
    });
    res.status(201).json({ ok: true, id: lead._id });
  } catch (err) {
    // Never leak internals (stack traces, driver errors) to the client.
    console.error("Lead save failed:", err.message);
    res.status(500).json({ ok: false, error: "Could not save right now. Please try again." });
  }
}

export async function listLeads(req, res) {
  const page = Math.max(1, parseInt(req.query.page, 10) || 1);
  const limit = Math.min(100, parseInt(req.query.limit, 10) || 50);

  const [items, total] = await Promise.all([
    Lead.find()
      .sort({ createdAt: -1 })
      .skip((page - 1) * limit)
      .limit(limit)
      .lean(),
    Lead.countDocuments(),
  ]);

  res.json({ ok: true, page, limit, total, items });
}
