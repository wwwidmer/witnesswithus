import os
import sys
from flask import Flask, render_template, request
from bamb import BambUserUtil


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


def getViewersByHost(host, vid):
    return 0

def getUrlByHost(host, vid):
    pass
    
@app.route('/counter', methods=['GET'])
def counter():
    vid = request.args.get('vid') 
    host = request.args.get('host')
    size = request.args.get('size')
    viewers = getViewersByHost(host, vid)
    

    return render_template("video.html", size=size, vid=vid, viewers=int(viewers),url=getUrlByHost(host, vid))


if __name__ == '__main__':
    app.run()
