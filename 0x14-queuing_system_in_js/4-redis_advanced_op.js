import redis from 'redis'
const client = redis.createClient();

client.once('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, i) => {
    client.hset('HolbertonSchools', key, values[i], redis.print);
});

client.hgetall('HolbertonSchools', (error, value) => {
    console.log(value)
})