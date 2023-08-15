#!/usr/bin/node

// A script that contains a class square inheriting from previous square class.

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
