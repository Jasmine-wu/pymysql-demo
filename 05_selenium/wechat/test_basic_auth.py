import requests
from requests.auth import HTTPBasicAuth


def test_basic_auth():
    res = requests.request("GET",
                           "http://httpbin.org/basic-auth/haha/123",
                           auth=HTTPBasicAuth("haha", "123")
                           )
    print(res.json())
