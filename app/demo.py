# -*- coding: utf-8 -*-
# Author By Jone xie
from appium import webdriver
import time
from appium.webdriver.common.mobileby import MobileBy


class TestWebView:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "9",
            "deviceName": "7825d7bc",
            "browserName": "Chrome",
            "chromeOptions": {"w3c": False},
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_browser(self):
        self.driver.get("https://www.baidu.com/")
        print(self.driver.contexts)  # ['NATIVE_APP', 'CHROMIUM']
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID, "index-kw").send_keys("appium webview测试")
        self.driver.find_element(MobileBy.ID, "index-bn").click()
