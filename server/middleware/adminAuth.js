/**
 * Very small guard for the "view saved leads" endpoint. Set ADMIN_API_KEY in
 * .env, then call GET /api/leads with header:  x-api-key: <that value>
 * If ADMIN_API_KEY is not set, the route is disabled entirely (safer default).
 */
export function requireAdminKey(req, res, next) {
  const expected = process.env.ADMIN_API_KEY;
  if (!expected) {
    return res.status(404).json({ ok: false, error: "Not available" });
  }
  const given = req.get("x-api-key");
  if (given !== expected) {
    return res.status(401).json({ ok: false, error: "Unauthorized" });
  }
  next();
}
