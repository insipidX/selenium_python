# -*- coding: utf-8 -*-
# File:app.py
# Author:Jone xie
# Date:2022/1/12 22:28
import yaml
from appium import webdriver

from xueqiu_op.bsee_page import BasePage
from xueqiu_op.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:

            desired_cap = {
                "automationName": 'uiautomator2',
                "platformName": "android",
                "platformVersion": "9",
                "deviceName": "7825d7bc",
                "udid": yaml.safe_load(open(r"F:\学习\untitled\app\xueqiu_op\configuration.yaml"))['caps']['udid'],
                "appPackage": self._package,
                "appActivity": self._activity,
                # 是否测试后重置app
                "noReset": True,
                # 不停止app
                "dontStopAppOnReset": True,
                # 跳过初始化
                "skipDeviceInitialization": True,
                "unicodeKeyboard": True,
                "resetKeyboard": True

            }

            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)

        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(10)
        return self

    def main(self) -> Main:
        # 需要添加driver的值
        return Main(self._driver)
