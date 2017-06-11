;(function () {
  'use strict'
  var express = require('express')
  var router = express.Router()

  var SUBJECT = 'Order Buy Drink.'
  var BODYTEXT = ''

  router.post('/setupMail', function (req, res) {
    BODYTEXT = req.body.bodyText
    res.send('success')
  })
  router.get('/setupEgg', function (req, res) {
    var nodemailer = require('nodemailer')
    var smtpTransport = require('nodemailer-smtp-transport')
    var transport = nodemailer.createTransport(smtpTransport({
      service: 'gmail',
      auth: {
        user: '5606021612065@fitm.kmutnb.ac.th', // my mail
        pass: 'anachakfitmokub@31'
      }
    }))
    var mailOptions = {
      from: '5606021612065@fitm.kmutnb.ac.th',
      to: 'chatty30433@windowslive.com',
      subject: 'Order Buy Eggs',
      text: 'Buy Eggs 1 Dozen'
    }
    transport.sendMail(mailOptions, function (error, info) {
      if (error) {
        console.log(error)
        res.send('Mail Not Send')
      } else {
        console.log('Email sent: ' + info.response)
        res.send('Mail Send')
      }
    })
  })
  router.get('/setupDrink', function (req, res) {
    var nodemailer = require('nodemailer')
    var smtpTransport = require('nodemailer-smtp-transport')
    var transport = nodemailer.createTransport(smtpTransport({
      service: 'gmail',
      auth: {
        user: '5606021612065@fitm.kmutnb.ac.th', // my mail
        pass: 'anachakfitmokub@31'
      }
    }))
    var mailOptions = {
      from: '5606021612065@fitm.kmutnb.ac.th',
      to: 'chatty30433@windowslive.com',
      subject: SUBJECT,
      text: BODYTEXT+'12 bottols'
    }
    transport.sendMail(mailOptions, function (error, info) {
      if (error) {
        console.log(error)
        res.send('Mail Not Send')
      } else {
        console.log('Email sent: ' + info.response)
        res.send('Mail Send')
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
