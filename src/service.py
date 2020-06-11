from flask import Flask,request
from PIL import Image

service = Flask(__name__)

@service.route('/',methods = ['GET','POST'])
def entry():
    return 'ok'
if __name__ == '__main__':
    service.run(host = '127.0.0.1',port = 1900)