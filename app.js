const express = require('express');
const app = express();
const port = 7000;

app.use(express.static(__dirname));

app.listen(port, () => {
    console.log(`Servidor rodando na porta http://localhost:${port}/`);
});