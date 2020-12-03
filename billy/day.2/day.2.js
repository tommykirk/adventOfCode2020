// https://adventofcode.com/2020/day/2

const fs = require("fs");

const passwordData = fs.readFileSync("./data.txt", "utf8", (err, data) => {
  if (err) throw err;
  // console.log(data);
});

// console.log(passwordData);

let lines = passwordData.split("\n");

console.log(`"file.txt" contains ${lines.length} lines`);
console.log(`First line : ${lines[0]}`);

// part 1

// parse a line
// 2-8 t: pncmjxlvckfbtrjh

const isPasswordValid = (line) => {
  const splitLine = line.split(": ");
  const passwordPolicy = splitLine[0];
  const password = splitLine[1];

  const passwordPolicySplit = passwordPolicy.split(" ");
  const passwordPolicyCount = passwordPolicySplit[0];

  const minimumTimes = passwordPolicyCount.split("-")[0];
  const maximumTimes = passwordPolicyCount.split("-")[1];
  const letter = passwordPolicySplit[1].charAt(0);

  const regEx = new RegExp(letter, "g");

  const matchesCount = ((password || "").match(regEx) || []).length;

  return matchesCount >= minimumTimes && matchesCount <= maximumTimes;
};

// part 2

const isPasswordValid2 = (line) => {
  const splitLine = line.split(": ");
  const passwordPolicy = splitLine[0];
  const password = splitLine[1];

  const passwordPolicySplit = passwordPolicy.split(" ");
  const passwordPolicyCount = passwordPolicySplit[0];

  const index1 = passwordPolicyCount.split("-")[0];
  const index2 = passwordPolicyCount.split("-")[1];
  const letter = passwordPolicySplit[1].charAt(0);

  const isFirstIndexMatch = password.charAt(index1 - 1) === letter;
  const isSecondIndexMatch = password.charAt(index2 - 1) === letter;

  return (
    (isFirstIndexMatch || isSecondIndexMatch) &&
    !(isFirstIndexMatch && isSecondIndexMatch)
  );
};

let validPasswordCount = 0;

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];

  if (isPasswordValid2(line)) {
    validPasswordCount += 1;
  }
}

console.log("validPasswordCount", validPasswordCount);
