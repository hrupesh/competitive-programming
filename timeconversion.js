"use strict";

const fs = require("fs");

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
    .map((str) => str.trim());

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the timeConversion function below.
 */
function timeConversion(s) {
  var hrs = s.slice(0, 2);
  var rest = s.slice(2, 8);
  hrs = parseInt(hrs);

  if (s.includes("PM")) {
    if (hrs == 12) {
      hrs = hrs;
    } else {
      hrs += 12;
    }
    return hrs + rest;
  } else if (s.includes("AM")) {
    if (hrs == 12) {
      hrs = "00";
    } else if (hrs < 10) {
      hrs = "0" + hrs;
    }
    return hrs + rest;
  }
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const s = readLine();

  let result = timeConversion(s);

  ws.write(result + "\n");

  ws.end();
}
