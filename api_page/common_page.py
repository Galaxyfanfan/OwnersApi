"""
OwnersApi - 当前Project名称;
common_page - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2021/4/1 10:31 上午 
"""

from api_page.base_api import BaseApi



class CommonPage(BaseApi):

    def get_api(self,url,request_mode,params,headers):
        if headers is not None:
            self.headers = headers
        if request_mode == 'POST':
            return self.send_post(url=url, params=params)
        else:
            return self.send_get(url=url,params=params)