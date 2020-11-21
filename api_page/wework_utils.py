import hashlib
import time


class WeWorkUtils:
    #字符串 md5加密
    def md5vale(self,key):
        input_name = hashlib.md5()
        input_name.update(key.encode("utf-8"))
        return input_name.hexdigest()

    #获取 毫秒级 时间戳
    def get_timestamp(self):
        t = int(round(time.time() * 1000))
        print(f'时间戳：{t}')  # 毫秒级时间戳
        return t