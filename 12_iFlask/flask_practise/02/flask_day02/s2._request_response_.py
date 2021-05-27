

from flask import Flask,request,jsonify,make_response


app=Flask(__name__)
app.debug=True


@app.route('/',methods=['GET','POST'])
def index():


    from werkzeug.datastructures import CombinedMultiDict
    # request.method  提交的方法
    # request.args  get请求提及的数据,是个字典
    # request.form   post请求提交的数据
    # request.values  post和get提交的数据总和
    # request.cookies  客户端所带的cookie

    # request.headers  请求头
    # request.path     不带域名，请求路径

    # # request.full_path  不带域名，带参数的请求路径

    # request.url           带域名带参数的请求路径

    # request.base_url		带域名请求路径
    # request.url_root      域名
    # request.host_url		域名
    # request.host			127.0.0.1:500
    # request.files
    # print(request.args.get("xxx"))
    # print(request.url)
    # print(request.url_root)
    # print(request.host_url)
    # print(request.host)
    # print(request.full_path)
    # print(request.path)
    # print(request.cookies)
    # print(request.method)
    # print(type(request.args))
    # from werkzeug.datastructures import ImmutableMultiDict
    # print(request.args.get('name'))
    # print(request.query_string)  # get形式提交的数据，需要自己转
    #
    # print(request.values)
    # print(request.values['name'])
    # print(request.values['xxx'])
    # print(request.values.getlist('name'))


    # 响应对象
    # 响应相关信息
    # return "字符串"
    # return render_template('html模板路径',**{})
    # return redirect('/index.html')
    # 对着django，JsonResponse
    # return jsonify({'k1':'v1'})

    # 设置cookie
    aa='hello world'
    res=make_response(aa)
    res.set_cookie('xxx','lqz')

    # 往响应头中放东西
    res.headers['X-Something'] = 'A value'
    print(type(res))
    from  flask.wrappers import Response
    return res

    # response = make_response(render_template('index.html'))
    # response是flask.wrappers.Response类型
    # response.delete_cookie('key')
    # response.set_cookie('key', 'value')
    # response.headers['X-Something'] = 'A value'
    # return response
    # return 'hello'


if __name__ == '__main__':
    print(app.config)
    app.run(port=8080)
    app.__call__()