import { Router } from "express";
import rateLimit from "express-rate-limit";
import { validateLead } from "../middleware/validation.js";
import { requireAdminKey } from "../middleware/adminAuth.js";
import { createLead, listLeads } from "../controllers/leadController.js";

const router = Router();

// Basic anti-spam limit on the public submit endpoint.
const submitLimiter = rateLimit({
  windowMs: 10 * 60 * 1000, // 10 minutes
  max: 30, // 30 submissions per IP per window
  standardHeaders: true,
  legacyHeaders: false,
});

// POST /api/leads — called by js/lead-gate.js on every site page
router.post("/", submitLimiter, validateLead, createLead);

// GET /api/leads — protected, for you to pull the list (see adminAuth.js)
router.get("/", requireAdminKey, listLeads);

export default router;
