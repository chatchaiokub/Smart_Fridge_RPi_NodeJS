;(function () {
  'use strict'
  var express = require('express')
  var router = express.Router()

  var SUBJECT = 'Ordering Product.'
  var BODYTEXT = ''

  router.post('/setupMail', function (req, res) {
    BODYTEXT = req.body.bodyText
    res.send('success')
  })

  router.get('/setupEgg', function (req, res) {
    var api_key = 'key-b86bc2d406d41485a38a6290e26adde9'
    var domain = 'sandbox340c66c365524888a8427b6a32210046.mailgun.org'
    var mailgun = require('mailgun-js')({apiKey: api_key, domain: domain})
    var data = {
      from: 'Smart-Fridge <postmaster@sandbox340c66c365524888a8427b6a32210046.mailgun.org>',
      to: 'chatty30433@windowslive.com',
      subject: 'Order Buy Eggs',
      text: 'Buy Eggs 1 Dozen'
    }
    mailgun.messages().send(data, function (error, body) {
      console.log(body)
      if (!error) {
        res.send('Mail Send')
      }else {
        res.send('Mail not Send')
      }
    })
  })

  router.get('/setupDrink', function (req, res) {
    var api_key = 'key-b86bc2d406d41485a38a6290e26adde9'
    var domain = 'sandbox340c66c365524888a8427b6a32210046.mailgun.org'
    var mailgun = require('mailgun-js')({apiKey: api_key, domain: domain})
    var data = {
      from: 'Smart-Fridge <postmaster@sandbox340c66c365524888a8427b6a32210046.mailgun.org>',
      to: 'chatty30433@windowslive.com',
      subject: SUBJECT,
      text: BODYTEXT
    }
    mailgun.messages().send(data, function (error, body) {
      console.log(body)
      if (!error) {
        res.send('Mail Send')
      }else {
        res.send('Mail not Send')
      }
    })
  })

  var pack = {}
  router.post('/dataEgg', function (req, res) {
    console.log(req.body)
    pack = req.body.egg
    res.send(req.body.egg)
  })
  router.get('/dataEgg', function (req, res) {
    res.send(pack)
  })

  var PACK = {}
  router.post('/dataDrink', function (req, res) {
    console.log(req.body)
    PACK = req.body.drink
    res.send(req.body.drink)
  })
  router.get('/dataDrink', function (req, res) {
    res.send(PACK)
  })

  module.exports = router
})()
