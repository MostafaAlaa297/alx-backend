import redis from 'redis'

const client = redis.createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, result) => {
		if (err) {
			console.log(err);
		} else {
			console.log(result);
		}
	});
}

client.on('error', (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
