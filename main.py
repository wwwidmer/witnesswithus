from flask import Flask, render_template, request
import conf


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


def getViewersByHost(host, vid):
    host_util_name = conf.ACCEPTED_HOSTS.get(host)
    if host_util_name:
        try:
            host_module = __import__(host_util_name)
            host_util = getattr(host_module, 'LoaderUtil')(vid)
            return host_util.get_viewers()
        except Exception as e:
            print e
    else:
        return None

def getUrlByHost(host, vid):
    host_util = conf.ACCEPTED_HOSTS.get(host)
    if host_util:
        pass
    else:
        return None

@app.route('/counter', methods=['GET'])
def counter():
    err = ''
    vid =  request.args.get('vid')
    host = request.args.get('host')
    size = request.args.get('size')
    viewers = getViewersByHost(host, vid)
    if viewers is None:
        err = 'Sorry, we can\t find this video at this host'

    return render_template("video.html", size=size, vid=vid, viewers=viewers, url=getUrlByHost(host, vid), err=err)


if __name__ == '__main__':
    app.run()
