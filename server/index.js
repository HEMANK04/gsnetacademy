import "dotenv/config";
import express from "express";
import cors from "cors";
import path from "node:path";
import { fileURLToPath } from "node:url";
import fs from "node:fs";
import { connectDB } from "./config/db.js";
import leadRoutes from "./routes/leadRoutes.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PORT = process.env.PORT || 5000;
const PUBLIC_DIR = path.join(__dirname, "public");

const allowedOrigins = (process.env.ALLOWED_ORIGINS || "")
  .split(",")
  .map((s) => s.trim())
  .filter(Boolean);

const app = express();

// nginx ke peeche chal rahe hain — asli client IP X-Forwarded-For se lo.
// express-rate-limit ke liye ye zaroori hai, warna sabka IP 127.0.0.1 dikhega.
app.set("trust proxy", 1);

app.use(
  cors({
    origin: allowedOrigins.length ? allowedOrigins : true,
    credentials: false,
  })
);
app.use(express.json({ limit: "100kb" }));

/* ------------------------------------------------------------------ *
 * API routes — static se PEHLE
 * ------------------------------------------------------------------ */

app.get("/api", (_req, res) => {
  res.json({ ok: true, service: "gsnet-static-leads-api" });
});

app.get("/api/health", (_req, res) => res.json({ ok: true }));

app.use("/api/leads", leadRoutes);

/* ------------------------------------------------------------------ *
 * Tutorial pages ke andar JS pushState() se fake sub-routes banti hain
 * (jaise /tutorials/.../topic-slug/practice-questions). In URLs par
 * directly reload/navigate karne par asli file nahi milti (404 aata),
 * kyunki actual HTML file root pe hi hai, alag naam/case ke saath.
 * Ye middleware us case ko handle karta hai: agar exact path na mile,
 * to ek-ek segment hata ke dekhta hai ki koi matching .html file
 * (case-insensitive) milti hai kya, aur wahi serve kar deta hai.
 * ------------------------------------------------------------------ */

// Startup par saari .html files ka case-insensitive index bana lo
const htmlIndex = new Map(); // lowercase-relative-path (no .html) -> actual relative path
(function buildHtmlIndex(dir, base = "") {
  if (!fs.existsSync(dir)) return; // prevent crash if public dir isn't fully ready
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const rel = base ? `${base}/${entry.name}` : entry.name;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      buildHtmlIndex(full, rel);
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith(".html")) {
      const withoutExt = rel.slice(0, -5); // remove ".html"
      htmlIndex.set(withoutExt.toLowerCase(), rel);
    }
  }
})(PUBLIC_DIR);

app.use((req, res, next) => {
  if (req.method !== "GET") return next();

  const decodedPath = decodeURIComponent(req.path).replace(/\/+$/, "");
  const segments = decodedPath.split("/").filter(Boolean);

  // Ek-ek segment hata ke check karo (max 3 levels tak, taaki loop na ho)
  for (let cut = 1; cut <= 3 && segments.length - cut >= 1; cut++) {
    const candidate = segments.slice(0, segments.length - cut).join("/").toLowerCase();
    const match = htmlIndex.get(candidate);
    if (match) {
      return res.sendFile(path.join(PUBLIC_DIR, match));
    }
  }

  next();
});

/* ------------------------------------------------------------------ *
 * Static site — index.html, about.html, unit-1.html, css/, js/, assets/
 * ------------------------------------------------------------------ */

app.use(
  express.static(PUBLIC_DIR, {
    extensions: ["html"], // /about  ->  about.html
    maxAge: "1h",
  })
);

// Kuch bhi match na ho to 404
app.use((_req, res) => {
  res.status(404).sendFile(path.join(PUBLIC_DIR, "404.html"), (err) => {
    if (err) res.status(404).json({ ok: false, error: "Not found" });
  });
});

/* ------------------------------------------------------------------ *
 * Error handler — hamesha sabse aakhir me
 * ------------------------------------------------------------------ */

app.use((err, _req, res, _next) => {
  console.error(err);
  res.status(500).json({ ok: false, error: "Something went wrong" });
});

/* ------------------------------------------------------------------ *
 * Start — Mongo fail ho to bhi static site chalti rahe
 * ------------------------------------------------------------------ */

connectDB()
  .then(() => console.log("✔ MongoDB connected"))
  .catch((err) => console.error("✖ MongoDB connection failed:", err.message));

app.listen(PORT, () => console.log(`✔ GS Net Academy running on port ${PORT}`));