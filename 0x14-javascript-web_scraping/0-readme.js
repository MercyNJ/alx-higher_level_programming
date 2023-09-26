#!/usr/bin/node
// Script that reads & prints content of a file.

const fs = require('fs');

const filepath = process.argv[2];

if (!filepath) {
  console.error('Provide file path as an arg.');
  process.exit(1);
}

fs.readFile(filepath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
