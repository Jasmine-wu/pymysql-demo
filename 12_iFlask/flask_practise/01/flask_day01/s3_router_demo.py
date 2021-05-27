


from flask import Flask,render_template,request,redirect,session,url_for
app = Flask(__name__)
app.debug = True  # 调试模式
app.secret_key = 'asdfsadfsdafasdfasdf'  # 跟djangosetting中的秘钥一个意思

USERS = {
    1:{'name':'张三','age':18,'gender':'男','text':"道路千万条"},
    2:{'name':'李四','age':28,'gender':'男','text':"安全第一条"},
    3:{'name':'王五','age':18,'gender':'女','text':"行车不规范"},
}

@app.route('/detail/<int:nid>',methods=['GET'])
def detail(nid):
    user = session.get('user_info')
    if not user:
        return redirect('/login')

    info = USERS.get(nid)
    return render_template('detail.html',info=info)


@app.route('/index',methods=['GET'])
def index():
    # 从session中拿出user_info
    user = session.get('user_info')
    if not user:
        # return redirect('/login')
        url = url_for('l1')  # 反向解析
        print(url)
        return redirect(url) # 重定向到login
    return render_template('index.html',user_dict=USERS)


# @
@app.route('/login',methods=['GET','POST'],endpoint='l1')  # endpoint：路由/login的别名，用作反向解析
# @登陆认证装饰器要放到下面来
def login():
    if request.method == "GET":
        print("request.query_string:",request.query_string)
        return render_template('login.html',success='LOGI')
    else:
        # request.query_string
        # post提交过来的数据放在form中
        # get请求提交过来的数据query_string中

        # user/pwd：根据index.html里的name属性
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'lqz' and pwd == '123':
            # 往session中放入key和value
            session['user_info'] = user
            return redirect('/index')
        # error是模版login.html的变量{{error}}
        return render_template('login.html',error='用户名或密码错误')



# 不用路由装饰器，怎么实现路由？如下：
def xxx():
    return 'xxx'
app.add_url_rule('/xxx',view_func=xxx)


if __name__ == '__main__':
    app.run()



'''
学到的
1 @app.route('/login',methods=['GET','POST'],endpoint='l1')，
    -第一个参数是路径，
    -methods=['GET','POST']，请求方式
    -endpoint='l1'，别名，如果不写，使用函数名作为别名，endpoint不能重名，因为反向解析会有问题。
路由的本质：self.add_url_rule

2 一个函数多个装饰器的执行顺序问题：从上到下执行。因此登陆认证装饰器，要当在登陆路由下面。

'''