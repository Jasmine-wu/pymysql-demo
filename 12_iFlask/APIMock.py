import json

from flask import Flask, request


# 创建一个应用对象
app = Flask(__name__)


# 定义视图函数，设置路由规则
@app.route("/index")
def index():
    print("访问的index主页")
    return "hello mock"

@app.route("/api/sys/login",methods=["POST"])
def login():
    result = json.loads(request.get_data().decode("utf-8"))
    mobile = result.get("mobile")
    password = result.get("password")
    print(mobile, password)
    if mobile == "138000000002" and password == "123456":
        data = {
            "success" : True,
            "code" : 10000,
            "message" : "操作成功",
            "token" : "ajsdfj-12312-szs-fd-fds"
        }
    else:
        data = {
            "success": False,
            "code": 999999,
            "message": "抱歉，系统繁忙没请稍候重试",
            "token": None
        }
    return data

if __name__ == '__main__':
    app.run()