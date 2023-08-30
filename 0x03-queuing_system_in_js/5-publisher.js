// Import the required modules
import redis from 'redis';

// Create a Redis publisher client
const publisher = redis.createClient();

// Handle successful connection
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection error
publisher.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Function to publish a message after a certain time
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
};

// Call the function with different messages and times
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
