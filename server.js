var express = require('express')
var bodyParser = require('body-parser')
var mongoose = require('mongoose')
var snap = require('./models/snap/snap.route.js')
var db = require('./models/db/db.route.js')
var freezer = require('./models/freezer/freezer.route.js')
var setupMail = require('./models/setupMail/setupMail.route.js')
var PythonShell = require('python-shell')
var cors = require('cors')
var app = express()

// mongoose.connect('mongodb://fridge:fridge@ds133348.mlab.com:33348/smart-fridge')
mongoose.connect('mongodb://localhost/smart-fridge')

app.use(cors())
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.static('public'))
app.use('/', snap)
app.use('/', db)
app.use('/', freezer)
app.use('/', setupMail)

app.get('/ledAlertON', function (req, res) {
  PythonShell.run('ledOn.py', function (err) {
    if (err) { res.send(err) }
    else res.send({message: 'done'})
  })
})
app.get('/ledAlertOFF', function (req, res) {
  PythonShell.run('ledOff.py', function (err) {
    if (err) { res.send(err) }
    else res.send({message: 'done'})
  })
})
app.post('/dataegg', function (req, res) {
 console.log(req.body)
 res.send(req.body)
})

app.listen(3000)
console.log('running on port 3000.')
