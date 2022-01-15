# -*- coding: utf-8 -*-
# Author By Jone xie
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver
    _black_list = [(By.ID, 'gt_one_login_nav_iv')]

    def __init__(self, dirver: WebDriver = None):
        self._driver = dirver

    def find(self, locator, value):
        try:
            ele = self._driver.find_element(locator, value)
            return ele
        except:
            for black in self._black_list:
                eles = self._driver.find_elements(*black)
                if len(eles) > 0:
                    eles[0].click()
                    break
            # 处理黑名单后，重新查询原来元素
            return self.find(locator, value)

    # def click(self, locator, value):
    #     self.find(locator, value).click()

    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        ele = None
        for step in steps:
            if "by" in step.keys():
                ele = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    ele.click()
