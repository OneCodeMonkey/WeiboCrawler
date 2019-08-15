import json,time,requests
from logger.log import other


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
        data = {
            'method': 'login',
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
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {
            'method': 'upload',
            'username': self.username,
            'password': self.password,
            'appid': self.appid,
            'appkey': self.appkey,
            'codetype': str(codetype),
            'timeout': str(timeout)
        }
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
        data = {
            'method': 'result',
            'username': self.username,
            'password': self.password,
            'appid': self.appid,
            'appkey': self.appkey,
            'cid': str(cid)
        }
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, filename, codetype, timeout):
        cid = self.upload(filename, codetype, timeout)
        if cid > 0:
            for i in range(0, timeout):
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
            if requests['ret']:
                return response['ret']
        else:
            return -9001

def code_verificate(name, password, filename, codetype=1005, app_id=3510, app_key='7281f8452aa559cdad6673684aa8f575', timeout=60):
        """
        :param name: 用户名
        :param password:
        :param filename:
        :param codetype:
        :param app_id:
        :param app_key:
        :param timeout:
        :return:
        """
        yundama_obj = YDMHttp(name, password, app_id, app_key)
        yundama_obj.login()

        rest = yundama_obj.balance()
        if rest <= 0:
            raise Exception('云打码账号欠费，需要充值才能使用')
        if rest <= 100:
            other.warning('云打码余额不多，请注意及时充值')

        # 开始识别验证码
        cid, result = yundama_obj.decode(filename, codetype, timeout)
        return result, yundama_obj, cid

if __name__ == '__main__':
    username = 'AAAAA'
    password = 'PPPPP'
    rs = code_verificate(username, password, 'pincode.png')