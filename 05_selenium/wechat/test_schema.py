import pytest
import json
import requests
import logging
import jsonpath
from hamcrest import *
from jsonschema import validate


class TestRequests():
    logging.basicConfig(level=logging.INFO)

    def test_get(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))

    def test_post(self):
        # 加proxies，用charles调试，不加代理,可以不用proxies+verify，同时要把charles关闭
        # resp= requests.post("https://testerhome.com/api/v3/topics.json?limit=2",
        #                     json={"1":"value1"},
        #
        #                     proxies={"http":"http://127.0.0.1:8888"},
        #                     verify=False)
        resp = requests.request("POST", "https://testerhome.com/api/v3/topics.json?limit=2",
                                json={"1": "value1"},
                                headers={"headerkey": "headervalue"},
                                proxies={"https": "http://127.0.0.1:8888"},
                                verify=False)
        print(resp.text)

    def test_cookie(self):
        # curl - H
        # 'Host: stock.xueqiu.com' - H
        # 'Cookie: xq_a_token=626b6e88da01737d12728f56a806fe197d8158b1;u=5497564746;session_id=;xid=0' - H
        # 'x-device-model-name: Netease_MuMu' - H
        # 'x-device-os: Android 6.0.1' - H
        # 'user-agent: Xueqiu Android 12.1.1' - H
        # 'accept-language: en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4' - -compressed
        # 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?_t=1NETEASE9c46f713ee5de1f96acaaecf1f4b52b7.5497564746.1618378834202.1618378975710&_s=06ee83&category=1&pid=-1&size=10000&x=0.63&page=1'
        url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?'
        params = {
            "category": "1",
        }
        header = {
            "user-agent": "Xueqiu Android 12.1.1",
        }

        # token会过期
        cookie = {"xq_a_token": "626b6e88da01737d12728f56a806fe197d8158b1",
                  "u": "5497564746"
                  }

        resp = requests.get(url,
                            params,
                            headers=header,
                            cookies=cookie,
                            proxies={"https": "http://127.0.0.1:8888"},
                            verify=False
                            )
        print(json.dumps(resp.json(), indent=2))

        assert resp.json()["data"]["category"] == 1
        assert resp.json()["data"]["stocks"][0]["symbol"] == "BABA"
        print(jsonpath.jsonpath(resp.json(), "$.data.stocks[?(@.symbol=='BABA')].name"))
        # assert jsonpath.jsonpath(resp.json(), "$.data.stocks[?(@.symbol=='BABA')].name")[0] == "阿里巴巴"
        #判断当symbol是BABA的时候，name是不是阿里巴巴
        assert_that(jsonpath.jsonpath(resp.json(), "$.data.stocks[?(@.symbol=='BABA')].name")[0], equal_to("阿里巴巴"),
                    "比较上市代码和上市公司名字")

    def test_harm(self):
        assert_that(70, close_to(80, 30))

        assert_that(['a', 'b'], has_item('a'))

        assert_that(['a', 'b', 'c'], has_items('b', 'a'))

        # 只要匹配任何一个条件
        assert_that(['a', 'b', 'c'], any_of(
            has_items('b', 'a'),
            has_items('c', 'd')
        ))

        # 所有条件都要匹配
        assert_that(['a', 'b', 'c'], all_of(
            has_items('b', 'a'),
            has_items('a', 'd')
        ))

    def test_all(self):
        url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?'
        params = {
            "category": "1",
        }
        header = {
            "user-agent": "Xueqiu Android 12.1.1",
        }

        # token会过期
        cookie = {"xq_a_token": "626b6e88da01737d12728f56a806fe197d8158b1",
                  "u": "5497564746"
                  }

        resp = requests.get(url,
                            params,
                            headers=header,
                            cookies=cookie,
                            proxies={"https": "http://127.0.0.1:8888"},
                            verify=False
                            )
        print(json.dumps(resp.json(), indent=2))

        # 断言里只要出现阿里巴巴或者京东就是对的
        print(jsonpath.jsonpath(resp.json(), "$..name"))
        assert_that(jsonpath.jsonpath(resp.json(), "$..name"), any_of(
            has_item("阿里巴巴"),
            has_item("京东"),
        ))

    def test_schema(self):
        url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json?'
        params = {
            "category": "1",
        }
        header = {
            "user-agent": "Xueqiu Android 12.1.1",
        }

        # token会过期
        cookie = {"xq_a_token": "626b6e88da01737d12728f56a806fe197d8158b1",
                  "u": "5497564746"
                  }

        resp = requests.get(url,
                            params,
                            headers=header,
                            cookies=cookie,
                            proxies={"https": "http://127.0.0.1:8888"},
                            verify=False
                            )
        print(json.dumps(resp.json(), indent=2))
        with open("list_schema.json", encoding="utf-8") as f:
            schema = json.load(f)
        validate(instance=resp.json(), schema=schema)


