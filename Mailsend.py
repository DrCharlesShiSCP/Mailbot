#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender='pythondistributionbot@gmail.com'    # Sender Mail
my_pass = 'czwcekimsscsixzx'              # Sender PW
my_user='drcharlesshi@gmail.com'      # Reciver Mail
def mail():
    ret=True
    try:
        msg=MIMEText('填写邮件内容','plain','utf-8')
        msg['From']=formataddr(["FromRunoob",my_sender])  # Sender Nick/mail
        msg['To']=formataddr(["FK",my_user])              # Reciver Nike/Mail
        msg['Subject']="发送邮件测试"                # Topic

        server=smtplib.SMTP_SSL("smtp.gmail.com", 465)  # SMTP，port 465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret

ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
