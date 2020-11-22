"""
OwnersApi - 当前Project名称;
test_login - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/21 4:12 下午 
"""
from api_page.login_page import LoginPage

class TestLogin():
    def setup_class(self):
        self.login = LoginPage()

    def test_code(self):
        params = {
            'cellphone':19292999229
        }
        login_message = self.login.get_code(params)
        assert login_message['code'] in [0, 400]

    def test_login(self):
        params = {
            "cellphone": 19292999229,
            "smsCode":1234
        }
        login_message = self.login.login(params)
        assert login_message['code'] == 200

    def test_logout(self):
        self.login.logout()