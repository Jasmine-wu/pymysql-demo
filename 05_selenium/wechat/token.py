import os
import yaml

from wechat.base_api import BaseApi


class Weixin(BaseApi):
    _token = ""

    @classmethod
    def get_token(cls):
        if len(cls._token) == 0:
            cls._token = cls.token()
        return cls._token

    @classmethod
    def token(cls):
        cwd = os.getcwd()
        cwd_path = cwd.split("wechat")[0] + "wechat/weixin.yaml"
        print(cwd_path)
        with open(cwd_path, encoding="utf-8") as f:
            env = yaml.safe_load(f)["env"]
        corpid = env["corpid"]
        corpsecret = env["corpsecret"]

        data = {"method": "GET",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken?",
                "params": {"corpid": corpid,
                           "corpsecret": corpsecret
                           }
                }

        return cls.send(cls, data)["access_token"]
