from flask import Flask, request, redirect, url_for,make_response,Response,jsonify, session, abort
from werkzeug.routing import BaseConverter
from werkzeug.datastructures import FileStorage
import json
from datetime import timedelta

app = Flask(__name__)


@app.errorhandler(404)
def error_404(error):
    return "<h3>您访问的页面去浪迹天涯了</h3> %s" % error



@app.errorhandler(ZeroDivisionError)
def error_zero(error):
    return '除数不能为0'


@app.before_request
def prepare():
    print('before_request')


@app.after_request
def process(response:Response):
    print('after_request:')
    print(response.headers)
    print(response.data)
    print(response.status_code)
    return response


@app.before_first_request
def initial():
    print('before_first_request')


@app.teardown_request
def request_hander(error):
    print('teardown_request : %s' % error)



app.secret_key = 'test'
app.permanent_session_lifetime = timedelta(days=7)
# app = Flask(__name__,static_folder='static1',static_url_path='/res/img')


# class MobileConverter(BaseConverter):
#     regex = '1[3-9]\d{9}$'


# app.url_map.converters['mob'] = MobileConverter

# @app.route("/hello",methods=['get','post'])
# @app.route("/",methods=['get','post'])
# @app.route('/user/<int:userid>')
# @app.route('/user/<mob:mobile>')
# def index(userid):
# def index(mobile):
@app.route('/')
def index():
    print('执行视图')
    a = 1/0
    # abort(500)


    # session['username'] = 'zs'
    # session.permanent = True
    # session.pop("username")
#     print(userid)
#     print(mobile)
#     print(request.url)
#     print(request.method)
#     print(request.headers)
#     print(request.headers.get('Host'))
#     print(request.args.get('name'))
#     print(request.args.get('age'))
#     print(request.form.get('username'))
#     print(request.data)
#     print(request.json.get('age'))
#     file = request.files.get('avatar')
#     print(type(file))
#     file.save('123.jpg')
#     img_bytes = file.read()
#     print(img_bytes)
#     response = make_response('index')
#     response.set_cookie('per_page','10',max_age=86400)
    # response.delete_cookie('per_page')
    # return response
    return "index"


@app.route('/demo1')
def demo1():
    # print(request.cookies.get("per_page"))
    # return 'demo1',400,{'A':40}
    # name = session.get("username")
    # print(name)
    return 'demo1'


@app.route('/demo2')
def demo2():
    response = make_response("hello,flask")
    response.headers['B']=10
    return response


@app.route('/demo3')
def demo3():
    dict1 = {'name': 'zs', 'age': 20}
    # return json.dumps(dict1)
    # return jsonify(dict1)
    return jsonify(name='zs', age=20)


@app.route('/demo4')
def demo4():
    # return redirect("http://www.baidu.com")
    return redirect('/demo3')


if __name__ == "__main__":
    # print(app.url_map)
    # print(app.url_map.converters)
    # for rule in app.url_map.iter_rules():
    #     print(rule.rule,rule.methods,rule.endpoint)
    # app.run(debug=True)
    app.run()






