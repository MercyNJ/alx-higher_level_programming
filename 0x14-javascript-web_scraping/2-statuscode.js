#!/usr/bin/node
// Script that displays the status code of a GET request.

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Please provide a URL as an arg.');
  process.exit(1);
}

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
