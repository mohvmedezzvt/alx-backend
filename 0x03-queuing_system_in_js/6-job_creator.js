import kue from 'kue';
import redis from 'redis';

const queue = kue.createQueue({
  redis: {
    createClientFactory: function () {
      return redis.createClient();
    }
  }
});

const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message.',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) throw err;
    console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (err) => {
  console.log(`Notification job failed with error: ${err}`);
});

kue.app.listen(3000, () => {
  console.log('Kue UI is running on port 3000');
});
