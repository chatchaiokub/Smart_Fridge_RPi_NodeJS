var sendgrid = require("sendgrid")("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");
var email = new sendgrid.Email();

email.addTo("chatty30433@windowslive.com");
email.setFrom("5606021612065@fitm.kmutnb.ac.th");
email.setSubject("Sending with SendGrid is Fun");
email.setHtml("and easy to do anywhere, even with Node.js");

sendgrid.send(email);
