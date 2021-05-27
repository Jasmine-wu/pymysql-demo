
from flask import  Flask,session,make_response,jsonify
from utils import SQLHelper
app =Flask(__name__ ,static_url_path='/static' ,static_folder='static' ,template_folder='templates')





@app.route('/')
def index():
    res=SQLHelper.fetch_all(sql='select * from boy where id=%s',args=[1,])
    print(res)
    return jsonify(res)


if __name__ == '__main__':
    app.run()