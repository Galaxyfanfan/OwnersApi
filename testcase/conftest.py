"""
OwnersApi - 当前Project名称;
conftest.py - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/12/5 4:57 下午 
"""
from time import sleep

import openpyxl

from api_page.login_page import LoginPage
from api_page.base_api import BaseApi
from config.config import Config
from typing import List
import pytest


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 修改编码
    # 将 编码格式unicode转化为中文
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')



#scope='session' 范围：testcase文件夹下多py文件
#autouse="true" 自动执行 自动运用到所有测试方法中
@pytest.fixture(scope='session')#,autouse="true"
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
