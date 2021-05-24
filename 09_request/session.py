import requests

# 获取验证码:http://localhost/index.php?m=Home&c=User&a=verify
# 登录用户:(username: 13088888888, password: 123456, verify_code: 1234)
# 登录:http://localhost/index.php?m=Home&c=User&a=do_login
# 我的订单:http://localhost/Home/Order/order_list.html

session = requests.session()
response = session.get("http://localhost/index.php?m=Home&c=User&a=verify")
url = "http://localhost/index.php?m=Home&c=User&a=do_login"
# (username: 13088888888, password: 123456, verify_code: 1234)
jsonData = {
    "username":"13088888888",
    "password": "123456",
    "verify_code": "1234"
}
session.post(url=url, json=jsonData)

