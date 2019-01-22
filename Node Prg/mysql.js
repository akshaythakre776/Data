var mysql = require('mysql');
var con = mysql.createConnection({
  
host: "localhost",
  user: "root",
  password: "",
  database: "angular_db"
 
});
con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});

con.query('SELECT * from student', function (err, result, fields) {
  if (err) throw err
   console.log('The result is: ', result)
});

con.query('SELECT * from student', function (err, result, fields) {
    if (err) throw err
      console.log('The result is: ', result)
});    

con.end(function(err) {
    if (err) throw err;
    console.log("Connection Closed!");
  });