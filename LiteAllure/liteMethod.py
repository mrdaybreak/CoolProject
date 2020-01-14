import uiautomator2 as u2
import allure
import time
from lite_checklist import d

height = float(d.info['displayHeight'])
width = float(d.info['displayWidth'])


def screen():
    nametime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    pic = "./screenshot/{}.jpg".format(nametime)
    time.sleep(0.5)
    d.screenshot(pic)
    file = open(pic, 'rb').read()
    allure.attach(file, "截图", allure.attachment_type.JPG)


class liteMethod():
    @staticmethod
    def idclick(ele):
        with allure.step("{}".format(ele[0])):
            d(resourceId='{}'.format(ele[1])).click()
            screen()

    @classmethod
    def xpathclick(cls, ele):
        with allure.step("{}".format(ele[0])):
            d.xpath('{}'.format(ele[1])).click()
            screen()

    @classmethod
    def lelfwipe(cls):
        with allure.step("左滑"):
            d.swipe(width*0.7, height/2, width*0.2, height/2)
            screen()

    @classmethod
    def rightwipe(cls):
        with allure.step("右滑"):
            d.swipe(width * 0.2, height / 2, width * 0.7, height / 2)
            screen()

    @classmethod
    def downswipe(cls):
        with allure.step("下滑"):
            d.swipe(width/2, height*0.2, width/2, height*0.7)
            screen()

    @classmethod
    def upswipe(cls):
        with allure.step("上滑"):
            d.swipe(width / 2, height * 0.7, width / 2, height * 0.2)
            screen()

    @classmethod
    def sendkey(cls, ele, keys):
        with allure.step("{}".format(ele[0])):
            d(resourceId='{}'.format(ele[1])).clear_text()
            d(resourceId='{}'.format(ele[1])).send_keys(keys)
            screen()

    @classmethod
    def back(cls):
        d.press("back")
        screen()

    @classmethod
    def home(cls):
        d.press("home")
        screen()




