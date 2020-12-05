"""
OwnersApi - 当前Project名称;
conftest.py - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/12/5 4:57 下午 
"""
from time import sleep

import pytest
from api_page.login_page import LoginPage
from api_page.base_api import BaseApi
from data.config import Config

@pytest.fixture(scope='session')
def login():
    print("登录")
    params = {
        "cellphone": 16896689007,
        "smsCode": 1234
    }

    my_login = LoginPage()
    if my_login.config.islogin:
        print('已登录')
    else:
        login_message = my_login.login(params)
        assert login_message['code'] == 200


    yield
    print('完成')
