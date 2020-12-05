"""
OwnersApi - 当前Project名称;
test_login - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/21 4:12 下午 
"""
import allure
import pytest

from api_page.login_page import LoginPage
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