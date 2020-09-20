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

function getSecondLargest(nums) {
  nums = nums.sort();
  let max = nums[nums.length - 1];
  let i = nums.length - 1;
  while (i >= 0) {
    if (nums[i] < max) {
      return nums[i];
      break;
    }
    i--;
  }
}

function main() {
  const n = +readLine();
  const nums = readLine().split(" ").map(Number);

  console.log(getSecondLargest(nums));
}
