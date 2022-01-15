# -*- coding: utf-8 -*-
# Author By Jone xie
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.common.by import By
# from webview.webview import WebView
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.connectiontype import ConnectionType



class TestJiaoHu:

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
            "resetKeyboard": True,
            # 自动设置权限
            "autoGrantPermissions": True

        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(10)
        # WebView.setWebContentsDebuggingEnabled(True)

    def teardown(self):
        self.driver.quit()
        sleep(3)

    def test_jiaohu(self):
        # 模拟器才能使用
        # self.driver.make_gsm_call('13126003896', GsmCallActions.CALL)
        # self.driver.send_sms('13126003896', 'hello')

        self.driver.set_network_connection(2)
        sleep(3)
        self.driver.get_screenshot_as_file('./photo/1.png')
        print(self.driver.network_connection)
        self.driver.set_network_connection(4)
        print(self.driver.network_connection)

