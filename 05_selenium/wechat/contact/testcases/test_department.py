import pytest

from wechat.base_test import BaseTest
from wechat.contact.api.department import Department
from wechat.token import Weixin


class TestDepartment(BaseTest):

    @classmethod
    def setup_class(cls):
        cls.department = Department()

    @pytest.mark.parametrize("name, parentID", {
        ("广州研0000", 1),
        ("교센터333333", 1),
        ("廣技術中心666666", 1)
    })
    def test_create_success(self, name, parentID):
        #
        data = {"token": Weixin.get_token(),
                "data": {
                    "name": name,
                    "parentid": parentID,
                },
                "json": ""
                }

        ## 是否是同一父部门下部门名重名
        try:
            assert "created" == self.department.create(data)["errmsg"]

        except AssertionError as e:
            if "department existed" in e.__str__():

                if self.department.is_exist_name(parentID, name) != 0:
                    id = self.department.is_exist_name(parentID, name)

                self.department.delete(id)

                res = self.department.create(data)
                assert res["errcode"] == 0
                assert res["errmsg"] == "created"
        print(res)

    def test_create_depth_success(self):
        pass
        # for i in range(50):
        #     data = {
        #         "name": "河北研发中心" + str(time.time()).replace(".", ""),
        #         "parentid": i
        #     }
        #
        #     # print(res.json())

    def test_update(self):
        pass

    @pytest.mark.parametrize("id", {55, 56})
    def test_delete_success(self, id):
        data = {"id": id,
                "token": Weixin.token()
                }
        try:
            res = self.department.delete(data)
            assert "deleted" == res["errmsg"]
        except AssertionError as e:
            print(e.__str__())
        else:
            assert "deleted" == res["errmsg"]

    def test_list_all(self):
        data = {"id": None,
                "token": Weixin.token()
                }
        self.print_json(self.department.list(data))

    @pytest.mark.parametrize("id", {5, 7})
    def test_list_by_id(self, id):
        data = {"id": id,
                "token": Weixin.token()
                }
        res = self.department.list(data)

        assert res["errcode"] == 0
        assert res["errmsg"] == "ok"
