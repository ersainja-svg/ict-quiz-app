const fs = require('fs');
const path = require('path');

const fileContent = fs.readFileSync(path.join(__dirname, 'app.js'), 'utf8');

// evaluate the parse function
const code = fileContent.substring(0, fileContent.indexOf('// App State')) + `
try {
    const data = parseTextToJSON(rawText);
    console.log("Parsed themes length:", data.length);
    console.log("Theme 1 questions:", data[0] && data[0].questions.length);
    if(data.length > 0) {
        data.forEach((t, i) => {
            if(!t || !t.questions) {
                console.log('Theme ' + i + ' is invalid!');
            } else {
                t.questions.forEach((q, j) => {
                    if(q.options.length === 0) {
                        console.log('Theme ' + i + ' Question ' + j + ' has NO options! text: ' + q.text);
                    }
                })
            }
        });
    }
} catch (e) {
    console.error("Error running parse:", e);
}
`;

eval(code);
