const fs = require('fs');

function countStudents(path) {
  let content;
  try {
    content = fs.readFileSync(`${path}`, { encoding: 'utf8' });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
  const chainStudents = content.split('\n');
  let students = chainStudents.filter((item) => item);

  const NUMBER_OF_STUDENTS = students.length ? students.length - 1 : 0;
  console.log(`Number of students: ${NUMBER_OF_STUDENTS}`);

  students = students.slice(1);
  const dict = {};
  students.forEach((element) => {
    const list = element.split(',');
    const key = list[3];
    if (!(key in dict)) {
      dict[key] = [];
    }
    dict[key].push(`${list[0]}`);
  });
  for (const i in dict) {
    if (i) {
      console.log(`Number of students in ${i}: ${dict[i].length}. List: ${dict[i].join(', ')}`);
    }
  }
}
module.exports = countStudents;
