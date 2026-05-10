const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const fs = require("fs");

const html = fs.readFileSync("index.html", "utf8");
const js = fs.readFileSync("app2.js", "utf8");

const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("error", (error) => {
  console.error("JSDOM ERROR:", error);
});
virtualConsole.on("log", (message) => {
  console.log("JSDOM LOG:", message);
});

const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole });

try {
  dom.window.eval(js);
  console.log("Number of theme cards generated:", dom.window.document.querySelectorAll('.theme-card').length);
} catch (e) {
  console.error("ERROR EVALUATING JS:", e);
}
