GS NET ACADEMY — Leads API (Node.js + Express + MongoDB Atlas)
================================================================

This is the ONE backend for every gated download on the static site
(Brochure, Notes PDFs, Tutorial study plan). js/lead-gate.js on the site
posts here whenever someone fills the form.


FOLDER STRUCTURE
----------------
server/
├── index.js                 ← start here (npm start)
├── package.json
├── .env.example             ← copy to .env, fill in your Atlas URI
├── config/db.js             ← MongoDB Atlas connection
├── models/Lead.js           ← what gets saved
├── routes/leadRoutes.js     ← POST /api/leads (public) + GET /api/leads (protected)
├── controllers/leadController.js
└── middleware/
    ├── validation.js        ← server-side validation of every submission
    └── adminAuth.js         ← simple x-api-key guard for GET /api/leads


SETUP
-----
1. cd server
2. npm install
3. cp .env.example .env
4. Open .env and paste your real MongoDB Atlas connection string into
   MONGODB_URI (Atlas → Database → Connect → Drivers → Node.js). Also set
   ALLOWED_ORIGINS to your live site's domain.
5. npm start
   → "✔ MongoDB Atlas connected" and "✔ Leads API running on http://localhost:5000"


CONNECTING THE SITE TO THIS API
--------------------------------
By default js/lead-gate.js posts to the relative path "/api/leads" (works if
you reverse-proxy the API under your site's own domain, e.g. Nginx routing
/api/* to this Node process).

If your API lives on a different domain (e.g. api.gsnetacademy.com), add ONE
line before the lead-gate.js <script> tag on every page:

    <script>window.GSNET_API_URL = "https://api.gsnetacademy.com/api/leads";</script>
    <script src="js/lead-gate.js"></script>

Also make sure that domain is listed in ALLOWED_ORIGINS in .env (CORS).


VIEWING SAVED LEADS
--------------------
GET /api/leads is protected. Set ADMIN_API_KEY in .env to any secret string,
then request:

    curl -H "x-api-key: your-secret-here" https://your-api-domain/api/leads

Without ADMIN_API_KEY set, this route is disabled (404) — safer default.


SECURITY NOTES
--------------
- MongoDB credentials live ONLY in .env (gitignored). Never hard-coded.
- express-rate-limit caps submissions to 30 per IP per 10 minutes.
- middleware/validation.js validates name/phone/email server-side — never
  trust the browser alone.
- The error handler never sends stack traces or driver errors to the client.
- CORS is restricted to ALLOWED_ORIGINS once you set it.


DEPLOYING
---------
Works on any Node host — Render, Railway, a VPS, etc. Just set the same
.env variables there (MONGODB_URI, PORT, ALLOWED_ORIGINS, optionally
ADMIN_API_KEY) and run `npm start`.
