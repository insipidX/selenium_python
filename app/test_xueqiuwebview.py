# -*- coding: utf-8 -*-
# File:test-xueqiuwebview.py
# Author:Jone xie
# Date:2022/3/1 23:12


import os

from appium import webdriver
from selenium.webdriver.common.by import By




def test_webview():
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
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,"//[@text='交易']").click()
    webview = driver.context[-1]
    performace = driver.execute_script("return window.performance.timing")
   # print(performace[''])
