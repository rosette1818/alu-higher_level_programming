#!/usr/bin/node

const args = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';

for (let i = 0; i < args.length; i++) {
  output += args[i] + '\n';
}

console.log(output.trimEnd());
