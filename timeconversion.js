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
  hrs = parseInt(hrs);

  if (s.includes("PM")) {
    return "Time in PM" + hrs;
  } else if (s.includes("AM")) {
    return "Time in AM";
  }
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const s = readLine();

  let result = timeConversion(s);

  ws.write(result + "\n");

  ws.end();
}
