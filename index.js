var mysql = require('mysql');

var connection = mysql.createConnection({
    host:"remotemysql.com",
    user:"Rz8hqn1dk4",
    password:"nd0WKO3xeO",
    database:"Rz8hqn1dk4"
});
connection.connect((err)=>{
    if(err) throw err
    console.log("connected!");
    var sql = "INSERT INTO(Student_ID,Student_FirstName,Student_LastName,Student_City,Student_Grade) VALUES ?";
    var values = [
        [101,'Teenu','Parshant','Madurai','5'],
        [101,'Chintu','Prakash','Chennai','6'],
        [101,'caral','Smith','Texas','2'],
        [101,'Riya','Gupta','Pune','9'],
        [101,'Teka','Parshant','Banglore','8'],
    ];
connection.query(sql,[values],function(err,result){
    if(err) throw err;
    console.log("Multiple Data inserted in DB");
});
});