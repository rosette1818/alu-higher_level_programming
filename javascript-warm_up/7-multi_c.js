#!/usr/bin/node

const x = parseInt(process.argv[2], 10);
const languages = ['C is fun', 'C is fun', 'C is fun'];
let output = '';
if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let output = '';
  for (let i = 0; i < x; i++) {
    output += 'C is fun\n';
  }
  if (output) {
    console.log(output.trimEnd());
  }
}
