# -*- coding: utf-8 -*-
# File:test_gettoken.py
# Author:Jone xie
# Date:2022/4/3 17:10
from jiekou.apiPO.address import Address


def test_token():
    address = Address()
    print(address.get_token())


def test_create():
    address = Address()
    print(address.creat_usr())