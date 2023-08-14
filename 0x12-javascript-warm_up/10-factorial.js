#!/usr/bin/node

// A script that computes and prints a factorial.

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const num = parseInt(process.argv[2], 10);

console.log(factorial(num));
