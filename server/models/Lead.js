import mongoose from "mongoose";

const { Schema, model } = mongoose;

/**
 * Every gated download on the site (Brochure, Notes PDFs, Tutorial study
 * plan — anything using js/lead-gate.js) saves one of these.
 */
const LeadSchema = new Schema(
  {
    name: { type: String, required: true, trim: true },
    phone: { type: String, required: true, trim: true },
    whatsapp: { type: String, default: "", trim: true },
    email: { type: String, default: "", lowercase: true, trim: true },
    course: { type: String, default: "" },
    resourceTitle: { type: String, default: "" }, // e.g. "Unit 3: Comprehension (PDF Notes)"
    formType: { type: String, default: "download" }, // "brochure" | "note" | "tutorial" | "enroll" | "contact"
    pageUrl: { type: String, default: "" }, // page the button was clicked on
    source: { type: String, default: "website" },
    message: { type: String, default: "" },
  },
  { timestamps: true }
);

export const Lead = model("Lead", LeadSchema);
