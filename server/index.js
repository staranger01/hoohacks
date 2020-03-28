const express = require("express");

const app = express();

// if (process.env.NODE_ENV == "PRODUCTION") {
app.get("*", (req, res) => {
  const path = require("path");
  res.sendFile(path.join(__dirname, "client/build/index.html"));
});
// }

let PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log("running on server ", PORT);
});
