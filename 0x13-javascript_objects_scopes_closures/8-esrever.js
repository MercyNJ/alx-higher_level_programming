#!/usr/bin/node

// A script that contains  a function that returns the reversed version of a list without using inbuilt reverse method.

exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
