// Import the required modules
import kue from 'kue';

// Create an array of jobs
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  // ... Add more job objects as needed
];

// Create a Kue queue
const queue = kue.createQueue();

// Function to send a notification
const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

// Loop through the array of jobs and create a job for each
jobs.forEach((jobData, index) => {
  const job = queue.create('push_notification_code_2', jobData);

  // On successful job creation
  job.save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  // On job completion
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // On job failure
  job.on('failed', (errorMessage) => {
    console.log(`Notification job ${job.id} failed: ${errorMessage}`);
  });

  // On job progress
  job.on('progress', (progress, data) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });

  // Simulate job progress (for demonstration purposes)
  job.progress(index * 10, 10);

  // Uncomment the line below to simulate job completion (for demonstration purposes)
  // job.complete();
});
