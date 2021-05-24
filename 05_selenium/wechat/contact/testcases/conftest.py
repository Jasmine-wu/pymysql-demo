import pytest

from wechat.token import Weixin


@pytest.fixture(scope="session")
def token():
    return Weixin.get_token()