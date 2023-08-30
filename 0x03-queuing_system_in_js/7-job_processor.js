// Import the required modules
import kue from 'kue';

// Create an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send a notification
const sendNotification = (phoneNumber, message, job, done) => {
  // Track progress of the job
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track progress to 50%
  job.progress(50, 100);

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Simulate the completion of the job (for demonstration purposes)
  setTimeout(() => {
    job.progress(100, 100);
    done();
  }, 2000); // Simulating a delay of 2 seconds
};

// Create a Kue queue for processing jobs
const queue = kue.createQueue({
  concurrency: 2, // Process two jobs at a time
});

// Process jobs from the queue
queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Log when processing starts
console.log('Job processor is running...');
