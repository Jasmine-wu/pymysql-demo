import requests
import yaml

from wechat.utils import Utils




def test_env():
    data = {"method":"GET",
            "url":"http://www.baidu.com"
            }
    env = yaml.safe_load(open("env.yaml"))
    data["url"] = str(data["url"]).replace("www.baidu.com", env["www.baidu.com"][env["default"]])
    res = requests.request(**data)
    print(res.content)


