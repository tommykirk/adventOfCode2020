// https://adventofcode.com/2020/day/5

const fs = require("fs");

const flightMapData = fs.readFileSync(
  "billy/day.5/data.txt",
  "utf8",
  (err, data) => {
    if (err) throw err;
  }
);

let seats = flightMapData.split("\n");

const totalRows = 127; // 0 - 127
const totalCols = 7; // 0 - 7

const colCharacters = 7;
const rowCharacters = 3;

const findSeat = (seat) => {
  let row = 0;
  let col = 0;
  let minRowRange = 0;
  let minColRange = 0;
  let maxRowRange = totalRows;
  let maxColRange = totalCols;

  for (let i = 0; i < seat.length; i++) {
    const char = seat.charAt(i);
    // console.log(char);
    /// row
    const newRowRange = (maxRowRange - minRowRange) / 2;
    // console.log("newRowRange", newRowRange);
    if (char === "F") {
      // lower half
      maxRowRange = maxRowRange - Math.ceil(newRowRange);
    } else if (char === "B") {
      // upper half
      minRowRange = minRowRange + Math.ceil(newRowRange);
    }

    // console.log("maxRowRange", maxRowRange);
    // console.log("minRowRange", minRowRange);
    if (maxRowRange === minRowRange) {
      row = minRowRange;
    }

    const newColRange = (maxColRange - minColRange) / 2;
    // column
    if (char === "L") {
      // lower half
      maxColRange = maxColRange - Math.ceil(newColRange);
    } else if (char === "R") {
      // upper half
      minColRange = minColRange + Math.ceil(newColRange);
    }

    // console.log("maxColRange", maxColRange);
    // console.log("minColRange", minColRange);
    if (maxColRange === minColRange) {
      col = minColRange;
    }
  }

  const seatId = row * 8 + col;

  // console.log("seat:", seat, "row:", row, "col:", col, "seatId:", seatId);

  return { row, col };
};

// let maxSeatId = 0;
let plane = {};

seats.map((seat) => {
  const { row, col } = findSeat(seat);
  if (!plane[row]) {
    plane[row] = [];
  }
  plane[row] = plane[row].concat([col]);
});

console.log(plane);
const planeCols = [0, 1, 2, 3, 4, 5, 6, 7];
let mySeatRow = 0;
let mySeatCol = 0;
Object.keys(plane).map((key) => {
  const cols = plane[key];
  if (cols.length === 7) {
    console.log(key);
    mySeatRow = key;
    // find missing row
    planeCols.map((col) => {
      if (!cols.includes(col)) {
        mySeatCol = col;
      }
    });
  }
});

const mySeatId = mySeatRow * 8 + mySeatCol;
console.log(mySeatId);
