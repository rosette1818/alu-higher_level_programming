#!/usr/bin/node

const x = parseInt(process.argv[2], 10);

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
