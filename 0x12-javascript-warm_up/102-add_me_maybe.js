#!/usr/bin/node

// A script that contains a function that increments and calls a function.

function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

exports.addMeMaybe = addMeMaybe;
