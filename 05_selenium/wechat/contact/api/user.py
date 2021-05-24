import requests

from wechat.base_api import BaseApi
from wechat.token import Weixin


class User(BaseApi):

    def list(self, department_id=1, fetch_child=0):
        data = {"method": "POST",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?",
                "params": {"access_token": Weixin.get_token(),
                           "department_id": department_id,
                           "fetch_child": fetch_child}
                }
        return self.send(data)

    def create(self, dic=None, data=None):
        data = {"method": "POST",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create?",
                "params": {"access_token": Weixin.get_token()},
                "json": dic,
                "data": data
                }
        return self.send(data)
