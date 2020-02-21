import requests
import re


class GetImsg():
    def __init__(self, url):
        self.url = url
        self.result = requests.get(self.url).content.decode('utf-8')
        self.result_js = re.findall('<script type="application/json" id="captain-config">(.*?)</script>', self.result)[0].replace('true', 'True')
        print(self.result_js)

    def China(self):
        result_js_load =eval(self.result_js)['component'][0]['summaryDataIn']
        print(result_js_load)
        confirmed = result_js_load['confirmed']
        died = result_js_load['died']
        cured = result_js_load['cured']
        unconfirmed = result_js_load['unconfirmed']
        chinaresult = '<h1 style=color:red>全国累计确认-> %s, 累计死亡-> %s, 累计治愈-> %s, 现有疑似-> %s</h1>' % (confirmed, died, cured, unconfirmed)
        return chinaresult

    def Area(self, area, city):
        result_js_load = eval(self.result_js)['component'][0]["caseList"]
        print(result_js_load)
        acount = 0
        bcount = 0
        for i in range(len(result_js_load)):
            if result_js_load[i]['area'] != area:
                acount += 1
            else:
                print(result_js_load[acount]['area'])
                areaname = result_js_load[acount]['area']
                areaconfirmed = result_js_load[acount]['confirmed']
                areadied = result_js_load[acount]['died']
                areacured = result_js_load[acount]['crued']
                areanewconfirmed = result_js_load[acount]['confirmedRelative']
                for j in range(len(result_js_load[acount]['subList'])):
                    if result_js_load[acount]['subList'][j]['city'] != city:
                        bcount += 1
                    else:
                        print(result_js_load[acount]['subList'][bcount]['city'])
                        cityname = result_js_load[acount]['subList'][bcount]['city']
                        cityconfirmed = result_js_load[acount]['subList'][bcount]['confirmed']
                        citydied = result_js_load[acount]['subList'][bcount]['died']
                        citycured = result_js_load[acount]['subList'][bcount]['crued']
                        citynewconfirmed = result_js_load[acount]['subList'][bcount]['confirmedRelative']
                        arearesult = '<h2 style="color:cadetblue">%s累计确认-> %s, 累计死亡-> %s, 累计治愈-> %s, 新增确诊-> %s, %s累计确认-> %s, 累计死亡-> %s, 累计治愈-> %s, 新增确认-> %s !<h2>' \
                                     % (areaname, areaconfirmed, areadied, areacured, areanewconfirmed, cityname, cityconfirmed, citydied, citycured, citynewconfirmed)
                        return arearesult

