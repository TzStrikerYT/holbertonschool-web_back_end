import express from 'express';
import serverController from './routes/index';

const app = express();
const PORT = 1245;

serverController(app);

app.listen(PORT, () => {
  console.log(`Example app listening at http://localhost:${PORT}`);
});

export default app;
