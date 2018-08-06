#!/usr/bin/python3
import smtplib

sender = 'archivefargo@here.com'
receivers = ['bill.royce@here.com']

message = """From: archive <archivefargo@here.com>
To: William Royce <bill.royce@here.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""
try:
   smtpObj = smtplib.SMTP('smtp.in.here.com')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"