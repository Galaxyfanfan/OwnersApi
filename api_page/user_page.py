"""
OwnersApi - 当前Project名称;
user_page - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/22 6:13 下午 
"""
from api_page.base_api import BaseApi
from api_page.wework_utils import WeWorkUtils


class UserPage(BaseApi):
    # 获取消息未读数
    def get_unread_number(self):
        return self.send_post(url=self.api_list['get_unread_number'], params={})

    # 获取消息列表
    def get_news_list(self,page):
        params = {
            'page':page
        }
        return self.send_post(url=self.api_list['get_news_list'], params=params)

    # 查看消息详情
    def get_news_info(self,info_id):
        params = {
            'id':info_id
        }
        return self.send_post(url=self.api_list['get_news_info'], params=params)

    # 设置全部已读
    def set_all_read(self):
        params = {
            'type':2
        }
        return self.send_post(url=self.api_list['set_all_read'], params=params)


    # ------------------------还款详情--------------------------#
    # 还款列表
    def get_repayloan_list(self):
        params = {
            'idno':self.config.idno
        }
        return self.send_post(url=self.api_list['get_repayloan_list'], params=params)

    # 还款卡信息
    def selcard(self,flow_id):
        params = {
            'flowid':flow_id
        }
        return self.send_post(url=self.api_list['selcard'], params=params)

    # 还款计划表
    def repayment_plan(self,flow_id):
        params = {
            'flowid':flow_id
        }
        return self.send_post(url=self.api_list['repayment_plan'], params=params)

    # ------------------------车险理赔--------------------------#
    # 理赔列表
    def get_claims_list(self):
        params = {
            'id':self.config.uid
        }
        return self.send_post(url=self.api_list['get_claims_list'], params=params)


    # 理赔详情
    def get_claims_detail(self,flow_id):
        params = {
            'flowid':flow_id
        }
        return self.send_post(url=self.api_list['get_claims_detail'], params=params)

    # 理赔历史记录
    def get_claims_histroy(self,flow_id):
        params = {
            'flow_id':flow_id
        }
        return self.send_post(url=self.api_list['get_claims_histroy'], params=params)

    # 提交理赔
    def commit_claims(self,params):
        return self.send_post(url=self.api_list['commit_claims'], params=params)
