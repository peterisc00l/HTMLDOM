var fs = require('fs');

fs.unlink('afile2.txt', function (err) {
    if (err) throw err;
    console.log('File deleted!')
})