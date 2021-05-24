from wechat.base_test import BaseTest
from wechat.contact.api.user import User
from wechat.utils import Utils


class TestUser(BaseTest):
    @classmethod
    def setup_class(cls):
        cls.user = User()

    def test_add_by_template(self):
        mobile = Utils.udid()[0:11]
        data = Utils.parse_template("../steps/user_template.json",
                                    {
                                        "userid": Utils.udid(),
                                        "name": "杭三" + mobile,
                                        "mobile": mobile,
                                        "email": mobile + "@163.com"
                                    }
                                    )

        res = self.user.create(data=data.encode("utf-8"))
        assert res["errcode"] == 0
        assert res["errmsg"] == "created"

    def test_add(self):
        pass

    def test_get_list(self):
        assert res["errcode"] == 0
        assert res["errmsg"] == "ok"
