#!/usr/bin/node

// A script that prints the first argument passed to it.

const args = process.argv.slice(2);
const args1st = args[0];

if (args1st === undefined) {
  console.log('No argument');
} else {
  console.log(args1st);
}
