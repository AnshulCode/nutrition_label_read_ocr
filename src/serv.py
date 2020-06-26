import flask
from flask import Flask,request

serv = Flask(__name__)

@serv.route('/',methods = ['POST'])
def entry():
    if request.method == 'POST':
        print("request sent")
    return'hello world'

if __name__ == '__main__':
    serv.run(host='127.0.0.1',port = 3000)