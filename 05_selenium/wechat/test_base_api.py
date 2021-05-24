from wechat.base_api import BaseApi
from wechat.token import Weixin


class Test_base(BaseApi):
    def setup_class(self):
        pass

    def test_send(self):
        # base = BaseApi()
        # data = {}
        # base.send(data)
        #
        pass

    def test_send_encode(self):
        base = BaseApi()
        data = {
            "method": "GET",
            "url": "http://localhost:9999/demo1.txt"
        }
        base.send_encrypt(data, encoding="base64")

        # data2 = {
        #     "method": "GET",
        #     "url": "http://localhost:9999/demo2.txt"
        # }
        # base.send_encrypt(data, encoding="md5")

    def test_template(self):
        token = Weixin.get_token()
        ID = 44
        data = {"token": token,
                "id": ID
                }

        content = self.load("contact/steps/department.yaml")
        # print(content)

        step = self.get_step(content, "update")
        print(step)
        print(type(step))

        data = self.template(step, data)
        print(data)


    def test_append(self):
        data = {"method": "GET",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete?",
                "params": {"access_token": "$token", "id": "$id"},

                }
        self.append("./contact/steps/department.yaml", data)
