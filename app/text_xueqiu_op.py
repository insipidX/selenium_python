# -*- coding: utf-8 -*-
# Author By Jone xie
import pytest
import yaml

from xueqiu_op.app import App


class TestMain:
    @pytest.mark.parametrize("value1, value2", yaml.safe_load(open('./test_xueqiu.yaml')))
    def test_main(self, value1, value2):
        app = App()
        app.start().main().goto_search()

        print(value1)
        print(value2)


    def test_windows(self):
        app = App()
        app.start().main().goto_windows()