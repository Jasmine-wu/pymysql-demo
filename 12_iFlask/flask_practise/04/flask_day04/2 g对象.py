
from flask import  Flask ,jsonify ,make_response ,request ,session ,current_app ,g

# g是一个全局变量，再当次请求当中一直有效



app =Flask(__name__ ,static_url_path='/static' ,static_folder='static' ,template_folder='templates')
@app.before_request
def aaaa():
    # 当次请求的g对象中放值
    g.name='lqz'
    # 在整个请求过程中不要往request对象中放东西，而要向g中放


@app.after_request
def after(response):
    print(g.name)
    return response
@app.route('/')
def index():
    print(g.name)
    res =make_response('hello')
    return res

if __name__ == '__main__':
    app.run()