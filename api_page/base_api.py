import json
import yaml
import requests
import time
from api_page.wework_utils import WeWorkUtils

class BaseApi:
    """
    api 的抽象类
    """
    env = yaml.safe_load(open('../datas/env.yaml'))

    #基础 get请求
    def send_get(self,url,params: dict):
        return self.send_api(url=url,method='get',params=params)

    #基础 post请求
    def send_post(self,url,params: dict):
        return self.send_api(url=url,method='post',params=params)

    def send_api(self,url,method,params: dict):
        """
        发送 api
        """
        appkey = self.env['appkey']
        uuid = self.env['uuid']
        token = self.env['token']
        t = WeWorkUtils.get_timestamp(self)
        t = str(t)
        sign_str = appkey + uuid + token + t
        sign = WeWorkUtils.md5vale(self,sign_str)

        data = {
            "method": method,
            "url": self.env['baseurl'] + url,
            "json": params,
            "headers": {
                "appkey": appkey,
                "token": token,
                "t": t,
                "uuid": uuid,
                "sign": sign,
                "uid": '',
            }
        }

        print('------------请求数据--------------')
        print(json.dumps(data, indent=2,ensure_ascii=False))#对简单数据类型进行编码
        print('------------返回数据--------------')
        response = requests.request(**data).json()
        print(json.dumps(response, indent=2,ensure_ascii=False))

        return response
