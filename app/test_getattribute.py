# -*- coding: utf-8 -*-
# Author By Jone xie
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By


class TestGetAttr:

    def setup(self):
        desired_cap = {
            "automationName": 'uiautomator2',
            "platformName": "android",
            "platformVersion": "9",
            "deviceName": "7825d7bc",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # 是否测试后重置app
            "noReset": True,
            # 不停止app
            "dontStopAppOnReset": True,
            # 跳过初始化
            "skipDeviceInitialization": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True

        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    # self.driver.quit()

    def test_get_attr(self):
        el1 = self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search")
        print(el1.get_attribute("content-desc"))
