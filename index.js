var mysql = require('mysql');

var con = mysql.createConnection({
    host:"remotemysql.com",
    user:"Rz8hqn1dk4",
    password:"nd0WKO3xeO",
});

con.connect(function(err) {
    if(err) throw err;
    console.log("Connected!")
})