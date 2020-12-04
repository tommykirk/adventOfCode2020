// https://adventofcode.com/2020/day/4

const fs = require("fs");

const passportData = fs.readFileSync("day.4/data.txt", "utf8", (err, data) => {
  if (err) throw err;
});

let passports = passportData.split("\n\n");

const BirthYear = "byr"; // (Birth Year)
const IssueYear = "iyr"; // (Issue Year)
const ExpirationYear = "eyr"; // (Expiration Year)
const Height = "hgt"; // (Height)
const HairColor = "hcl"; // (Hair Color)
const EyeColor = "ecl"; // (Eye Color)
const PassportID = "pid"; // (Passport ID)
const CountryID = "cid"; // (Country ID)

// byr (Birth Year) - four digits; at least 1920 and at most 2002.
const isValidBirthYear = (year) => year >= 1920 && year <= 2002;

// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
const isValidIssueYear = (year) => year >= 2010 && year <= 2020;

// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
const isValidExpirationYear = (year) => year >= 2020 && year <= 2030;

// hgt (Height) - a number followed by either cm or in:
// If cm, the number must be at least 150 and at most 193.
// If in, the number must be at least 59 and at most 76.
const isValidHeight = (height) => {
  const unit = height && height.slice(-2);
  const number = height && height.slice(0, -2);
  if (unit === "cm") {
    return number >= 150 && number <= 193;
  }

  if (unit === "in") {
    return number >= 59 && number <= 76;
  }

  return false;
};

// hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
const isValidHairColor = (hairColor) => {
  return hairColor && hairColor.match(new RegExp(/[#][\dabcdef]{6}/));
};

// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
const isValidEyeColor = (eyeColor) => {
  const eyeColorArray = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];
  return eyeColor && eyeColorArray.includes(eyeColor);
};

// pid (Passport ID) - a nine-digit number, including leading zeroes.
const isValidPassportId = (pptId) => {
  return pptId && pptId.match(new RegExp(/\d{9}/)) && pptId.length <= 9;
};

// cid (Country ID) - ignored, missing or not.

const functionMap = {
  [BirthYear]: isValidBirthYear,
  [IssueYear]: isValidIssueYear,
  [ExpirationYear]: isValidExpirationYear,
  [Height]: isValidHeight,
  [HairColor]: isValidHairColor,
  [EyeColor]: isValidEyeColor,
  [PassportID]: isValidPassportId,
};

const requiredFields = [
  BirthYear,
  IssueYear,
  ExpirationYear,
  Height,
  HairColor,
  EyeColor,
  PassportID,
];

const isPassportValid = (passport) => {
  const fields = passport.split(/\s/);
  let validity = true;

  const passportFieldKeys = [];
  let passportFieldValues = {};
  for (let i = 0; i < fields.length; i++) {
    const field = fields[i];
    const fieldKey = field.split(":")[0];
    const fieldValue = field.split(":")[1];

    passportFieldKeys.push(fieldKey);
    passportFieldValues = { ...passportFieldValues, [fieldKey]: fieldValue };
    functionMap;
  }

  for (let j = 0; j < requiredFields.length; j++) {
    const requiredField = requiredFields[j];

    if (!passportFieldKeys.includes(requiredField)) {
      validity = false;
    }
  }

  for (let j = 0; j < requiredFields.length; j++) {
    const requiredField = requiredFields[j];

    const fieldValidityFunction = functionMap[requiredField];
    const fieldValue = passportFieldValues[requiredField];

    console.log(requiredField, fieldValue, fieldValidityFunction(fieldValue));

    if (!fieldValidityFunction(fieldValue)) {
      validity = false;
    }
  }

  console.log(validity);
  return validity;
};

// Part 1
let validPassportCount = 0;
for (let i = 0; i < passports.length; i++) {
  const passport = passports[i];
  const isValidPassport = isPassportValid(passport);
  console.log("Passport", i);

  if (isValidPassport) {
    validPassportCount += 1;
  }
}
console.log(validPassportCount);

// Part 2
