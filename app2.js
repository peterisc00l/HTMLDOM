var fs = require('fs');

fs.rename('arandomfile.txt', 'anewfile2.txt', function (err) {
    if (err) throw err;
    console.log('File has been newly renamed!');
});