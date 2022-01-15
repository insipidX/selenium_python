# -*- coding: utf-8 -*-
# Author By Jone xie


from selenium import webdriver


class TestWindow():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id('s-top-loginbtn').click()
