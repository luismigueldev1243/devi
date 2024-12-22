const express = require("express");
const cors = require("cors");
const app = express();

app.use(express.json());
app.use(cors());

let users = {};

app.get("/user", (req, res) => {
  res.send(
    `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="refresh" content="1; url=/user">
      <title>Auto Refresh</title>
    </head>
    <body>
      <pre>${JSON.stringify(users, null, 2)}</pre>
    </body>
    </html>
  `
  );
});

app.post("/user", (req, res) => {
  const { nome, idade, senha, level } = req.body;
  if (users[nome]) {
    res.send("oh oh :(. the user: " + nome + " already exists");
  } else {
    users[nome] = { idade: idade, senha: senha, level: level };
    res.send("usuario " + nome + " feito!");
  }
});

app.post("/changeuser", (req, res) => {
  const { usersel, lvl } = req.body;
  users[usersel].level = lvl;
});

app.delete("/remove/:id", (req, res) => {
  const id = req.params.id;

  if (users[id]) {
    delete users[id];
    res.send("sucesfuly deleted ");
  } else {
    res.send("the user" + " '" + id + "' " + "does not exists");
  }
});

app.listen(3000, () => {
  console.log("server is running on port 3000");
});
