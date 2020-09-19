"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .trim()
    .split("\n")
    .map((string) => {
      return string.trim();
    });

  main();
});

function readLine() {
  return inputString[currentLine++];
}

function vowelsAndConsonants(s) {
  var vowel = [];
  var consonants = [];
  var string = [];
  for (let i = 0; i < s.length; i++) {
    string.push(s[i]);
  }
  string.forEach((i) => {
    switch (i) {
      case "a":
      case "e":
      case "i":
      case "o":
      case "u":
        vowel.push(i);
        break;
      default:
        consonants.push(i);
    }
  });

  vowel.forEach((i) => {
    console.log(i);
  });
  consonants.forEach((i) => {
    console.log(i);
  });
}

function main() {
  const s = readLine();

  vowelsAndConsonants(s);
}

