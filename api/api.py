import time
from flask import Flask
from flask import request
from model.main import test,essai,launchMyFlow

app = Flask(__name__, static_folder='../build', static_url_path='/')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')



@app.route('/api/test2')
def getTest():
    un = request.args.get('un')
    deux = request.args.get('deux')
    return {'te': test(int(un),int(deux))}

@app.route('/api/essai')
def getEssai():
    un = request.args.get('un')
    deux = request.args.get('deux')
    return {'te': essai(int(un),int(deux))}

@app.route('/api/launchFlow')
def launchFlow():
    launchMyFlow()
    return {'te': 'ok'}
