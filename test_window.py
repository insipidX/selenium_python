# -*- coding: utf-8 -*-
# Author By Jone xie

from base import Base
from time import sleep


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("s-top-loginbtn").click()
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.window_handles)
        window = self.driver.window_handles
        # 窗口代号为列表，-1选择最后一个窗口
        self.driver.switch_to_window(window[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("usrname")
        sleep(3)
    # self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("")
    # frame使用self.driver.swith_to_frame
