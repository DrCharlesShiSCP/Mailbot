# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from flask import request
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/api/mailbot')
def hello():
    """Return a friendly HTTP greeting."""
    email = request.args.get('email')

    # Logic to select receipient
    # # TODO:

    my_sender='pythondistributionbot@gmail.com'    # Sender Mail
    my_pass = 'czwcekimsscsixzx'              # Sender PW
    my_user='drcharlesshi@gmail.com'      # Reciver Mail
    try:
        msg=MIMEText('填写邮件内容','plain','utf-8')
        msg['From']=formataddr(["FromRunoob",my_sender])  # Sender Nick/mail
        msg['To']=formataddr(["FK",email])              # Reciver Nike/Mail
        msg['Subject']="发送邮件测试"                # Topic

        server=smtplib.SMTP_SSL("smtp.gmail.com", 465)  # SMTP，port 465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        return 'Failure ' + request.args.get('email')
    return 'Success ' +


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
