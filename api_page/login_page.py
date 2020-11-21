"""
OwnersApi - 当前Project名称;
login_api - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/21 3:30 下午 
"""
from api_page.base_api import BaseApi
import yaml

class LoginPage(BaseApi):
    """
    登录
    """

    api_list = yaml.safe_load(open('../datas/api_list.yaml'))

    # def __init__(self):
    #     pass

    def get_code(self,params):
        return self.send_post(url=self.api_list['code'],params=params)

    def login(self):
        pass
