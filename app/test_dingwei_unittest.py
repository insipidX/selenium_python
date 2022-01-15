# -*- coding: utf-8 -*-
# Author By Jone xie
from appium import webdriver
from selenium.webdriver.common.by import By

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
    "skipDeviceInitialization": True,
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
el1 = driver.find_element(By.ID, "com.xueqiu.android:id/home_search")
el1.click()
el2 = driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
el2.click()
el2.send_keys("阿里巴巴")
driver.back()
driver.back()
