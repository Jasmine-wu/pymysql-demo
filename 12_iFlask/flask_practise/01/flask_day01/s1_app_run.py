
from flask import Flask,request

app=Flask(__name__)

@app.route('/')   # 装饰器加括号和不加括号的区别
def index():
    # 当前请求地址，当前请求携带过来的数据
    print(request.path)
    return 'hello world'

@app.route('/hello')
def hello():

    print(request.path)
    return 'hello hellohello'
if __name__ == '__main__':
    app.run()
    # 请求来了，会执行 app(request),会触发谁？触发__call__方法


'''
        ctx = self.request_context(environ)
        error = None
        try:
            try:
                ctx.push()
                response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.handle_exception(e)
            except:
                error = sys.exc_info()[1]
                raise
            return response(environ, start_response)
        finally:
            if self.should_ignore_error(error):
                error = None
            ctx.auto_pop(error)
'''