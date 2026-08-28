import mongoose from "mongoose";

/**
 * Connects to MongoDB Atlas using MONGODB_URI from .env.
 * The URI (with the real username/password) is never hard-coded here —
 * it only ever lives in .env, which is gitignored.
 */
export async function connectDB() {
  const uri = process.env.MONGODB_URI;
  if (!uri) {
    console.error("\n✖ MONGODB_URI is missing. Copy .env.example to .env and fill it in.\n");
    process.exit(1);
  }

  mongoose.set("strictQuery", true);

  try {
    await mongoose.connect(uri);
    console.log("✔ MongoDB Atlas connected —", mongoose.connection.name);
  } catch (err) {
    console.error("✖ MongoDB connection failed:", err.message);
    process.exit(1);
  }
}
