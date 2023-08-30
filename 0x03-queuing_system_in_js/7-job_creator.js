// Import the required modules
import kue from 'kue';

// Create an array of jobs
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  // ... (add more objects here)
];

// Create a Kue queue
const queue = kue.createQueue();

// Loop through the jobs array and create jobs
jobs.forEach((jobData, index) => {
  const job = queue
    .create('push_notification_code_2', jobData)
    .save((err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

  job
    .on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    })
    .on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
