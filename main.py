import os
import sys

from flask import Flask, render_template, request

sys.path.append(os.path.join('.', 'modules'))
sys.path.append(os.path.join('.', 'setup'))

import conf


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


def getViewersByHost(host, vid):
    host_util_name = conf.ACCEPTED_HOSTS.get(host)
    if host_util_name:
        host_module = __import__(host_util_name)
        host_util = getattr(host_module, 'LoaderUtil')(vid)
        return host_util.get_viewers()
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
    vid = request.args.get('vid') or request.args.get('user')
    host = request.args.get('host')
    size = request.args.get('size')
    viewers = getViewersByHost(host, vid)
    if viewers is None:
        err = 'Sorry, we can\t find this video at this host'

    return render_template(
        "video.html", size=size, vid=vid, viewers=viewers, url=getUrlByHost(host, vid), err=err
    )


@app.route('/facebook', methods=['GET'])
def facebook(video_id=None):
    facebook_app_id = conf.FACEBOOK_APP_ID
    if video_id is None:
        return render_template(
            "facebook.html", facebook_app_id=facebook_app_id
        )


@app.route('/facebook/<user_id>/<video_id>/<at>', methods=['GET'])
def facebook_live_video(user_id, video_id, at):
    err = None
    facebook_app_id = conf.FACEBOOK_APP_ID
    access_token = at
    return render_template(
        "video.html", user_id=user_id, facebook_app_id=facebook_app_id,
        facebook_video_id=video_id, viewers=0, err=err, access_token=""
    )


if __name__ == '__main__':
    debug = os.environ.get('DEBUG', True)
    if debug is False  and os.environ.get('PROD', False):
        debug = False
    app.run(threaded=True, debug=debug)
