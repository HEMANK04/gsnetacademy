import "dotenv/config";
import express from "express";
import cors from "cors";
import path from "node:path";
import { fileURLToPath } from "node:url";
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