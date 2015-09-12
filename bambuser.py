__author__ = 'wwidmer'

import os
import urllib2
import json
import conf


api_key = conf.BAMBUSER_API_KEY
username = conf.BAMBUSER_USERNAME
# bambuser.com/broadcast/.json?username=username?api_key=asdasd

class LoaderUtil(object):
    def __init__(self, v_id):
        self.api_key = api_key
        self.user = username
        self.v_id = str(v_id)
        self.api_url = self.get_api_url()

    def get_viewers(self):
        request = self.api_url
        try:
            response = urllib2.urlopen(request)
            data = json.load(response)
            return data['result']['views_live']
        except:
            return None

    def get_api_url(self):
        url_prefix = "http://api.bambuser.com/broadcast/"
        method = ".json"
        params = ["?api_key=" + self.api_key, "&limit=3"]
        request = os.path.join(url_prefix, self.v_id+method)
        for param in params:
            request += param
        return request
