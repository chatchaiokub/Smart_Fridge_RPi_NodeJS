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

  // router.get('/setupEgg', function (req, res) {
  //   var api_key = 'key-087ab4313404c2df9dab775cb3d0ecb9'
  //   var domain = 'sandboxbbf5cfe12b8741589ab71636de046655.mailgun.org'
  //   var mailgun = require('mailgun-js')({apiKey: api_key, domain: domain})
  //   var data = {
  //     from: 'Smart-FridgeC <postmaster@sandboxbbf5cfe12b8741589ab71636de046655.mailgun.org>',
  //     to: 'chatty30433@windowslive.com',
  //     subject: 'Order Buy Eggs',
  //     text: 'Buy Eggs 1 Dozen'
  //   }
  //   mailgun.messages().send(data, function (error, body) {
  //     console.log(body)
  //     if (!error) {
  //       res.send('Mail Send')
  //     }else {
  //       res.send('Mail not Send')
  //     }
  //   })
  // })
  router.get('/setupEgg', function (req, res) {
    var nodemailer = require('nodemailer')
    var transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: '5606021612065@fitm.kmutnb.ac.th',
        pass: 'anachakfitmokub@31'
      }
    })
    var mailOptions = {
      from: '5606021612065@fitm.kmutnb.ac.th',
      to: 'chatty30433@windowslive.com',
      subject: 'Sending Email using Node.js',
      text: 'That was easy!'
    }
    transporter.sendMail(mailOptions, function (error, info) {
      if (error) {
        console.log(error)
      } else {
        console.log('Email sent: ' + info.response)
      }
    })
    // var helper = require('sendgrid').mail
    // var fromEmail = new helper.Email('5606021612065@fitm.kmutnb.ac.th')
    // var toEmail = new helper.Email('chatty30433@windowslive.com')
    // var subject = 'Sending with SendGrid is Fun'
    // var content = new helper.Content('text/plain', 'and easy to do anywhere, even with Node.js')
    // var mail = new helper.Mail(fromEmail, subject, toEmail, content)
    // var sg = require('sendgrid')(process.env.SENDGRID_API_KEY)
    // var request = sg.emptyRequest({
    //   method: 'POST',
    //   path: '/v3/mail/send',
    //   body: mail.toJSON()
    // })
    // sg.API(request, function (error, response) {
    //   if (error) {
    //     console.log('Error response received')
    //   }
    //   console.log(response.statusCode)
    //   console.log(response.body)
    //   console.log(response.headers)
    // })
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
