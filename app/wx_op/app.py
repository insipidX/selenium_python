# -*- coding: utf-8 -*-
# Author By Jone xie
from appium import webdriver

from wx_op.base_page import BasePage
from wx_op.main import Main


class App(BasePage):
    def start(self):

        desired_cap = {
            "automationName": 'uiautomator2',
            "platformName": "android",
            "platformVersion": "9",
            "deviceName": "7825d7bc",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            # 是否测试后重置app
            "noReset": True,
            # 不停止app
            "dontStopAppOnReset": True,
            # 跳过初始化
            "skipDeviceInitialization": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            # 自动设置权限
            "autoGrantPermissions": True

        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(10)
        # WebView.setWebContentsDebuggingEnabled(True)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
