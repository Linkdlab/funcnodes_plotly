import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, "..");

const srcStylePath = path.join(rootDir, "src", "style.css");
const distStylePath = path.join(rootDir, "dist", "plugin-custom-renders.css");
const packagedStylePath = path.join(
  rootDir,
  "..",
  "funcnodes_plotly",
  "react_plugin",
  "plugin-custom-renders.css"
);

function readTextFile(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

test("src/style.css uses Radix `dialog-children` selector for dialog sizing", () => {
  const css = readTextFile(srcStylePath);
  assert.match(css, /\.dialog-children\s+\.funcnodes_plotly_container\s*\{/);
});

test("src/style.css does not use deprecated `dialogchildren` selector", () => {
  const css = readTextFile(srcStylePath);
  assert.doesNotMatch(css, /\.dialogchildren\s+\.funcnodes_plotly_container\s*\{/);
});

test("src/style.css defines a minimum preview size", () => {
  const css = readTextFile(srcStylePath);
  assert.match(
    css,
    /\.funcnodes_plotly_container\s*\{[^}]*min-height:\s*300px;[^}]*min-width:\s*300px;[^}]*\}/s
  );
});

test("dist/plugin-custom-renders.css matches src dialog selector", () => {
  const css = readTextFile(distStylePath);
  assert.match(css, /\.dialog-children\s+\.funcnodes_plotly_container\s*\{/);
  assert.doesNotMatch(css, /\.dialogchildren\s+\.funcnodes_plotly_container\s*\{/);
});

test("funcnodes_plotly/react_plugin/plugin-custom-renders.css matches src dialog selector", () => {
  const css = readTextFile(packagedStylePath);
  assert.match(css, /\.dialog-children\s+\.funcnodes_plotly_container\s*\{/);
  assert.doesNotMatch(css, /\.dialogchildren\s+\.funcnodes_plotly_container\s*\{/);
});
