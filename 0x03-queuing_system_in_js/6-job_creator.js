// Import the required modules
import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification.'
};

// Create a job
const job = queue.create('push_notification_code', jobData)
  .save((error) => {
    if (!error) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Job completed event
job.on('complete', () => {
  console.log('Notification job completed');
});

// Job failed event
job.on('failed', () => {
  console.log('Notification job failed');
});
