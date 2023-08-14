#!/usr/bin/node

// A script that  script that prints My number: <first arg converted in int> if 1st arg can be converted to an integer.

const num = parseInt(process.argv[2], 10);

if (isNaN(num) === false) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
