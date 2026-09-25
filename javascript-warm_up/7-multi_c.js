#!/usr/bin/node

const languages = ['C is fun', 'C is fun', 'C is fun'];
let output = '';

for (let i = 0; i < languages.length; i++) {
  output += languages[i] + '\n';
}

console.log(output.trimEnd());
