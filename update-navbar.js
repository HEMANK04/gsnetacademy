#!/usr/bin/env node
/**
 * update-navbar.js
 * -----------------
 * Puri site ke saare .html files me galat navbar dhoondh kar
 * use SAHI navbar se replace karta hai — ek sath, ek hi script se.
 *
 * SETUP (1 baar):
 *   1) "navbar-correct.html" file isi folder me rakho, jisme aapka
 *      SAHI navbar ka poora HTML code ho (ye file already di gayi hai).
 *   2) Neeche CONFIG.rootDir me apna project folder ka path daalo
 *      (jaha aapke saare .html files hain — index.html, about.html, etc).
 *
 * RUN:
 *      node update-navbar.js
 *
 * Kya hoga:
 *   - Har .html file me purana navbar block dhoondega
 *     (<input id="nav-toggle"> se lekar "Call 9266511505" button tak).
 *   - Use navbar-correct.html ke content se replace kar dega.
 *   - Replace karne se pehle har file ka ".bak" backup bana dega
 *     (kuch galat ho jaye to wapas restore kar sakte ho).
 */

const fs = require('fs');
const path = require('path');

const CONFIG = {
  rootDir: path.resolve(__dirname),                         // <-- apna project folder path yaha daalo
  navbarFile: path.resolve(__dirname, 'navbar-correct.html'), // sahi navbar wali file
  extensions: ['.html', '.htm'],
  makeBackup: true,
};

// Navbar block hamesha isi input se start hota hai...
const START_MARKER = /<input\s+type="checkbox"\s+id="nav-toggle"[^>]*>/;
// ...aur "Call 9266511505" button ke baad 4 closing </div> tags par khatam hota hai.
const END_MARKER = /Call 9266511505<\/a>\s*<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/;

function getAllHtmlFiles(dir, exts, fileList = []) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === 'node_modules' || entry.name.startsWith('.')) continue;
      getAllHtmlFiles(fullPath, exts, fileList);
    } else if (exts.includes(path.extname(entry.name).toLowerCase())) {
      fileList.push(fullPath);
    }
  }
  return fileList;
}

function findNavbarRange(content) {
  const startMatch = content.match(START_MARKER);
  if (!startMatch) return null;
  const startIndex = startMatch.index;

  const afterStart = content.slice(startIndex);
  const endMatch = afterStart.match(END_MARKER);
  if (!endMatch) return null;

  const endIndex = startIndex + endMatch.index + endMatch[0].length;
  return { startIndex, endIndex };
}

function main() {
  if (!fs.existsSync(CONFIG.navbarFile)) {
    console.error(`❌ navbar-correct.html nahi mili: ${CONFIG.navbarFile}`);
    console.error('   Pehle sahi navbar wali file isi naam se banao.');
    process.exit(1);
  }

  const correctNavbar = fs.readFileSync(CONFIG.navbarFile, 'utf8').trim();
  const htmlFiles = getAllHtmlFiles(CONFIG.rootDir, CONFIG.extensions)
    .filter((f) => path.resolve(f) !== path.resolve(CONFIG.navbarFile));

  if (htmlFiles.length === 0) {
    console.log('⚠️  Koi .html file nahi mili.');
    return;
  }

  let updated = 0;
  let alreadyOk = 0;
  let skipped = 0;

  for (const file of htmlFiles) {
    const content = fs.readFileSync(file, 'utf8');
    const range = findNavbarRange(content);

    if (!range) {
      console.log(`⏭  Navbar nahi mila (skip):  ${file}`);
      skipped++;
      continue;
    }

    const before = content.slice(0, range.startIndex);
    const after = content.slice(range.endIndex);
    const newContent = before + correctNavbar + after;

    if (newContent === content) {
      console.log(`✅ Already sahi hai:          ${file}`);
      alreadyOk++;
      continue;
    }

    if (CONFIG.makeBackup) {
      fs.writeFileSync(file + '.bak', content, 'utf8');
    }

    fs.writeFileSync(file, newContent, 'utf8');
    console.log(`✔  Navbar update ho gaya:     ${file}`);
    updated++;
  }

  console.log('\n--------------------------------------');
  console.log(`Total files scanned : ${htmlFiles.length}`);
  console.log(`Updated             : ${updated}`);
  console.log(`Already correct     : ${alreadyOk}`);
  console.log(`Skipped (no match)  : ${skipped}`);
  console.log('--------------------------------------');
}

main();
