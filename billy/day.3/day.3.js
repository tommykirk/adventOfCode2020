// https://adventofcode.com/2020/day/3

const fs = require("fs");

const treeData = fs.readFileSync("day.3/data.txt", "utf8", (err, data) => {
  if (err) throw err;
});

// Starting at the top-left corner of your map and following a slope of right 3 and down 1,
// how many trees would you encounter?

let treeRows = treeData.split("\n");

const countTrees = (treeRows, right, down) => {
  let treeCount = 0;
  let colIndex = 0;

  for (let i = 0; i < treeRows.length; i += down) {
    const row = treeRows[i];

    const square = row.charAt(colIndex);

    if (square === "#") {
      treeCount += 1;
    }

    colIndex += right;
    if (colIndex >= row.length) {
      colIndex -= row.length;
    }
  }

  return treeCount;
};

const tree1 = countTrees(treeRows, 3, 1);
const tree2 = countTrees(treeRows, 1, 1);
const tree3 = countTrees(treeRows, 5, 1);
const tree4 = countTrees(treeRows, 7, 1);
const tree5 = countTrees(treeRows, 1, 2);

console.log(tree1);
console.log(tree2);
console.log(tree3);
console.log(tree4);
console.log(tree5);

console.log(tree1 * tree2 * tree3 * tree4 * tree5);
