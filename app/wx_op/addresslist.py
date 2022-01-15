# -*- coding: utf-8 -*-
# Author By Jone xie
from wx_op.base_page import BasePage


class Addresslist(BasePage):
    def add_menber(self):
        from wx_op.MemberInvite import MemberInvite
        return MemberInvite(self._driver)
