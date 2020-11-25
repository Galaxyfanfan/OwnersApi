"""
OwnersApi - 当前Project名称;
test_user - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/23 2:39 下午 
"""
import allure

from api_page.user_page import UserPage
@allure.feature('个人中心')
class TestUser():
    # ------------------------（个人中心）--------------------------#
    def setup_class(self):
        self.user = UserPage()


    # ------------------------消息--------------------------#
    @allure.story('获取消息未读数')
    def test_get_unread_number(self):
        message = self.user.get_unread_number()
        assert message['code'] == 200

    @allure.story('获取消息列表')
    def test_get_news_list(self):
        message = self.user.get_news_list(page=1)
        assert message['code'] == 200

    @allure.story('查看消息详情')
    def test_get_news_info(self):
        message = self.user.get_news_info(info_id=123)
        assert message['code'] == 200

    @allure.story('设置全部已读')
    def test_set_all_readr(self):
        message = self.user.set_all_read()
        assert message['code'] == 200

    # ------------------------还款详情--------------------------#
    @allure.story('还款列表')
    def test_get_repayloan_list(self):
        message = self.user.get_repayloan_list()
        assert message['code'] == 200

    @allure.story('还款卡信息')
    def test_selcard(self):
        with allure.step('还款列表'):
            list = self.user.get_repayloan_list()
            if list['code'] == 200:
                if len(list['data']) > 0:
                    flowid = list['data'][0]['flow_id']

        message = self.user.selcard(flowid)
        assert message['code'] == 200

    @allure.story('还款计划表')
    def test_repayment_plan(self):
        with allure.step('还款列表'):
            list = self.user.get_repayloan_list()
            if list['code'] == 200:
                if len(list['data']) > 0:
                    flowid = list['data'][0]['flow_id']
        message = self.user.repayment_plan(flowid)
        assert message['code'] == 200

    # ------------------------车险理赔--------------------------#
    @allure.story('理赔列表')
    def test_get_claims_list(self):
        message = self.user.get_claims_list()
        assert message['code'] == 200

    @allure.story('理赔详情')
    def test_get_claims_detail(self):
        with allure.step('理赔列表'):
            list = self.user.get_claims_list()
            if list['code'] == 200:
                if len(list['data']) > 0:
                    flowid = list['data'][0]['flowid']

        message = self.user.get_claims_detail(flowid)
        assert message['code'] == 200

    @allure.story('理赔历史记录')
    def test_get_claims_histroy(self):
        with allure.step('理赔列表'):
            list = self.user.get_claims_list()
            if list['code'] == 200:
                if len(list['data']) > 0:
                    flowid = list['data'][0]['flowid']

        message = self.user.get_claims_histroy(flowid)
        assert message['code'] == 200

    @allure.story('提交理赔')
    def test_commit_claims(self):
        with allure.step('理赔列表'):
            list = self.user.get_claims_list()
            if list['code'] == 200:
                if len(list['data']) > 0:
                    flowid = list['data'][0]['flowid']
        with allure.step('理赔详情'):
            detail = self.user.get_claims_detail(flowid)
            if detail['code'] == 200:
                departid = detail['data']['depart_id']
                files = detail['data']['files']
                if len(files) > 0:
                    id = files[0]['id']
        params = {
            'amount':6000,
            'departid':departid,
            'files':[],
            'flowid':flowid,
            'id':id
        }
        message = self.user.commit_claims(params)
        assert message['code'] == 200

