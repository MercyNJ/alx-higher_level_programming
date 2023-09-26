#!/usr/bin/node
// Script that writes a string to a file.

const fs = require('fs');

const filepath = process.argv[2];
const content = process.argv[3];

if (!filepath || !content) {
  console.error('Usage:node writeToFile.js <file_path><content_to_write>');
  process.exit(1);
}

fs.writeFile(filepath, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log('File written successfully.');
  }
});
