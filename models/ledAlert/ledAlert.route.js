;(function () {
  'use strict'
  var express = require('express')
  var PythonShell = require('python-shell')
  var router = express.Router()

  router.get('/ledAlertON', function (req, res) {
    PythonShell.run('ledOn.py', function (err) {
      if (err) { res.send(err) }
      else res.send('ledAlert ON')
    })
  })
  router.get('/Alertexpire', function (req, res) {
    PythonShell.run('Alertexpire.py', function (err) {
      if (err) { res.send(err) }
      else res.send('Line send success')
    })
  })
  router.get('/ledAlertOFF', function (req, res) {
    PythonShell.run('ledOff.py', function (err) {
      if (err) { res.send(err) }
      else res.send('ledAlert OFF')
    })
  })
  module.exports = router
})()
