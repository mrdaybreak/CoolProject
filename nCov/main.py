from case import DayAdd
from log.savelog import logs
import json
from SendEmail import sendwe
from SendEmail.emailimage import line
import sqlite3
conn = sqlite3.connect("DayAdd.db")
c = conn.cursor()
try:
    c.execute("create table nCovchina"
              "(confirmed int default 0, unconfirmed int default 0, "
              "otime timestamp default (datetime('now')))")
except:
    pass

with open('nCov/url/baidu.json') as wj:
    text = json.loads(wj.read())
    url = text['url']
    area = text['area']
    citya = text['citya']
    cityb = text['cityb']
A = DayAdd.GetImsg(url)
a = '<h1 style=color:red>全国累计确认-> %s, 累计死亡-> %s, 累计治愈-> %s, 现有疑似-> %s</h1>' % (A.China()[0], A.China()[1], A.China()[2], A.China()[3])
b = A.Area(area, citya)
ca = A.Area(area, cityb)
c.execute("insert into nCovchina (confirmed, unconfirmed) values ({}, {})".format(int(A.China()[0]), int(A.China()[3])))
conn.commit()
y = list(c.execute("select confirmed from nCovchina"))
x = [i[0] for i in list(c.execute("select otime from nCovchina"))]
print(y)
imgpath = line(x, y)
print(imgpath)
sendtext = a+b+ca
ac = logs("main")
ac.info(sendtext)
sm = sendwe.SM('3180966941@qq.com', '289140347@qq.com', 'sgfmmvitbhraddca', sendtext, imgpath)
sm.sendEmail()
conn.close()