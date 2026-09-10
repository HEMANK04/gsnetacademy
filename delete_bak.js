#!/usr/bin/env node
/**
 * delete_bak.js
 * --------------
 * Project folder ke andar (sub-folders sameet) sabhi *.bak files
 * dhoondh kar delete kar deta hai — jo replace_header.js/py ne banayi thi.
 *
 * USAGE:
 *   node delete_bak.js <project_folder>
 *
 * Example:
 *   node delete_bak.js .
 *
 * Safety:
 *   - Pehle sirf list karta hai ki kaunsi .bak files milin.
 *   - --yes / -y flag ke bina sirf DRY RUN karega (kuch delete nahi karega),
 *     sirf dikhayega ki kya delete hoga.
 *   - Delete pakka karne ke liye:  node delete_bak.js . --yes
 */

const fs = require("fs");
const path = require("path");

function findBakFiles(dir) {
  let results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results = results.concat(findBakFiles(fullPath));
    } else if (entry.isFile() && fullPath.toLowerCase().endsWith(".bak")) {
      results.push(fullPath);
    }
  }

  return results;
}

function main() {
  const args = process.argv.slice(2);
  const projectDir = args[0];
  const confirm = args.includes("--yes") || args.includes("-y");

  if (!projectDir) {
    console.log("Usage: node delete_bak.js <project_folder> [--yes]");
    process.exit(1);
  }

  if (!fs.existsSync(projectDir) || !fs.statSync(projectDir).isDirectory()) {
    console.log(`Error: '${projectDir}' ek folder nahi hai.`);
    process.exit(1);
  }

  const bakFiles = findBakFiles(projectDir).sort();

  if (bakFiles.length === 0) {
    console.log("Koi .bak file nahi mili.");
    process.exit(0);
  }

  console.log(`${bakFiles.length} .bak file(s) mili:\n`);
  bakFiles.forEach((f) => console.log(`  ${f}`));

  if (!confirm) {
    console.log(
      "\n(Ye DRY RUN tha — kuch delete nahi hua.)\nPakka delete karne ke liye ye chalao:\n" +
        `  node delete_bak.js ${projectDir} --yes`
    );
    return;
  }

  console.log("\nDeleting...\n");
  for (const f of bakFiles) {
    fs.unlinkSync(f);
    console.log(`  Deleted: ${f}`);
  }

  console.log(`\nDone. ${bakFiles.length} .bak file(s) delete ho gayi.`);
}

main();
