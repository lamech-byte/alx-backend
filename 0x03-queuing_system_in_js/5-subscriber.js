// Import the required modules
import redis from 'redis';

// Create a Redis subscriber client
const subscriber = redis.createClient();

// Handle successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection error
subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the holberton school channel
subscriber.subscribe('holberton school channel');

// Handle incoming messages
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
