# -*- coding: utf-8 -*-
# Author By Jone xie
# 上传文件
from base import Base
from time import sleep


class TestFile(Base):
    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("C:\\Users\\QG\Desktop\\1.jpg")
        sleep(5)
