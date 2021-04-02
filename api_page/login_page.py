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
    获取验证码
    """
    def get_code(self,params):
        return self.send_post(url=self.api_list['code'],params=params)
    """
    登录
    """
    def login(self,params):
        response = self.send_post(url=self.api_list['login'],params=params)
        if response['code'] == 200:
            #登录数据保存
            print('登录数据保存')
            data = response['data']
            self.config.userinfo = data
            self.config.token = data['token']
            self.config.uid = str(data['userInfo']['id'])
            self.config.username = data['userInfo']['username']
            self.config.cellphone = data['userInfo']['cellphone']
            self.config.idno = data['userInfo']['identity_card_num']
            self.config.accid = data['userInfo']['yx_video_accid']

            WeWorkUtils.save_user_info( data)

        return response
    """
    设备信息
    """
    def client_device(self):
        params = {

        }
        return self.send_post(url=self.api_list['client_device'], params=params)

    """
    退出登录
    """
    def logout(self):
        data = {}
        WeWorkUtils.save_user_info(data)
        self.config.uid = ''
        self.config.token = ''
        self.config.cellphone = ''
        self.config.username = ''
        self.config.islogin = False

    """
    获取应用信息
    """
    # 获取应用信息
    def get_last_app(self):
        params = {
            'appkey' : self.config.appkey,
            't' : WeWorkUtils.get_timestamp(self)
        }
        return self.send_post(url=self.api_list['get_last_app'], params=params)
