import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
  console.log('Redis client not connected to the server: ', error);
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
}

const setNewSchool = function(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const displaySchoolValue = function(schoolName) {
  client.get(schoolName, (err, response) => {
    console.log(response);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
