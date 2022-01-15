# -*- coding: utf-8 -*-
# Author By Jone xie
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:

    def setup(self):
        desired_capabilities = {
            "automationName": 'uiautomator2',
            "platformName": "android",
            "platformVersion": "9",
            "deviceName": "7825d7bc",
            # "deviceName": "57147944",
            "browserName": "Chrome",
            # 是否测试后重置app
            "noReset": True,
            # 不停止app
            "dontStopAppOnReset": True,
            "chromeOptions": {"w3c": False},
            # # 跳过初始化
            # "skipDeviceInitialization": True,
            # "unicodeKeyboard": True,
            # "resetKeyboard": True

        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # pass
        sleep(3)
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://baidu.com")
        print(self.driver.contexts)  # ['NATIVE_APP', 'CHROMIUM']
        self.driver.switch_to.context(self.driver.contexts[-1])
        sleep(3)
        # 无法点击，可以直接发送参数
        self.driver.find_element(By.ID, "index-kw").send_keys("appium webview测试")
        self.driver.find_element(By.ID, "index-bn").click()

        # search_locat = (By.ID, "index-kw")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(search_locat))
        # # self.driver.find_element(By.XPATH, "//*[@id='index-kw']").click()
        # self.driver.find_element(*search_locat).click()
        # # self.driver.find_element(By.ID, 'index-kw')
        # self.driver.find_element(By.CSS_SELECTOR, "input#index-kw").click()
        # self.driver.find_element(By.ID, "index-kw").send_keys("appium")
        # self.driver.find_element(By.ID, "se-bn").click()
