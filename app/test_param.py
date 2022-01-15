# -*- coding: utf-8 -*-
# Author By Jone xie

from time import sleep

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from hamcrest import *


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
        self.driver.find_element(By.ID, "com.xueqiu.android:id/action_close").click()
        # pass
        # self.driver.quit()

    # 搜索并返回股价是否大于100
    @pytest.mark.parametrize('searchkey, type_key, expect_price', [
        ('alibaba', 'BABA', 110),
        ('xiaomi', '01810', 20)

    ])
    def test_search(self, searchkey, type_key, expect_price):
        self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search").click()
        el1 = self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        # el1.click()
        # el1.send_keys(searchkey)
        self.driver.find_element(By.ID, "com.xueqiu.android:id/name").click()
        sleep(3)
        price = self.driver.find_element(By.XPATH,
                                         f"//*[@text='{type_key}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price = float(price.text)
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
