// Assignment 1

const express = require('express');

const app = express();



app.set('view engine', 'pug');

router.get('/hello', (req, res) => {
    res.send("hi man");
});

app.listen(3000, () => {
    console.log("The application is running on localhost:3000.");
});

// Asignment 2

const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

const app = express();

app.use(bodyParser.urlencoded({ extended: false}));
app.use(cookieParser());

app.set('view engine', 'pug');

app.get('/getData', (req, res) => {
    const num = req.query.number;
    if (num == 5) {
        const result = calcNum(num);
    }
        else (num !== undefined) {
        res.send(result.toString());
        else{
            res.send("wrong parameter");
        }
    }
    else{
        res.send("lack of parameter");
    }
});

function calcNum(num){
    const result = 0;
    for (i = 1; i <= num ; i++) {
        result += i;
    }
    return result;
}

// Asignment 3
const express = require('express');
const app = express();
app.set('view engine', 'pug');

app.use(express.static('assignment'));

app.listen(3000, () => {
    console.log("The application is running on localhost:3000.");
});

// Asignment 4
const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

const app = express();

app.use(bodyParser.urlencoded({ extended: false}));
app.use(cookieParser());

app.set('view engine', 'pug');

app.get('/myName', (req, res) => {
    const name = req.cookies.username;
    if (name) {
        res.render('hi2', { "name" : name.toString()});
    } else {
        res.render('index');
    }
});

app.get('/hello2', (req, res) => {
    const name = req.query.username;
    if (name !== undefined) {
        res.cookie('name', name);
        res.redirect('myName');
    } else {
        res.render('index');
    }
});

app.listen(3000, () => {
    console.log("The application is running on localhost:3000.");
});












/*
//for card1, just for fun
const colors = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple'
  ];
const mainRoutes = require('./routes/index');
const cardRoutes = require('./routes/cards');
app.use(mainRoutes);
app.use('/cards', cardRoutes);
app.use((req, res, next) => {
    const err = new Error('Not Found');
    err.status = 404;
    next(err);
});
app.use((err, req, res, next) => {
    res.locals.error = err;
    res.status(err.status);
    res.render('error');
});
//back-end footer
app.listen(3000, () => {
    console.log('The appl is runnong on localhotst:300-')
});
*/

