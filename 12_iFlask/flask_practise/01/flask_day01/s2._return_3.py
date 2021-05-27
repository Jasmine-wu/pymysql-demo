
from flask import Flask,request,render_template,redirect


app=Flask(__name__)

@app.route('/')
def index():

    # return render_template('index.html')
    # return redirect('http://www.baidu.com')
    return redirect('/hello')

@app.route('/hello')
def hello():
    return 'hello'
'''
django            flask
HttpResponse---->直接字符串
render()----->render_template('index.html')
redirect()---->redirect()
'''

if __name__ == '__main__':
    app.run()
