"""
OwnersApi - 当前Project名称;
login_api - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/21 3:30 下午 
"""
import json

from api_page.base_api import BaseApi
import yaml

from api_page.wework_utils import WeWorkUtils


class LoginPage(BaseApi):
    """
    登录
    """

    api_list = yaml.safe_load(open('../datas/api_list.yaml'))

    def get_code(self,params):
        return self.send_post(url=self.api_list['code'],params=params)

    def login(self,params):
        response = self.send_post(url=self.api_list['login'],params=params)
        if response['code'] == 200:
            #登录数据保存
            print('登录数据保存')
            data = response['data']
            WeWorkUtils.save_user_info(self, data)

        return self.send_post(url=self.api_list['login'],params=params)


    """
    退出登录
    """
    def logout(self):
        data = {}
        WeWorkUtils.save_user_info(self,data)
        self.config.uid = ''
        self.config.token = ''
        self.config.cellphone = ''
        self.config.username = ''
        self.config.islogin = False