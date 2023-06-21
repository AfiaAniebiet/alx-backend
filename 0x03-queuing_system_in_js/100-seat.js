import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';

const client = createClient();
const queue = createQueue();

const clientGet = promisify(client.get).bind(client);
const clientSet = promisify(client.set).bind(client);

const redisConnection = function() {
  client.on('error', (error) => {
    console.log(`Redis connection failed: ${error}`);
  });

  client.on('connect', () => {
    console.log('Connection to Redis successful');
  });
}
redisConnection();

function reserveSeat(number) {
  client.set('available_seats', number);
}

function getCurrentAvailableSeats(number) {
  client.get(number, (err, response) => {
    console.log(response);
  });
}
