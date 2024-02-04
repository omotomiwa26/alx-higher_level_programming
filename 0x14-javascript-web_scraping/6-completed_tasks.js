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
      const tasksData = JSON.parse(body);

      const completedTasksByUser = {};

      tasksData.forEach(task => {
        if (task.completed) {
          const userId = task.userId;
          completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
        }
      });
      for (const userId in completedTasksByUser) {
        console.log(`${userId}: ${JSON.stringify(completedTasksByUser[userId], null, 2)}`);
      }
    } else {
      console.error('Error:', response.statusCode);
    }
  }
});
