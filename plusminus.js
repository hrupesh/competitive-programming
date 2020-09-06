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
    .replace(/\s*$/, "")
    .split("\n")
    .map((str) => str.replace(/\s*$/, ""));

  main();
});

function readLine() {
  return inputString[currentLine++];
}

// Complete the plusMinus function below.
function plusMinus(arr) {
  var positive = 0.0;
  var negative = 0.0;
  var zeroes = 0.0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      positive += 1;
    } else if (arr[i] < 0) {
      negative += 1;
    } else {
      zeroes += 1;
    }
  }

  positive = positive / arr.length;
  positive = positive.toFixed(6);
  negative = negative / arr.length;
  negative = negative.toFixed(6);
  zeroes = zeroes / arr.length;
  zeroes = zeroes.toFixed(6);

  console.log(positive);
  console.log(negative);
  console.log(zeroes);
}

function main() {
  const n = parseInt(readLine(), 10);

  const arr = readLine()
    .split(" ")
    .map((arrTemp) => parseInt(arrTemp, 10));

  plusMinus(arr);
}

