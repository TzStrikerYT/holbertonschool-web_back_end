function createPushNotificationsJobs(jobs, queue) {
    if (!(jobs instanceof Array)) throw Error('Jobs is not an array')

    jobs.forEach((index) => {
        const job = queue.create('push_notification_code_3', index)
        .save((error) => {
            if (!error) console.log(`Notification job created: ${job.id}`);
        })
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });
    
        job.on('failed', (errorMessage) => {
            console.log(`Notification job ${job.id} failed: ${errorMessage}`);
        });
    
        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    })
}
module.exports = createPushNotificationsJobs; 