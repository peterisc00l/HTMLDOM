var http = require('http');

http.createServer(function (req, res) {
    res.write('This is my first activity in Node.js');
    res.end();
}).listen(8080);