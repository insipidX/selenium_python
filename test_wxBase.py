# -*- coding: utf-8 -*-
# Author By Jone xie
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium import webdriver


# 本地包关键字不亮的时候
# noinspection PyUnresolvedReferences
# from base import Base


class TestDemo():
    def setup_method(self, method):
        options = Options()

        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        # self.driver.find_element_by_id("menu_contacts").click()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 获取当前cookies
        # print(self.driver.get_cookies())

        #取出的cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1635064685'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
                                                                    'name': 'wwrtx.logined', 'path': '/',
                                                                    'secure': False, 'value': 'true'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
                'value': '1688857427272169'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid',
                                               'path': '/', 'secure': False, 'value': '1688857427272169'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
                'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
                                'secure': False, 'value': '38933948511169809'}, {'domain': '.qq.com',
                                                                                 'expiry': 1857879301,
                                                                                 'httpOnly': False,
                                                                                 'name': 'tvfe_boss_uuid', 'path': '/',
                                                                                 'secure': False,
                                                                                 'value': 'a9400f74b36585f5'}, {
                'domain': '.work.weixin.qq.com', 'expiry': 1666592368, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
                'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1698137964,
                                                              'httpOnly': False, 'name': '_ga', 'path': '/',
                                                              'secure': False, 'value': 'GA1.2.395169894.1635056371'}, {
                'domain': '.work.weixin.qq.com', 'expiry': 1637658016, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
                                                               'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                                                               'value': 'AnGNgvPvfZ2p64xEorCESNZ6jET4_2HjFQ9fxk_yHEgX_ljrX2Q0As666TlXSi8AjM2HGHMAtL1J9h6LzhRNh4hGZ3nadf1wIu-sHaSaXN26VkzXxDAF7G63uOiYkmzXL7JG2jHX_FFGdWaX54aJFmaenp9yf8q36RbVAPdWH46CXFtn01iybGtGMFj3eijTynMQp5GhyC0O4FZjvj1e3tEc6gN6613GiHG27wJcVGT3izdmxDC21VaE2utraQcEugCKPoK3mfh9BYFeUHVfPg'},
            {
                'domain': '.work.weixin.qq.com', 'expiry': 1666600685, 'httpOnly': False,
                'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                'value': '1635056370,1635056512,1635056754,1635060218'}, {'domain': '.qq.com', 'httpOnly': False,
                                                                          'name': '_qpsvr_localtk', 'path': '/',
                                                                          'secure': False,
                                                                          'value': '0.8837758428949849'}, {
                'domain': '.qq.com', 'httpOnly': False, 'name': 'ptisp', 'path': '/', 'secure': False,
                'value': 'edu'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'match2019_sid', 'path': '/',
                                  'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
                                                                  'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                                                                  'value': 'twgjL_90SUjQLVOQ9ofPLVcvLqYulMGJME_wlxrzwBVTROe12DOXeWW3IDrCL5hG'},
            {
                'domain': '.qq.com', 'expiry': 1635152364, 'httpOnly': False, 'name': '_gid', 'path': '/',
                'secure': False, 'value': 'GA1.2.103066294.1635056371'}, {'domain': '.work.weixin.qq.com',
                                                                          'httpOnly': False, 'name': 'wwrtx.d2st',
                                                                          'path': '/', 'secure': False,
                                                                          'value': 'a3218212'}, {'domain': '.qq.com',
                                                                                                 'httpOnly': False,
                                                                                                 'name': 'lplqqcomrouteLine',
                                                                                                 'path': '/',
                                                                                                 'sameSite': 'Lax',
                                                                                                 'secure': False,
                                                                                                 'value': 'a20200903worlds_a20200903worlds'},
            {
                'domain': '.qq.com', 'expiry': 1635077287, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
                'secure': False, 'value': '0126O0V3B5G4G1H2p8E7n2E8m7'}, {'domain': '.qq.com', 'httpOnly': False,
                                                                          'name': 'vfwebqq', 'path': '/',
                                                                          'secure': False,
                                                                          'value': 'b7e1d3e74562630d1154a00dafa1f1670678dc467e5bf6d53f964e24a76df0d2c7391fd406cff930'},
            {
                'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
                'value': 'ssid=s2293474212'}, {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False,
                                               'name': 'RK', 'path': '/', 'secure': False, 'value': 'STAsT5zVtS'}, {
                'domain': '.qq.com', 'httpOnly': False, 'name': 'session_id', 'path': '/', 'secure': False,
                'value': 'null'}, {'domain': '.qq.com', 'expiry': 7895619500, 'httpOnly': False,
                                   'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False,
                                   'value': '%7B%22distinct_id%22%3A%22171d52dfa1b542-058687a3f67cc5-6373664-1397912-171d52dfa1c176%22%2C%22%24device_id%22%3A%22171d52dfa1b542-058687a3f67cc5-6373664-1397912-171d52dfa1c176%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D'},
            {
                'domain': '.qq.com', 'httpOnly': False, 'name': 'user_id', 'path': '/', 'secure': False,
                'value': 'null'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz',
                                   'path': '/', 'secure': False,
                                   'value': 'b6a53f4c457e9427903faf32c4fe0ba21299d15fd88c85e2c62bdf1dd563ce69'}, {
                'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
                'secure': False, 'value': '2450639353'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
                                                          'name': 'wwrtx.ref', 'path': '/', 'secure': False,
                                                          'value': 'direct'}, {'domain': '.work.weixin.qq.com',
                                                                               'httpOnly': False,
                                                                               'name': 'wwrtx.cs_ind', 'path': '/',
                                                                               'secure': False, 'value': ''}, {
                'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_si', 'path': '/', 'secure': False,
                'value': 's6619157504'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid',
                                          'path': '/', 'secure': False, 'value': '1970324954494477'}, {
                'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
                'secure': False, 'value': '8855679266'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False,
                                                          'name': 'pgv_pvi', 'path': '/', 'secure': False,
                                                          'value': '6953590784'}]

        #db = shelve.open("cookies")
        # shelve
        #cookies = db["cookie"]
        #db["cookie"]=self.driver.get_cookies()

        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)






