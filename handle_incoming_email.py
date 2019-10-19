#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import logging

from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
import webapp2

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def find_best_match_email(mail_message):

    return "foo@yahoo.com"

class LogSenderHandler(InboundMailHandler):
    def receive(self, mail_message):

        # ML stuff
        email = find_best_match_email(mail_message)

        my_sender='pythondistributionbot@gmail.com'    # Sender Mail
        my_pass = 'czwcekimsscsixzx'              # Sender PW
        my_user='drcharlesshi@gmail.com'      # Reciver Mail
        email = my_user
        try:
            msg=MIMEText(context,'plain','utf-8')
            msg['From']=formataddr([sender,my_sender])  # Sender Nick/mail
            msg['To']=formataddr([receipient,email])              # Reciver Nike/Mail
            msg['Subject']=Topic                # Topic

            server=smtplib.SMTP_SSL("smtp.gmail.com", 465)  # SMTP，port 465
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception, e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            logging.info("Failure from:" + mail_message.sender + " Exception: " + str(e))
            raise
        logging.info("Success from:" + mail_message.sender)

app = webapp2.WSGIApplication([LogSenderHandler.mapping()], debug=True)
