#!/usr/bin/node

// A script that prints two arguments passed to it in a specified format.

const arg1 = process.argv[2] || 'undefined';
const arg2 = process.argv[3] || 'undefined';

console.log(arg1 + ' is ' + arg2);
