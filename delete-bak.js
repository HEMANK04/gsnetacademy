const fs = require("fs");
const path = require("path");

const folderPath = __dirname;

fs.readdirSync(folderPath).forEach(file => {
    if (file.endsWith(".bak")) {
        const filePath = path.join(folderPath, file);

        fs.unlinkSync(filePath);

        console.log("Deleted:", file);
    }
});

console.log("All .bak files deleted.");