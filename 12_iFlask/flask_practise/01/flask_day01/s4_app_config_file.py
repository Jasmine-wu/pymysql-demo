


from flask import Flask,request,render_template,redirect


app=Flask(__name__)
# 第一种方式(小项目，很少用)
# app的配置文件全在config字典中，但是有一些常用的，比如debug，会直接提到app这一层
# app.debug=True
# app.config['DEBUG'] = False

# 第二种方式（像django）
# app.config.from_pyfile("settings.py")

# 第三种（用到最多，推荐）
app.config.from_object("mysettings.DevelopmentConfig")

@app.route('/')
# 相当于放了index=decorator(index)
def index():
    return redirect('/hello')

@app.route('/hello',endpoint='hello',defaults={'n1':'xxx'},strict_slashes=False,redirect_to='http://www.baidu.com')
def hello(n1):
    print(n1)
    return 'hello'


if __name__ == '__main__':
    app.run()
