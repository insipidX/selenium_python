# -*- coding: utf-8 -*-
# Author By Jone xie
from appium.webdriver.common.mobileby import MobileBy

from wx_op.base_page import BasePage


class ContactAdd(BasePage):
    def imput_name(self):
        self._driver.find_element(MobileBy.XPATH,"//*[@text=]")
        return self

    def set_gender(self):
        return self

    def input_phonenum(self):
        return self

    def click_save(self):
        from wx_op.MemberInvite import MemberInvite
        return MemberInvite(self._driver)
