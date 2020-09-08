"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/*
 * Complete the 'getTotalX' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

function getTotalX(a, b) {
  var X = [];
  var n = a[a.length - 1];
  var okay = true;

  for (let i = 0; i < a.length; i++) {
    if (n % a[i] == 0) {
      for (let j = 0; j < b.length; j++) {
        if (!(b[i] % n == 0)) {
          okay = false;
        }
      }
    }
  }

  if (okay) {
    X.push(n);
  }

  var n2 = a[0] * a[1];
  var okay2 = false;
  if (n2 < b[0]) {
    for (let i = 0; i < b.length; i++) {
      if (b[i] % n2 == 0) {
        okay2 = true;
      } else {
        okay2 = false;
      }
    }
  }
  if (okay2) {
    X.push(n2);
  }

  var n3 = b[0];
  var okay3 = false;

  for (let i = 0; i < a.length; i++) {
    if (n3 % a[i] == 0) {
      for (let j = 0; j < b.length; j++) {
        if (b[i] % n == 0) {
          okay3 = true;
        } else {
          okay3 = false;
        }
      }
    }
  }

  if (okay3) {
    X.push(n3);
  }

  return X;
}

function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const firstMultipleInput = readLine().replace(/\s+$/g, "").split(" ");

  const n = parseInt(firstMultipleInput[0], 10);

  const m = parseInt(firstMultipleInput[1], 10);

  const arr = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((arrTemp) => parseInt(arrTemp, 10));

  const brr = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((brrTemp) => parseInt(brrTemp, 10));

  const total = getTotalX(arr, brr);

  ws.write(total + "\n");

  ws.end();
}
