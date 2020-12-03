// https://adventofcode.com/2020/day/1

const data = require("./data");

const sum = 2020;
const sumArray = [];

for (let i = 0; i < data.length; i++) {
  sumArray[i] = data[i];
}

for (let k = 0; k < data.length; k++) {
  sumArray[k] = data[k];
}

const sumsToTargetTwo = (arr, sumVal) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] === sumVal) {
        console.log(arr[i], arr[j]);
        // solution
        console.log(arr[i] * arr[j]);
        return true;
      }
    }
  }
  return false;
};

const sumsToTargetThree = (arr, sumVal) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      for (let k = j + 1; k < arr.length; k++) {
        if (arr[i] + arr[j] + arr[k] === sumVal) {
          console.log(arr[i], arr[j], arr[k]);
          // solution
          console.log(arr[i] * arr[j] * arr[k]);
          return true;
        }
      }
    }
  }
  return false;
};

sumsToTargetThree(data, sum);
