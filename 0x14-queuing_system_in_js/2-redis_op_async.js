import redis from 'redis'
import { promisify } from 'util'

const client = redis.createClient();
const asyncGet = promisify(client.get).bind(client)
const asyncSet = promisify(client.set).bind(client)

client.once('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

/*  Normal Functions
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => console.log(reply) );
}
*/

async function setNewSchool(schoolName, value) {
    await asyncSet(schoolName, value)
    .then((reply) => {
        redis.print(`Reply: ${reply}`)
    })
}

async function displaySchoolValue(schoolName) {
    console.log(await asyncGet(schoolName))
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');