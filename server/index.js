const express = require("express");

const app = express();

if (process.env.NODE_ENV == "PRODUCTION") {
  app.get("*", (req, res) => {
    res.sendFile("./client/build/index.html");
  });
}
