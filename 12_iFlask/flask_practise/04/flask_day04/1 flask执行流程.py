

from flask import  Flask,jsonify,make_response,request,session,current_app,g


app=Flask(__name__,static_url_path='/static',static_folder='static',template_folder='templates')



# @app.before_first_request  只在app上，蓝图上没有

# app上有，蓝图上也有
# @app.before_request
# @app.after_request
@app.after_request
def xx(response):
    # 如果处理session，session就会被修改
    return response
@app.route('/')
def index():
    res=make_response('hello')
    print(request)  # 代理模式
    print(request.method)
    print(session)
    return res

if __name__ == '__main__':
    app.run()
    # 请求来了会执行app()--->__call__
    # app()
    app.__call__