import json
import yaml
import requests
from config.config import Config
from api_page.wework_utils import WeWorkUtils

class BaseApi:
    """
    api 的抽象类
    """

    api_list = yaml.safe_load(open('../config/api_list.yaml'))

    def __init__(self):
        self.config = Config()

        #请求头
        appkey = self.config.appkey
        uuid = self.config.uuid
        token = self.config.token
        t = WeWorkUtils.get_timestamp()
        t = str(t)
        sign_str = appkey + uuid + token + t
        sign = WeWorkUtils.md5vale(sign_str)

        self.headers = {
                "appkey": appkey,
                "token": token,
                "t": t,
                "uuid": uuid,
                "sign": sign,
                "uid": self.config.uid,
            }

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

        #params
        # if self.config.islogin:
        #     params['appkey'] = appkey
        #     params['token'] = token
        if 'http' not in url:
            url = self.config.baseurl + url

        data = {
            "method": method,
            "url": url,
            "json": params,
            "headers": self.headers
        }

        print('/-------------------请求数据-------------------/')
        print(json.dumps(data, indent=2,ensure_ascii=False))#对简单数据类型进行编码
        print('/-------------------返回数据-------------------/')
        response = requests.request(**data).json()
        print(json.dumps(response, indent=2,ensure_ascii=False))

        return response
