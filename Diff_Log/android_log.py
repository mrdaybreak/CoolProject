import smtplib
from email.mime.text import MIMEText
from email.header import Header
import difflib
import time
import os


class LogFiff(object):

    def __init__(self, path, nowtime):
        self.path = path
        self.nowtime = nowtime

    def read_file(self):
        path1 = self.path + '/correct_log/'
        path2 = self.path + '/to_diff_log/'
        text_a = open(path1 + os.listdir(path1)[0]).readlines()
        text_b = open(path2 + os.listdir(path2)[0]).readlines()
        diff_rs = difflib.HtmlDiff()
        diff_result = diff_rs.make_file(text_a, text_b, context=True)
        return diff_result

    def send_email(self):
        sender = 'sender@qq.com'
        password = 'pwd'
        receivers = 'receiver@qq.com'
        mail_msg = LogFiff.read_file(self)
        with open(self.nowtime + '_result.html', 'w') as writein:
            writein.write(mail_msg)
        message = MIMEText(mail_msg, 'html', 'utf-8')
        subject = self.nowtime + '_log测试'
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = Header('python_autotest', 'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
            smtpObj.login(sender, password)
            smtpObj.sendmail(sender, receivers,  message.as_string())
            smtpObj.quit()
        except smtplib.SMTPException:
            print('error')


if __name__ == '__main__':
    path = os.getcwd()
    nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    s = LogFiff(path, nowtime)
    s.send_email()