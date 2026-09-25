#!/usr/bin/node

const size = parseInt(process.argv[2], 10);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  let square = '';
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    square += row + '\n';
  }
  if (square) {
    console.log(square.trimEnd());
  }
}
