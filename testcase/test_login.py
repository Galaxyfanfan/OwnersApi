"""
OwnersApi - 当前Project名称;
test_login - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/21 4:12 下午 
"""
import allure
import pytest
import yaml

from api_page.login_page import LoginPage


def getLoginData():
    login_dic = yaml.safe_load(open('../testdata/login.yaml'))
    phone_list = login_dic['phone']
    code_list = login_dic['code']

    login_list = []
    for phone in phone_list:
        phone_num = phone['num']
        phone_status = phone['code']
        for code in code_list:
            code_num = code['num']
            code_status = code['code']
            if phone_status == 200:
                login_list.append((phone_num, code_num, [code_status]))
            else:
                login_list.append((phone_num, code_num, [phone_status, code_status]))

    return login_list

@allure.feature('登录')# feature定义功能
class TestLogin():

    def setup_class(self):
        self.login = LoginPage()

    @allure.story('获取登录验证码')
    def test_code(self):
        params = {
            'cellphone':16896689007
        }
        login_message = self.login.get_code(params)
        assert login_message['code'] == 200

    @pytest.mark.skip()
    @allure.story('登录')
    def test_login(self):
        if self.login.config.islogin :
            print('已登录')
            return

        params = {
            "cellphone": 16896689007,
            "smsCode":1234
        }
        login_message = self.login.login(params)
        assert login_message['code'] == 200

    @pytest.mark.skip()
    @allure.story('退出登录')
    def test_logout(self):
        self.login.logout()

    @allure.story('获取应用信息')
    def test_get_last_app(self):
        login_message = self.login.get_last_app()
        assert login_message['code'] == 200

    @allure.story('登录用例验证')
    @pytest.mark.parametrize("phone,code,back_assert",getLoginData())
    # @pytest.mark.parametrize("phone,code,back_assert", [('16896689007','1234',[200])])
    def test_login_verify(self,phone,code,back_assert):
        params = {
            "cellphone": phone,
            "smsCode":code
        }
        self.login.headers = {
            'appkey' : '123'
        }#登录的时候没做校验
        login_message = self.login.login(params)
        assert login_message['code'] in back_assert