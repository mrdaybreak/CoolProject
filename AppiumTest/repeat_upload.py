from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'baiming'
desired_caps['appActivity'] = 'baomingActivity'
desired_caps['noReset'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(2)


def get_window_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def upload():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '点击录制按钮')
    driver.find_element_by_id('video.like:id/btn_record').click()
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '滑动滤镜')
    l = get_window_size()
    x1 = int(l[0]*0.7)
    x2 = int(l[0]*0.2)
    y1 = int(l[1]*0.5)
    for i in range(15):
        driver.swipe(x1, y1, x2, y1)
        i += 1
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '开始录制')
    driver.find_element_by_id('video.like:id/iv_record_pause').click()
    time.sleep(7)
    driver.tap([(500, 1700)], 500)   # //android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.ViewAnimator[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[2]
    driver.find_element_by_id('video.like:id/iv_finish').click()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '下一步')
    driver.find_element_by_id('video.like:id/iv_btn_right').click()
    driver.find_element_by_id('video.like:id/iv_save_to_phone').click()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '上传')
    driver.find_element_by_id('video.like:id/fl_post').click()
    time.sleep(12)

a = 1
while a < 11:
    upload()
    a += 1