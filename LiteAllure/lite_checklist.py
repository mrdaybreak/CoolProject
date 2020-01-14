import pytest
from liteMethod import *
from liteElement import *
import time
import os
import sys
import uiautomator2.exceptions as e
nametime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
d = u2.connect('192.168.31.41')


def setup_module():
    d.app_start("video.like.lite", "video.like.lite.ui.home.HomeActivity")
    liteMethod.idclick(newClose())
    d.set_fastinput_ime(True)


@allure.story("登陆")
def test_login():
    if d(resourceId="video.like.lite:id/iv_coin").exists:
        liteMethod.idclick(people())
    else:
        liteMethod.idclick(avatar())
    liteMethod.idclick(selectcountry())
    liteMethod.sendkey(inputcountry(), 'china')
    liteMethod.idclick(firstcountry())
    liteMethod.sendkey(phone(), '1xxx')
    liteMethod.idclick(loginnextstep())
    liteMethod.sendkey(inputpassword(), 'axxx')
    liteMethod.idclick(login())


@allure.story("上下滑动视频")
def test_switchvideo():
    liteMethod.idclick(firstvideo())
    for i in range(10):
        liteMethod.upswipe()
        time.sleep(2)


@allure.story("视频详情页操作")
def test_videooperation():
    liteMethod.idclick(detailfollow())
    liteMethod.idclick(detaillike())
    liteMethod.sendkey(detailwaicomment(), "good")
    liteMethod.idclick(detailwaiat())
    liteMethod.idclick(firstat())
    liteMethod.idclick(detailwaiemoji())
    liteMethod.idclick(firstemoji())
    liteMethod.idclick(detailwaisent())
    liteMethod.idclick(detailincomment())
    liteMethod.sendkey(detailwaicomment(), "goodtoo")
    liteMethod.idclick(detailwaiat())
    liteMethod.idclick(firstat())
    liteMethod.idclick(detailwaiemoji())
    liteMethod.idclick(firstemoji())
    liteMethod.idclick(detailwaisent())
    liteMethod.back()
    liteMethod.back()
    liteMethod.back()


@allure.story("退出登陆")
def test_logout():
    liteMethod.idclick(avatar())
    liteMethod.idclick(setting())
    liteMethod.idclick(logout())
    liteMethod.idclick(logoutsure())


@allure.story("任务页")
def test_task():
    liteMethod.idclick(taskentrance())


def teardown_module():
    d.app_stop_all()


if __name__ == '__main__':
    pytest.main(['-s', '-v', '--alluredir', './report/{}'.format(nametime), "{}".format(os.path.basename(__file__))])
    os.system('/Users/lingchen/Downloads/allure-2.13.0/bin/allure generate ./report/{} -o ./report/html/{}'.format(nametime,
                                                                                                             nametime))
