"""
OwnersApi - 当前Project名称;
test_home - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/22 3:35 下午 
"""
import pytest
import allure

from api_page.home_page import HomePage

@allure.feature('首页')# feature定义功能

# def test_1(login):
#     print('1111')

class TestHome(object):#需要继承object 不然无法调用login
    def setup_class(self):
        self.home = HomePage()

    @allure.story('首页 状态')  # story定义用户场景
    @allure.severity(allure.severity_level.NORMAL)
    def test_model_status(self,login):
        home_message = self.home.home_status()
        assert home_message['code'] == 200

    # ------------------------征信授权书签署--------------------------#
    @allure.story('获取征信授权书列表')  # story定义用户场景
    @allure.severity(allure.severity_level.BLOCKER)  # 严重级别
    def test_get_credit_lists(self,login):
        home_message = self.home.get_credit_lists()
        assert home_message['code'] == 200


    # ------------------------合同签署--------------------------#
    @allure.story('获取合同列表')
    def test_get_contract_lists(self,login):
        home_message = self.home.get_contract_lists()
        assert home_message['code'] == 200

    @pytest.mark.skip()
    @allure.story('获取合同pdf')
    def test_get_production_pdf(self,login):
        home_message = self.home.get_production_pdf()
        assert home_message['code'] == 200

    @pytest.mark.skip()
    @allure.story('获取验证码')
    def test_get_verification_code(self,login):
        home_message = self.home.get_verification_code()
        assert home_message['code'] == 200

    @pytest.mark.skip()
    @allure.story('校验验证码')
    def test_check_verification_code(self,login):
        home_message = self.home.check_verification_code()
        assert home_message['code'] == 200

    @allure.story('获取身份证列表')
    def test_get_idno_img(self,login):
        home_message = self.home.get_idno_img()
        assert home_message['code'] == 200


    # ------------------------视频面签--------------------------#
    @allure.story('获取视频面签列表')
    def test_call_lists(self,login):
        home_message = self.home.call_lists()
        assert home_message['code'] == 200

    @allure.story('申请面签')
    def test_start_call(self,login):
        home_message = self.home.start_call()
        assert home_message['code'] == 200


    # ------------------------增信补充--------------------------#
    @allure.story('获取七牛云上传token')
    def test_get_upload_token(self,login):
        home_message = self.home.get_upload_token()
        assert home_message['code'] == 200

    @allure.story('获取资料库列表')
    def test_get_picture_list(self,login):
        home_message = self.home.get_picture_list()
        assert home_message['code'] == 200

    @allure.story('上传图片')
    def test_upload_picture(self):
        params = {
            'address':'中国浙江省杭州市',
            'city':'杭州市',
            'lon_lat': '120, 30',
            'type': '96',
            'url': '202011/985_22_2420201122164524621.png'
        }
        home_message = self.home.upload_picture(params)
        allure.attach('上传图片',attachment_type=allure.attachment_type.TEXT)
        assert home_message['code'] == 200

if __name__ == '__main__':
    pytest.main()