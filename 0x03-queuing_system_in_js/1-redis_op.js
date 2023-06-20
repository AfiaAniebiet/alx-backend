import { createClient, print } from 'redis'

const client = createClient();

const redisConnect = () => {
  client.on('error', err => console.log('Redis client not connected to the server: ', err));

  client.on('connect', () => console.log('Redis client connected to the server'))
}
redisConnect();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, resp) => {
    print(`Output: ${resp}`);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, response) => {
    console.log(response);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
