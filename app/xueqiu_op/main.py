# -*- coding: utf-8 -*-
# File:main.py
# Author:Jone xie
# Date:2022/1/12 22:59
from selenium.webdriver.common.by import By

from xueqiu_op.bsee_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # 非yaml方法
        # self.find(By.ID, 'home_search').click()
        self.steps(r"F:\学习\untitled\app\xueqiu_op\main.yaml")

    def goto_windows(self):
        self.find(By.ID, 'post_status').click()
        self.find(By.ID, 'home_search').click()
