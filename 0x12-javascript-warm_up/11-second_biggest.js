#!/usr/bin/node

// A script that searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a);
  console.log(sorted[1]);
}
