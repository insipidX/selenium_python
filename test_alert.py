# -*- coding: utf-8 -*-
# Author By Jone xie

from base import Base
from selenium.webdriver import ActionChains
from time import sleep

class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")

        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        # action.click_and_hold(drag).release(drop).perform()
        sleep(3)

        print("点击确认")
        # 切换窗口
        self.driver.switch_to.alert.accept()
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)