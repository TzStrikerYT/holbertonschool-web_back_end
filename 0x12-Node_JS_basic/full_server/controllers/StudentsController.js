const readDatabase = require('../utils');

export default class StudentsController {
  static getAllStudents(request, response, DB) {
    readDatabase(DB)
      .then((data) => {
        const msg = 'This is the list of our students\n';
        const newData = msg + data;
        response.send(200, newData.slice(0, -1));
      })
      .catch((error) => {
        response.send(500, error.message);
      });
  }

  static getAllStudentsByMajor(request, response, DB) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.send(500, 'Major parameter must be CS or SWE');
    } else {
      readDatabase(DB)
        .then((fields) => {
          const list = fields.split('\n');
          const [field1, field2] = list.slice(1, 3);

          let students;
          if (major === 'CS') {
            students = field1;
          } else {
            students = field2;
          }
          students = students.split('. ');

          response.send(200, `${students[1]}`);
        })
        .catch(() => response.send(500, 'Cannot load the database'));
    }
  }
}
