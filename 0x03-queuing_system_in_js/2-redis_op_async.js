import redis from 'redis'
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);

const client = redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
	getAsync(schoolName).then((result) => {
		console.log(result);
	}).catch((err) => {
		console.log(err);
	});
}

client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
