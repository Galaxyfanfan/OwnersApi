"""
OwnersApi - 当前Project名称;
home_page - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/22 3:28 下午 
"""
from api_page.base_api import BaseApi
from api_page.wework_utils import WeWorkUtils


class HomePage(BaseApi):
    # 首页 状态
    def home_status(self):
        params = {
            'id':self.config.uid
        }
        return self.send_post(url=self.api_list['model_state'], params=params)

    # ------------------------征信授权书签署--------------------------#
    # 获取征信授权书列表
    def get_credit_lists(self):
        params = {
            'tel':self.config.cellphone,
        }
        return self.send_post(url=self.api_list['get_credit_lists'], params=params)

    # 获取合同pdf
    def get_production_pdf(self):
        credit_lists = self.get_credit_lists()
        if credit_lists['code'] == 200:
            data = credit_lists['data']
            if len(data) > 0:
                first = data[0]
                params = {
                    'bank_type': first['bank_type'],
                    'flowid': first['flow_id'],
                    'sealLocation': '120, 30',
                }

        return self.send_post(url=self.api_list['get_production_pdf'], params=params)

    # 获取验证码
    def get_verification_code(self):
        params = {
            'bank_type':'NT',
        }
        return self.send_post(url=self.api_list['get_verification_code'], params=params)

    # 校验验证码
    def check_verification_code(self):
        return self.send_post(url=self.api_list['check_verification_code'], params={})

    # 获取身份证列表
    def get_idno_img(self):
        return self.send_post(url=self.api_list['get_idno_img'], params={})


    # ------------------------合同签署--------------------------#
    # 获取合同列表
    def get_contract_lists(self):
        params = {
            'id':self.config.uid,
        }
        return self.send_post(url=self.api_list['get_contract_lists'], params=params)

    # ------------------------视频面签--------------------------#
    # 获取视频面签列表
    def call_lists(self):
        params = {
            'acc_id':self.config.accid,
            'idno': self.config.idno,
            'tel': self.config.cellphone
        }
        return self.send_post(url=self.api_list['call_lists'], params=params)

    # 申请面签
    def start_call(self):
        call_lists = self.call_lists()
        if call_lists['code'] == 200:
            data = call_lists['data']
            if len(data) > 0:
                first_dict = data[0]
                params = {
                    'acc_id': self.config.accid,
                    'bank_id': first_dict['bank_id'],
                    'flow_id': first_dict['flow_id'],
                    'id': first_dict['id'],
                    'name': first_dict['realname'],
                }

        return self.send_post(url=self.api_list['start_call'], params=params)









    # ------------------------增信补充--------------------------#
    # 获取七牛云上传token
    def get_upload_token(self):
        params = {
            't':WeWorkUtils.get_timestamp(self)
        }
        return self.send_post(url=self.api_list['get_upload_token'], params=params)

    # 获取资料库列表
    def get_picture_list(self):
        return self.send_post(url=self.api_list['get_picture_list'], params={})

    # 上传图片
    def upload_picture(self,params):
        return self.send_post(url=self.api_list['upload_picture'], params=params)

