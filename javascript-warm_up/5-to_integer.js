#!/usr/bin/node
const args = process.argv[2];
const num = Number(args);
if (args === undefined || Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(num, 10)}`);
}
