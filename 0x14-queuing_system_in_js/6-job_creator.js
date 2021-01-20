import kue from 'kue';
const queue = kue.createQueue();

const job = {
    phoneNumber: "3240861107",
    message: "This is message of test"
}

const jobsiwis = queue.create('push_notification_code', job).save((err) => {
    if( !err ) console.log(`Notification job created: ${jobsiwis.id}`);
})

jobsiwis.on('complete', function() {
    console.log('Job completed with data ');

}).on('failed', function(err, done) {
    console.log('Notification job completed');
})