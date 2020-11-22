"""
OwnersApi - 当前Project名称;
config - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/21 5:37 下午 
"""
import yaml


class Config(object):
    userinfo = yaml.safe_load(open('../datas/userinfo.yaml'))

    appkey = 'b91714e8654c75b298fda4029685101f'
    baseurl = "http://daopu.chejinkuang.com/api/consumer/"
    uuid = '123456kjshksjs'

    try:
        token = userinfo['token']
        uid = userinfo['userInfo']['id']
        username = userinfo['userInfo']['username']
        cellphone = userinfo['userInfo']['cellphone']
    except:
        token = ''
        uid = ''
        username = ''
        cellphone = ''

    islogin = token != ''
