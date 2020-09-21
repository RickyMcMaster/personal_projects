var express = require('express');
var app = express();
var mysql = require('mysql');
var bodyParser = require('body-parser');

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(express.static(__dirname + "/public"));

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root', //your username
    database: 'join_us', //the name of your db
    password: process.env.MYSQL_PW
});



app.get("/", function (req, res) {
    //  res.send("HELLO FROM OUR WEB APP!");
    var q = 'SELECT COUNT(*) AS total FROM users ';
    var cnt = connection.query(q, function (error, results) {
        if (error) throw error;
        var cnt = results[0].total;
        // res.send("We have " + cnt + " users in our database.")
        res.render('home', {
            data: cnt
        })
    });
});





app.post("/register", function (req, res) {
    console.log("POST REQUEST SENT TO /REGISTER email is " + req.body.email);
    // var email = 
    var person = {
        email: req.body.email
    };
    var end_result = connection.query('INSERT INTO users SET ?', person, function (err, result) {
        if (err) throw err;
        console.log(result);
        res.redirect("/");
    });

});

app.get("/joke", function (req, res) {
    res.send("<strong>What do you call a dog that does magic tricks?</strong>  <em>A Labracadabrador.</em>")
});

app.get("/random_num", function (req, res) {
    var num = Math.floor((Math.random() * 10) + 1);
    res.send("Your lucky number is " + num);
});

app.listen(8080, function () {
    console.log('App listening on port 8080!');
});