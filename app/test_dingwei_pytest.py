# -*- coding: utf-8 -*-
# Author By Jone xie
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDw:

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
        self.driver.quit()

    # 搜索并返回股价是否大于100
    # def test_serch(self):
    #     el1 = self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search")
    #     el1.click()
    #     el2 = self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text")
    #     el2.click()
    #     el2.send_keys("阿里巴巴")
    #     self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']").click()
    #     current_price = float(self.driver.find_element(By.ID, "com.xueqiu.android:id/current_price").text)
    #     assert current_price > 100

    #   常用方法
    # def test_attr(self):
    #     element = self.driver.find_element(By.ID, "com.xueqiu.android:id/home_search")
    #     element_serch = element.is_enabled()
    #     print(element.text)
    #     print(element.location)
    #     print(element.size)
    #     if element_serch == True:
    #         element.click()
    #         self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
    #         alibaba_element = self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']")
    # 需要多点一下才可以出现搜索内容
    #         self.driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").click()
    #         element_displayed = alibaba_element.get_attribute("displayed")
    #         if element_displayed == "true":
    #             print("搜索成功")
    #         else:
    #             print("搜索失败")

    # 显式等待，非全局
    #    locator=(By.ID,"com.xueqiu.android:id/search_input_text")
    # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(*locator))
    # 模拟触屏操作
    # def test_touchaction(self):
    #     action = TouchAction(self.driver)
    #     action.press(x=731, y=1083).wait(500).move_to(x=731, y=484).release().perform()
    #


if __name__ == '__main__':
    pytest.main()
