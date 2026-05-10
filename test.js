const fs = require('fs');
const content = fs.readFileSync('app2.js', 'utf8');

// We just want to see if `const themesData = parseTextToJSON(rawText);` crashes.
const script = content.split('// DOM Elements')[0] + `
console.log("Parsed " + themesData.length + " themes.");
themesData.forEach(t => {
    console.log(t.title);
    if (!t.title) throw new Error("Title is undefined!");
    console.log("  Questions: " + t.questions.length);
});
`;
eval(script);
