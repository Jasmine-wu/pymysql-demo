

from flask import Flask,session,render_template,Markup


app=Flask(__name__)
app.debug=True
# 用session之前必须设置secret_key，否则会被runtime error
app.secret_key='asdfsdfe34454dfdf'
app.config['SESSION_COOKIE_NAME']='xxxxxx'

# Django session设置： 如果SESSION_COOKIE_PATH设置为='/',意思是只要是/下面的路径都会带cookie过来
# 比如/index；意思是只有/index及其以后的路径才会把cookie带过来
# "PERMANENT_SESSION_LIFETIME": timedelta(days=31),
# "SESSION_COOKIE_NAME": "session",
# "SESSION_COOKIE_DOMAIN": None,
# "SESSION_COOKIE_PATH": None,
# "SESSION_COOKIE_HTTPONLY": True,
# "SESSION_COOKIE_SECURE": False,

# Flask把这些session是如何实现的？
# 通过secret_key加密后，当成cookie返回给了浏览器
# 下次发送请求，携带cookie，反解，放到了session中

# cookie放到浏览器并不安全，可以放到redis中
# 这时，数据库地址，端口号，也要放到配置文件中，但是不是内置的参数

def test():
    # return a+b
    return Markup('<input type="text">')

#J9.X0YGQg.Uc9RkCClahhpqXkU7qITS0hrdT8
@app.route('/',methods=['GET'])
def index():

    # 这样设置cookie并不安全，一般放到redis中
    session['key']='asdfasdf'
    session['user']='lqz'
    return 'hello'

@app.route('/order',methods=['GET'])
def order():
    print(session['key'])
    return 'order'
@app.route('/xxx',methods=['GET'])
def xxx():
    return render_template('index.html',aa='lqz',bb=18,cc=test,ll=[1,2,3],name=True,sss='<input type="text">')

if __name__ == '__main__':
    print(app.config)
    app.run(port='8989')
    app.__call__()
    app.session_interface