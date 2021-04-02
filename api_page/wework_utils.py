import hashlib
import time

import yaml


class WeWorkUtils:
    #字符串 md5加密
    @staticmethod
    def md5vale(key):
        input_name = hashlib.md5()
        input_name.update(key.encode("utf-8"))
        return input_name.hexdigest()

    #获取 毫秒级 时间戳
    @staticmethod
    def get_timestamp():
        t = int(round(time.time() * 1000))
        # print(f'时间戳：{t}')  # 毫秒级时间戳
        return t

    @staticmethod
    def save_user_info(data):
        with open('../config/userinfo.yaml', mode='w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True)