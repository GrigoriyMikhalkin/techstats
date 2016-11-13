var express = require('express');
var path = require('path');

var index = require('./frontend/index');

var port = 3000;
var app = express();


//View Engine
app.set('views', path.join(__dirname, 'frontend'));
app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);


// Set static folder
app.use(express.static(path.join(__dirname, 'client')));


app.use('/', index);


app.listen(port, finction () {
    console.log('Server started on port' + port);
});
