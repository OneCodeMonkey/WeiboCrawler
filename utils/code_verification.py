import json
import time

import requests
from hashlib import md5

from logger import other


class YDMHttp:
    apiurl = 'http://api.yundama.com/api.php'
    username = ''
    password = ''
    appid = ''
    appkey = ''

    def __init__(self, name, passwd, app_id, app_key):
        self.username = name
        self.password = passwd
        self.appid = str(app_id)
        self.appkey = app_key

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response

    def balance(self):
        data = {
            'method': 'balance',
            'username': self.username,
            'password': self.password,
            'appid': self.appid,
            'appkey': self.appkey
        }
        response = self.request(data)
        if response:
            if response['ret'] and response['ret'] < 0:
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001

    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if response:
            if response['ret'] and response['ret'] < 0:
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if response:
            if response['ret'] and response['ret'] < 0:
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, file_name, code_type, time_out):
        cid = self.upload(file_name, code_type, time_out)
        if cid > 0:
            for i in range(0, time_out):
                result = self.result(cid)
                if result != '':
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def post_url(self, url, fields, files=[]):
        for key in files:
            files[key] = open(files[key], 'rb')
        res = requests.post(url, files=files, data=fields)
        return res.text

    def report_error(self, cid):
        data = {
            'method': 'report',
            'username': self.username,
            'password': self.password,
            'appid': self.appid,
            'appkey': self.appkey,
            'flag': 0,
            'cid': cid
        }

        response = self.request(data)
        if response:
            if response['ret']:
                return response['ret']
        else:
            return -9001


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {+
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


def code_verificate(name, passwd, file_name, code_type=1005, app_id=3510, app_key='7281f8452aa559cdad6673684aa8f575',
                    time_out=60):
    chaojiying = Chaojiying_Client('cjyA123B', 'chaojiyingA123', '96001')  # 用户中心>>软件ID 生成一个替换 96001
    # im = open('a.jpg', 'rb').read()
    api_cjy_result = chaojiying.PostPic(file_name, 1902)
    rs = api_cjy_result['pic_str']
    err_no = api_cjy_result['err_no']
    cid = api_cjy_result['pic_id']

    return rs, chaojiying, cid, err_no


# def code_verificate(name, passwd, file_name, code_type=1005, app_id=3510, app_key='7281f8452aa559cdad6673684aa8f575',
#                     time_out=60):
#     """
#     :param name: 云打码注册用户名，这是普通用户注册，而非开发者用户注册名
#     :param passwd: 用户密码
#     :param file_name: 需要识别的图片名
#     :param app_id: 软件ID，这里默认是填的我的，如果需要，可以自行注册一个开发者账号，填自己的。
#     软件开发者会有少额提成，希望大家支持weibospider的发展（提成的20%会给celery项目以支持其发展）
#     :param app_key: 软件key，这里默认是填的我的，如果需要，可以自行注册一个开发者账号，填自己的
#     :param code_type: 1005表示五位字符验证码。价格和验证码类别，详细请看http://www.yundama.com/price.html
#     :param time_out: 超时时间
#     :return: 验证码结果
#     """
#     yundama_obj = YDMHttp(name, passwd, app_id, app_key)
#     yundama_obj.login()
#
#     rest = yundama_obj.balance()
#     if rest <= 0:
#         raise Exception('云打码已经欠费了，请及时充值')
#     if rest <= 100:
#         other.warning('云打码余额已不多，请注意及时充值')
#
#     # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
#     cid, result = yundama_obj.decode(file_name, code_type, time_out)
#     return result, yundama_obj, cid
