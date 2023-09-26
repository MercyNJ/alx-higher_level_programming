#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasksCompleted = {};
  let jsonData;

  try {
    jsonData = JSON.parse(body);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
    return;
  }

  jsonData.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
