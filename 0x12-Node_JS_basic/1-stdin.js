process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const name = process.stdin.read();
  if (name) console.log(`your name is: ${name}`);
});
process.stdin.on('end', () => {
  console.log('This important software is now closing\n');
});
