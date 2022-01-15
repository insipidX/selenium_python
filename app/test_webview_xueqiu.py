# -*- coding: utf-8 -*-
# Author By Jone xie
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
# from webview.webview import WebView
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWebviewXQ:

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
        # WebView.setWebContentsDebuggingEnabled(True)

    def teardown(self):
        self.driver.quit()
        sleep(3)

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()
        # 打印当前页面属性
        print(self.driver.contexts)  # ['NATIVE_APP', 'WEBVIEW_com.xueqiu.android']
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 打印当前页窗口句柄
        print(self.driver.window_handles)  # ['CDwindow-4ED7D986998EF22B048A9A67B7AB5F30', 'CDwindow-65E8CD247AD73C0EECDDA88C0CCEDF31', 'CDwindow-03D83D5FB7D6FDFF211F6478142EBBF3']
        kaihu_locator = (MobileBy.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div[1]/div[2]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(kaihu_locator))
        self.driver.find_element(*kaihu_locator).click()
        print(self.driver.contexts)  # ['NATIVE_APP', 'WEBVIEW_com.xueqiu.android']
        print(self.driver.window_handles)  # ['CDwindow-4ED7D986998EF22B048A9A67B7AB5F30', 'CDwindow-65E8CD247AD73C0EECDDA88C0CCEDF31', 'CDwindow-03D83D5FB7D6FDFF211F6478142EBBF3', 'CDwindow-DEFFD47194198C7DEE04CAD212CC22EB']

        # 切换窗口，-1为最新窗口
        kaihu_window = self.driver.window_handles[-1]

        self.driver.switch_to.window(kaihu_window)
        self.driver.find_element(MobileBy.ID, 'phone-number').send_keys(13126003896)
        self.driver.find_element(MobileBy.ID, 'code').send_keys(123456)
