#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const dataA = fs.readFileSync(fileA);
const dataB = fs.readFileSync(fileB);

fs.writeFileSync(fileC, Buffer.concat([dataA, dataB]));
