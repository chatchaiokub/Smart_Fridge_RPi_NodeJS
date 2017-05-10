;(function () {
  'use strict'
  var express = require('express')
  var PythonShell = require('python-shell')
  var router = express.Router()

  router.get('/ledAlertON', function (req, res) {
    PythonShell.run('ledOn.py', function (err) {
      if (err) { res.send(err) }
      else res.send({message: 'done'})
    })
  })
  router.get('/ledAlertOFF', function (req, res) {
    PythonShell.run('ledOff.py', function (err) {
      if (err) { res.send(err) }
      else res.send({message: 'done'})
    })
  })
  module.exports = router
})()
