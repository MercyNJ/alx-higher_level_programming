#!/usr/bin/node

// A script that  imports an array and computes a new array.

const data = require('./100-data');

const initialList = data.list;
const newList = initialList.map((value, index) => value * index);

console.log(initialList);
console.log(newList);
