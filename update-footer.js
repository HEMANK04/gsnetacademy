#!/usr/bin/env node
/**
 * update-footer.js
 * -----------------
 * Puri site ke saare .html files me galat footer dhoondh kar
 * use SAHI footer se replace karta hai — ek sath, ek hi script se.
 *
 * SETUP (1 baar):
 *   1) "footer-correct.html" file isi folder me rakho, jisme aapka
 *      SAHI footer ka poora HTML code ho (ye file already di gayi hai).
 *   2) Neeche CONFIG.rootDir me apna project folder ka path daalo
 *      (jaha aapke saare .html files hain — index.html, about.html, etc,
 *       subfolders ke andar wali files bhi apne aap mil jayengi).
 *
 * RUN:
 *      node update-footer.js
 *
 * Kya hoga:
 *   - Har .html file me purana <footer>...</footer> block dhoondega.
 *   - Use footer-correct.html ke content se replace kar dega.
 *   - Replace karne se pehle har file ka ".bak" backup bana dega
 *     (kuch galat ho jaye to wapas restore kar sakte ho).
 */

const fs = require('fs');
const path = require('path');

const CONFIG = {
  rootDir: path.resolve(__dirname),                          // <-- apna project folder path yaha daalo
  footerFile: path.resolve(__dirname, 'footer-correct.html'), // sahi footer wali file
  extensions: ['.html', '.htm'],
  makeBackup: true,
};

// <footer ...> se lekar matching </footer> tak (case-insensitive, non-greedy)
const FOOTER_REGEX = /<footer\b[^>]*>[\s\S]*?<\/footer\s*>/i;

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

function main() {
  if (!fs.existsSync(CONFIG.footerFile)) {
    console.error(`❌ footer-correct.html nahi mili: ${CONFIG.footerFile}`);
    console.error('   Pehle sahi footer wali file isi naam se banao.');
    process.exit(1);
  }

  const correctFooter = fs.readFileSync(CONFIG.footerFile, 'utf8').trim();
  const htmlFiles = getAllHtmlFiles(CONFIG.rootDir, CONFIG.extensions)
    .filter((f) => path.resolve(f) !== path.resolve(CONFIG.footerFile));

  if (htmlFiles.length === 0) {
    console.log('⚠️  Koi .html file nahi mili.');
    return;
  }

  let updated = 0;
  let alreadyOk = 0;
  let skipped = 0;

  for (const file of htmlFiles) {
    const content = fs.readFileSync(file, 'utf8');

    if (!FOOTER_REGEX.test(content)) {
      console.log(`⏭  Footer nahi mila (skip):  ${file}`);
      skipped++;
      continue;
    }

    const newContent = content.replace(FOOTER_REGEX, correctFooter);

    if (newContent === content) {
      console.log(`✅ Already sahi hai:          ${file}`);
      alreadyOk++;
      continue;
    }

    if (CONFIG.makeBackup) {
      fs.writeFileSync(file + '.bak', content, 'utf8');
    }

    fs.writeFileSync(file, newContent, 'utf8');
    console.log(`✔  Footer update ho gaya:     ${file}`);
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
