#!/usr/bin/node

// A script that  imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const dict = require('./101-data.js').dict;
const usersByOccurrence = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (!usersByOccurrence[occurrence]) {
    usersByOccurrence[occurrence] = [];
  }
  usersByOccurrence[occurrence].push(userId);
}
console.log(usersByOccurrence);
