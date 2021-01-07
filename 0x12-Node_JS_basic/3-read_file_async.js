const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, (error, data) => {
      if (error) reject(Error('Cannot load the database'));
      if (data) {
        const response = [];
        const content = data.toString();
        const chainStudents = content.split('\n');
        let students = chainStudents.filter((item) => item);

        const NUMBER_OF_STUDENTS = students.length ? students.length - 1 : 0;
        const msg = `Number of students: ${NUMBER_OF_STUDENTS}`;
        console.log(msg);
        response.push(msg);

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
            const msg2 = `Number of students in ${i}: ${dict[i].length}. List: ${dict[i].join(', ')}`;
            console.log(msg2);
            response.push(msg2);
          }
        }
        resolve(response);
      }
    });
  });
}
module.exports = countStudents;
