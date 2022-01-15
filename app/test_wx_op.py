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

from wx_op.app import App


class TestWX:

    def setup(self):

        self.app = App()
        self.main = self.app.start().main()

    #
    # def teardown(self):
    #     self.driver.quit()
    #     sleep(3)


    def test_addmenber(self):
        self.main.goto_addresslist().add_menber().addmenber_by_manul().imput_name().set_gender().input_phonenum().click_save()

