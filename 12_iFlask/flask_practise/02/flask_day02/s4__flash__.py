

from flask import Flask,request,jsonify,make_response,session,flash,get_flashed_messages


app=Flask(__name__)
app.debug=True
app.secret_key='sdafasdfasdf'
@app.route('/',methods=['GET','POST'])
def index():
    # flash('lqz-nb')  # 往某个位置放值
    flash('lqz',category='error1')
    return 'hello'

@app.route('/order',methods=['GET','POST'])
def order():
    # res=get_flashed_messages()
    res=get_flashed_messages(category_filter=['error1'])
    print(res)
    return  'cccc' # 从某个位置取出来

@app.route('/order2',methods=['GET','POST'])
def order2():
    # res=get_flashed_messages()
    # res=get_flashed_messages(category_filter=['error1'])
    res=get_flashed_messages(category_filter=['error1'])
    print(res)
    return  'dsadfsda' # 从某个位置取出来
if __name__ == '__main__':
    app.run()
