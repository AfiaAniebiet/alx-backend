import { createQueue } from 'kue';
const queue = createQueue();

const jobDataObj = {
  phoneNumber: '2348027872415',
  message: 'This is your account verification code',
}

const job = queue.create('push_notification_code', jobDataObj).save(err => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
