from flask import Flask,session,request,redirect,render_template

app = Flask(__name__)
app.debug = False
app.secret_key = 'sdafasdfasdf'


# 请求来了就会触发,类似于django的process_request,
# @app.before_request
# def before2(*args,**kwargs):
#     print('before2222')
#
#
# @app.before_request
# def before(*args,**kwargs):
#     print('before1111')
#     if request.path=='/login':
#         return None
#     else:
#         name=session.get('user')
#         if not name:
#             return redirect('/login')
#         else:
#             return None
#
# # 请求走了就会触发,类似于django的process_response,
# @app.after_request
# def after(response):
#     print('我走了')
#     return response
#
# @app.after_request
# def after2(response):
#     print('我走了222222')
#     return response
#
#
# @app.before_first_request
# def first():
#     print('我的第一次')



# @app.teardown_request  # 用来记录出错日志
# def ter(e):
#     print(e)
#     print('我是teardown_request ')


# 全局标签
@app.template_global()
def sb(a1, a2):
    return a1 + a2

# 全局过滤器
@app.template_filter()
def db(a1, a2, a3):
    return a1 + a2 + a3


# @app.errorhandler(404)
@app.errorhandler(500)
def error_500(arg):
    return render_template('error.html',message='500错误')

@app.errorhandler(404)
def error_404(arg):
    return render_template('error.html',message='404错误')


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('我是login')
    session['user']='lqz'
    return 'hello'

@app.route('/order', methods=['GET'])
def order():
    print('我是order')
    a
    return '我是order页面'

if __name__ == '__main__':
    app.run()
