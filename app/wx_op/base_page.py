# -*- coding: utf-8 -*-
# Author By Jone xie
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self._driver = driver
