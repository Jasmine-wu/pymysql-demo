from wechat.token import Weixin


def test_get_token():
    assert Weixin.get_token() != ""
