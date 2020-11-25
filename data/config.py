"""
OwnersApi - 当前Project名称;
config - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/11/21 5:37 下午 
"""
import yaml
import os

class Config(object):
    basedir = os.path.dirname(__file__)
    path = basedir + '/userinfo.yaml'
    userinfo = yaml.safe_load(open(path))

    appkey = 'b91714e8654c75b298fda4029685101f'
    baseurl = "http://daopu.chejinkuang.com/api/consumer/"
    uuid = 'B1566FDC-2F4D-4FE2-B8D7-A0558E771536'

    if not userinfo:
        token = ''
        uid = ''
        username = ''
        cellphone = ''
        idno = ''
        accid = ''
    else:
        token = userinfo['token']
        uid = str(userinfo['userInfo']['id'])
        username = userinfo['userInfo']['username']
        cellphone = userinfo['userInfo']['cellphone']
        idno = userinfo['userInfo']['identity_card_num']
        accid = userinfo['userInfo']['yx_video_accid']


    islogin = token != ''
