"""
OwnersApi - 当前Project名称;
test_login - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/21 4:12 下午 
"""
from api_page.login_page import LoginPage

class TestLogin():

    def test_code(self):
        login = LoginPage()
        params = {
            'cellphone':19292999229
        }
        login_message = login.get_code(params)

        assert login_message['code'] in [0, 400]
