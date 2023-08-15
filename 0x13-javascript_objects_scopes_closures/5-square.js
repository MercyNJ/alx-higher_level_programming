#!/usr/bin/node

// A script that contains a class square inheriting from Rectangle class.

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
