# -*- coding: utf-8 -*-
# Author By Jone xie
from wx_op.base_page import BasePage


class MemberInvite(BasePage):
    def addmenber_by_manul(self):
        from wx_op.ContactAdd import ContactAdd
        return ContactAdd(self._driver)

    def get_toast(self):
        return "toast"
