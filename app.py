from flask import Flask, request
import qiniu
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/token')
def gen_token():
    ak = request.args['ak']
    sk = request.args['sk']
    key = request.args['key']
    bucket = request.args['bucket']
    q = qiniu.Auth(access_key=ak, secret_key=sk)
    if key:
        bucket = bucket+":"+key
    token = q.upload_token(bucket)
    return token

@app.route('/url')
def gen_private_url():
    ak = request.args['ak']
    sk = request.args['sk']
    url = request.args['url']
    q = qiniu.Auth(access_key=ak, secret_key=sk)
    pu = q.private_download_url(url)
    return pu