import createPushNotificationsJobs from './8-job.js';
import kue from 'kue';
const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  // Test cases go here
});

before(() => {
  queue.testMode.enter();
});

after(() => {
  queue.testMode.exit();
});

it('display an error message if jobs is not an array', (done) => {
  // Test implementation
});

it('create two new jobs to the queue', (done) => {
  // Test implementation
});

it('display an error message if jobs is not an array', (done) => {
  const nonArrayJobs = { phoneNumber: '123', message: 'Test' };

  // Call the function
  try {
    createPushNotificationsJobs(nonArrayJobs, queue);
  } catch (error) {
    // Verify the error message
    assert.strictEqual(error.message, 'Jobs is not an array');
    done();
  }
});
