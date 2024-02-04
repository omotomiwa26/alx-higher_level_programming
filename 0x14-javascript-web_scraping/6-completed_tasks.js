#!/usr/bin/node
// This node script computes the number of tasks completed by user id.

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node count-completed-tasks.js <api-url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    if (response.statusCode === 200) {
      const todosData = JSON.parse(body);

      const completedTasksByUser = todosData.reduce((result, todo) => {
        if (todo.completed) {
          result[todo.userId] = (result[todo.userId] || 0) + 1;
        }
        return result;
      }, {});

      console.log(JSON.stringify(completedTasksByUser, null, 2).replace(/"/g, "'"));
    } else {
      console.error('Error:', response.statusCode);
    }
  }
});
