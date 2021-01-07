import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

export default function serverController(app) {
  const router = express.Router();
  app.use('/', router);

  app.get('/', (req, res) => {
    AppController.getHomepage(req, res);
  });

  app.get('/students', (req, res) => {
    StudentsController.getAllStudents(req, res, process.argv[2]);
  });

  app.get('/students/:major', (req, res) => {
    StudentsController.getAllStudentsByMajor(req, res, process.argv[2]);
  });
}
