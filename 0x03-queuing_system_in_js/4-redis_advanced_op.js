import { createClient, print } from 'redis';
const client = createClient();

client.on("error", (error) => {
    if (error) console.log(`Redis client not connected to the server: ${error}`)
  }).on('ready', () => {
      console.log('Redis client connected to the server');
  });

const KEYHASH = 'HolbertonSchools';

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, idx) => {
  client.hset(KEYHASH, key, values[idx], (err, resp) => {
    print(`Reply: ${resp}`);
  });
});

client.hgetall(KEYHASH, (err, value) => {
  console.log(value);
});
