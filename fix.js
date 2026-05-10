const fs = require('fs');
let c = fs.readFileSync('app2.js', 'utf8');
c = c.replace(/\\`/g, '`');
c = c.replace(/\\\$/g, '$');
fs.writeFileSync('app2.js', c);
console.log("Fixed!");
