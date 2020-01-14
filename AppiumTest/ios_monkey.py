import numpy as np
from appium import webdriver
import time
import logging
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {}
desired_caps['platformName'] = 'ios'
desired_caps['platformVersion'] = '12.1'
desired_caps['deviceName'] = 'iphone'
desired_caps['udid'] = 'e07e9028f89bd759e05bdb3596c5f70a1e76595f'
desired_caps['bundleId'] = 'booming'
desired_caps['noReset'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

logging.debug('进入录制')
driver.find_element_by_accessibility_id('videoEntryBtn').click()
driver.find_element_by_accessibility_id('ic beauty color').click()


def get_window_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)


def swipe():
    l = get_window_size()
    x1 = np.random.randint(1, l[0])
    y1 = int(l[1]*0.8)
    x2 = np.random.randint(1, l[0])
    driver.swipe(x1, y1, x2, y1, 500)
    time.sleep(1)


def count():
    for i in range(200):
        print(i)
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        a = np.random.randint(1, x)
        b = np.random.randint(int(y * 0.7), y)
        TouchAction(driver).tap(x=a, y=b).perform().release()
        swipe()

    for i2 in range(200):
        print(i2)
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        a = np.random.randint(1, x)
        b = np.random.randint(1, y)
        TouchAction(driver).tap(x=a, y=b).perform().release()
        swipe()


if __name__ == '__main__':
    count()


