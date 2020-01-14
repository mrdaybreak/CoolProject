from selenium import webdriver
import os
import time
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains
import http.client
import json
import ssl

broswer = webdriver.Chrome()

broswer.find_element_by_id("submit").click()
broswer.implicitly_wait(20)


def click_element(element):
    source = broswer.find_element_by_css_selector("{}".format(element))
    ActionChains(broswer).move_to_element(source).click().perform()
    time.sleep(1)


def select_name(excel_name):
    wb = openpyxl.load_workbook(excel_name, read_only=True)

    sheet = wb.active
    nowork = []
    shouldwork = []

    for i in range(1, 800):
        if sheet["O{}".format(i)].value is not None:
            if sheet["O{}".format(i)].value == '已解决':
                nowork.append((str(sheet["A{}".format(i)].value) + "-->" + sheet["T{}".format(i)].value))
            elif sheet["O{}".format(i)].value == '激活':
                shouldwork.append((str(sheet["A{}".format(i)].value) + "-->" + sheet["T{}".format(i)].value))
        else:
            break
    # print(nowork)
    # print(shouldwork)
    return nowork, shouldwork


def clicking():
    try:
        os.remove("/Users/lingchen/Downloads/like-Bug.xlsx")
        os.remove("/Users/lingchen/Downloads/like-Bug (1).xlsx")
    except FileNotFoundError:
        pass
    # 第一个选择框
    click_element("#field1_chosen > a > span")
    js = "var q=document.documentElement.scrollTop=1000"
    broswer.execute_script(js)
    time.sleep(1)
    # 选中项目
    click_element("#field1_chosen > div > ul > li:nth-child(12)")
    # 第一个选择框的value
    click_element("#value1_chosen > a > span")
    # 选中Android项目
    click_element("#value1_chosen > div > ul > li:nth-child(3)")

    # 第二个选择框
    click_element("#field4_chosen > a > span")
    js2 = "var q=document.documentElement.scrollTop=1000"
    broswer.execute_script(js2)
    time.sleep(1)
    # 选中严重程度
    click_element("#field4_chosen > div > ul > li:nth-child(13)")
    # 选择<=
    click_element("#operator4")
    click_element("#operator4 > option:nth-child(6)")
    # 选中第二个选择框的value
    click_element("#value4_chosen > a > span")
    # 选中2级
    click_element("#value4_chosen > div > ul > li:nth-child(2)")
    # 点击搜索
    broswer.find_element_by_css_selector("#submit").click()
    broswer.implicitly_wait(20)
    # 点击导出数据
    click_element("#mainMenu > div.btn-toolbar.pull-right > div > button")
    click_element("#exportActionMenu > li:nth-child(1) > a")
    broswer.implicitly_wait(20)
    # 转换iframe点击导出
    iframe = broswer.find_element_by_id("iframe-triggerModal")
    broswer.switch_to.frame(iframe)
    click_element("#submit")
    broswer.implicitly_wait(10)

    # 选中ios项目
    # 第一个选择框的value
    broswer.switch_to.default_content()
    click_element("#value1_chosen > a > span")
    click_element("#value1_chosen > div > ul > li:nth-child(2)")
    # 点击搜索
    broswer.find_element_by_css_selector("#submit").click()
    broswer.implicitly_wait(20)
    # 点击导出数据
    click_element("#mainMenu > div.btn-toolbar.pull-right > div > button")
    click_element("#exportActionMenu > li:nth-child(1) > a")
    broswer.implicitly_wait(20)
    # 转换iframe点击导出
    iframe = broswer.find_element_by_id("iframe-triggerModal")
    broswer.switch_to.frame(iframe)
    click_element("#submit")
    time.sleep(7)
    broswer.close()


def send_message(program_name, excel_name):
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {"Content-Type": "application/json", "Accept": "text/plain"}
    nowork, shouldwork = select_name(excel_name)
    if nowork != [] and shouldwork != []:
        done = str(nowork).replace(',', ',\n')
        active = str(shouldwork).replace(',', ',\n')
        params_notice = json.dumps({"msgtype": "markdown",
                                    "markdown": {
                                        "content": "%s以下这些<font color=\"warning\">Bug</font>麻烦大佬们验证和留意下。\n>需要验证:<font color=\"comment\">%s</font> \n>\n需要提醒开发:<font color=\"comment\">%s</font>" % (
                                        program_name, done, active)}}, ensure_ascii=False).encode('utf-8')
        conn2 = http.client.HTTPSConnection("qyapi.weixin.qq.com")
        conn2.request('POST', '/cgi-bin/webhook/send?key=fd524bb1-1866-40fe-a082-fd208d9f1eaf', params_notice, headers)
    else:
        pass


clicking()
send_message("Android", "/Users/lingchen/Downloads/like-Bug.xlsx")
send_message("IOS", "/Users/lingchen/Downloads/like-Bug (1).xlsx")
