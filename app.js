var fs = require('fs');

fs.writeFile('afile.txt', 'hello my name is Peter and i am 11yrs old',
    function (err) {
        if (err) throw err;
        console.log('Content changed!');
});