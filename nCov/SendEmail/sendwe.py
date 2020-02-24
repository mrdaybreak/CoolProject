import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SM:
    def __init__(self, sender, receiver, password, message, imgpath):
        self.sender = sender
        self.receiver = receiver
        self.password = password
        self.message = message
        self.imgpath = imgpath

    def sendEmail(self):
        msgtext = MIMEText(self.message + '''<table><tr><td><img src="cid:ache"></td></tr></table>''', 'html', 'utf-8')
        msgAlternative = MIMEMultipart('alternative')
        content = MIMEMultipart('related')
        content.attach(msgAlternative)
        msgAlternative.attach(msgtext)
        with open(self.imgpath, "rb") as ig:
            msgimg = MIMEImage(ig.read())
        msgimg.add_header('Content-ID', 'ache')
        content.attach(msgimg)
        subject = '每日一发-疫情进展'
        content['Subject'] = Header(subject, 'utf-8')
        content['From'] = Header('LingChen', 'utf-8')
        smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtp.login(self.sender, self.password)
        smtp.sendmail(self.sender, self.receiver, content.as_string())
        smtp.quit()


