const fs = require('fs');

module.exports = function readDatabase(path) {
  return new Promise(((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, paramsStudents) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }

      let students = paramsStudents;
      students = students.split('\n');
      const headers = students.shift().split(',');

      const groupingStudentsField = {};
      const studentsObjects = [];

      students.forEach((student) => {
        if (student) {
          const studentInfo = student.split(',');
          const studentObject = {};

          headers.forEach((header, index) => {
            studentObject[header] = studentInfo[index];
            if (header === 'field') {
              if (groupingStudentsField[studentInfo[index]]) {
                groupingStudentsField[studentInfo[index]].push(studentObject.firstname);
              } else {
                groupingStudentsField[studentInfo[index]] = [studentObject.firstname];
              }
            }
          });
          studentsObjects.push(studentObject);
        }
      });
      const numberStudents = `Number of students: ${studentsObjects.length}`;

      let response = `${numberStudents}\n`;
      console.log(numberStudents);

      for (const groupStudent in groupingStudentsField) {
        if (groupingStudentsField[groupStudent]) {
          const listStudents = groupingStudentsField[groupStudent];
          const responseGroupStudents = `Number of students in ${groupStudent}: ${listStudents.length}. List: ${listStudents.join(', ')}`;
          response += `${responseGroupStudents}\n`;
          console.log(responseGroupStudents);
        }
      }
      resolve(response);
    });
  }));
};
