

# 当程序执行都某个位置，会自动触发某些操作（咱们写代码实现），异步操作



from flask import  Flask,signals
from flask.signals import _signals

app=Flask(__name__,static_url_path='/static',static_folder='static',template_folder='templates')


######### 内置信号的使用
##第一步写一个函数（触发某些动作）
# 往信号中注册函数
def func(*args,**kwargs):
    print(args[0])  # 当前app对象
    print('触发信号',args,kwargs)
# 第二步：函数跟内置信号绑定
signals.request_started.connect(func)


def func1(*args,**kwargs):
    print(args)
    print(kwargs)
    import time
    time.sleep(100)
    print('触发信号',args,kwargs)
signals.request_finished.connect(func1)



### 自定义信号

# 自定义信号
# #第一步：定义一个信号
# xxxxx = _signals.signal('xxxxx')
# # 第二步：定义一个函数
# def func3(*args,**kwargs):
#     import time
#     time.sleep(1)
#     print('触发信号',args,kwargs)
# #第三步：信号跟函数绑定
# xxxxx.connect(func3)

#第四步：触发信号

@app.route('/')
def index():
    # xxxxx.send(1,k='2')
    # xxxxx.send()
    # xxxxx.send(1)

    return 'xxx'

if __name__ == '__main__':
    app.run(threaded=False)
