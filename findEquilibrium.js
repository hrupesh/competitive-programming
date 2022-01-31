const findEquilibriumIndex = (arr) => {
  let mid = parseInt(arr.length / 2);
  let leftSum = 0,
    rightSum = 0;
  for (let i = 0; i < mid; i++) {
    leftSum += arr[i];
  }
  for (let i = mid + 1; i < arr.length; i++) {
    rightSum += arr[i];
  }
  if (leftSum === rightSum) return mid;
  if (rightSum > leftSum) {
    while (rightSum > leftSum && mid < arr.length - 1) {
      rightSum -= arr[mid + 1];
      leftSum += arr[mid];
      mid++;
    }
  } else {
    while (leftSum > rightSum && mid > 0) {
      rightSum += arr[mid];
      leftSum -= arr[mid - 1];
      mid--;
    }
  }
  console.log(leftSum, rightSum);
  return leftSum === rightSum ? mid : -1;
};

let arr = [-7, 1, 5, 2, -4, 3, 0];
console.log(`[${arr?.toString()}]`);
console.log(findEquilibriumIndex(arr));
