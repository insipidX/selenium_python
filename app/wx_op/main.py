# -*- coding: utf-8 -*-
# Author By Jone xie
from wx_op.addresslist import Addresslist
from appium import webdriver

from wx_op.base_page import BasePage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_addresslist(self):
        self.driver
        return Addresslist(self._driver)

    def goto_woekbench(self):
        pass

    def goto_profile(self):
        pass