#
#
#
# 取出的cookie
# cookies = [
#             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
#              'path': '/', 'secure': False, 'value': '1635064685'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
#                                                                     'name': 'wwrtx.logined', 'path': '/',
#                                                                     'secure': False, 'value': 'true'}, {
#                 'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
#                 'value': '1688857427272169'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid',
#                                                'path': '/', 'secure': False, 'value': '1688857427272169'}, {
#                 'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
#                 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
#                                 'secure': False, 'value': '38933948511169809'}, {'domain': '.qq.com',
#                                                                                  'expiry': 1857879301,
#                                                                                  'httpOnly': False,
#                                                                                  'name': 'tvfe_boss_uuid', 'path': '/',
#                                                                                  'secure': False,
#                                                                                  'value': 'a9400f74b36585f5'}, {
#                 'domain': '.work.weixin.qq.com', 'expiry': 1666592368, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
#                 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1698137964,
#                                                               'httpOnly': False, 'name': '_ga', 'path': '/',
#                                                               'secure': False, 'value': 'GA1.2.395169894.1635056371'}, {
#                 'domain': '.work.weixin.qq.com', 'expiry': 1637658016, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
#                 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
#                                                                'name': 'wwrtx.vst', 'path': '/', 'secure': False,
#                                                                'value': 'AnGNgvPvfZ2p64xEorCESNZ6jET4_2HjFQ9fxk_yHEgX_ljrX2Q0As666TlXSi8AjM2HGHMAtL1J9h6LzhRNh4hGZ3nadf1wIu-sHaSaXN26VkzXxDAF7G63uOiYkmzXL7JG2jHX_FFGdWaX54aJFmaenp9yf8q36RbVAPdWH46CXFtn01iybGtGMFj3eijTynMQp5GhyC0O4FZjvj1e3tEc6gN6613GiHG27wJcVGT3izdmxDC21VaE2utraQcEugCKPoK3mfh9BYFeUHVfPg'}, {
#                 'domain': '.work.weixin.qq.com', 'expiry': 1666600685, 'httpOnly': False,
#                 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
#                 'value': '1635056370,1635056512,1635056754,1635060218'}, {'domain': '.qq.com', 'httpOnly': False,
#                                                                           'name': '_qpsvr_localtk', 'path': '/',
#                                                                           'secure': False,
#                                                                           'value': '0.8837758428949849'}, {
#                 'domain': '.qq.com', 'httpOnly': False, 'name': 'ptisp', 'path': '/', 'secure': False,
#                 'value': 'edu'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'match2019_sid', 'path': '/',
#                                   'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
#                                                                   'name': 'wwrtx.sid', 'path': '/', 'secure': False,
#                                                                   'value': 'twgjL_90SUjQLVOQ9ofPLVcvLqYulMGJME_wlxrzwBVTROe12DOXeWW3IDrCL5hG'}, {
#                 'domain': '.qq.com', 'expiry': 1635152364, 'httpOnly': False, 'name': '_gid', 'path': '/',
#                 'secure': False, 'value': 'GA1.2.103066294.1635056371'}, {'domain': '.work.weixin.qq.com',
#                                                                           'httpOnly': False, 'name': 'wwrtx.d2st',
#                                                                           'path': '/', 'secure': False,
#                                                                           'value': 'a3218212'}, {'domain': '.qq.com',
#                                                                                                  'httpOnly': False,
#                                                                                                  'name': 'lplqqcomrouteLine',
#                                                                                                  'path': '/',
#                                                                                                  'sameSite': 'Lax',
#                                                                                                  'secure': False,
#                                                                                                  'value': 'a20200903worlds_a20200903worlds'}, {
#                 'domain': '.qq.com', 'expiry': 1635077287, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
#                 'secure': False, 'value': '0126O0V3B5G4G1H2p8E7n2E8m7'}, {'domain': '.qq.com', 'httpOnly': False,
#                                                                           'name': 'vfwebqq', 'path': '/',
#                                                                           'secure': False,
#                                                                           'value': 'b7e1d3e74562630d1154a00dafa1f1670678dc467e5bf6d53f964e24a76df0d2c7391fd406cff930'}, {
#                 'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
#                 'value': 'ssid=s2293474212'}, {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False,
#                                                'name': 'RK', 'path': '/', 'secure': False, 'value': 'STAsT5zVtS'}, {
#                 'domain': '.qq.com', 'httpOnly': False, 'name': 'session_id', 'path': '/', 'secure': False,
#                 'value': 'null'}, {'domain': '.qq.com', 'expiry': 7895619500, 'httpOnly': False,
#                                    'name': 'sensorsdata2015jssdkcross', 'path': '/', 'secure': False,
#                                    'value': '%7B%22distinct_id%22%3A%22171d52dfa1b542-058687a3f67cc5-6373664-1397912-171d52dfa1c176%22%2C%22%24device_id%22%3A%22171d52dfa1b542-058687a3f67cc5-6373664-1397912-171d52dfa1c176%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D'}, {
#                 'domain': '.qq.com', 'httpOnly': False, 'name': 'user_id', 'path': '/', 'secure': False,
#                 'value': 'null'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz',
#                                    'path': '/', 'secure': False,
#                                    'value': 'b6a53f4c457e9427903faf32c4fe0ba21299d15fd88c85e2c62bdf1dd563ce69'}, {
#                 'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
#                 'secure': False, 'value': '2450639353'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
#                                                           'name': 'wwrtx.ref', 'path': '/', 'secure': False,
#                                                           'value': 'direct'}, {'domain': '.work.weixin.qq.com',
#                                                                                'httpOnly': False,
#                                                                                'name': 'wwrtx.cs_ind', 'path': '/',
#                                                                                'secure': False, 'value': ''}, {
#                 'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_si', 'path': '/', 'secure': False,
#                 'value': 's6619157504'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid',
#                                           'path': '/', 'secure': False, 'value': '1970324954494477'}, {
#                 'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
#                 'secure': False, 'value': '8855679266'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False,
#                                                           'name': 'pgv_pvi', 'path': '/', 'secure': False,
#                                                           'value': '6953590784'}]