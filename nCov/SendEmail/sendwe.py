import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SM:
    def __init__(self, sender, receiver, password, message):
        self.sender = sender
        self.receiver = receiver
        self.password = password
        self.message = message

    def sendEmail(self):
        content = MIMEText(self.message, 'html', 'utf-8')
        subject = '每日一发-疫情进展'
        content['Subject'] = Header(subject, 'utf-8')
        content['From'] = Header('LingChen', 'utf-8')
        smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtp.login(self.sender, self.password)
        smtp.sendmail(self.sender, self.receiver, content.as_string())
        smtp.quit()
