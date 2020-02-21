from case import DayAdd
from log.savelog import logs
import json
from SendEmail import sendwe

with open('nCov/url/baidu.json') as wj:
    text = json.loads(wj.read())
    url = text['url']
    area = text['area']
    citya = text['citya']
    cityb = text['cityb']
A = DayAdd.GetImsg(url)
a = A.China()
b = A.Area(area, citya)
c = A.Area(area, cityb)
sendtext = a+b+c
ac = logs("main")
ac.info(sendtext)
sm = sendwe.SM('3180966941@qq.com', '289140347@qq.com', 'sgfmmvitbhraddca', sendtext)
sm.sendEmail()
