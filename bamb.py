__author__ = 'wwidmer'

import os
import urllib2
import json
import conf


api_key = conf.BAMBUSER_API_KEY
username = conf.BAMBUSER_USERNAME

class BambuserUtil(object):
    def __init__(self, v_id):
        self.api_key = api_key
        self.user = username
        self.v_id = str(v_id)

    def get_all_json_data(self):
        request = self.getURL()
        try:
            response = urllib2.urlopen(request)
            data = json.load(response)
            return data['result']#['vid']#['views_total']
        except:
            return "ERROR REQUEST DENIED"

    def get_api_url(self):
        bamburl = "http://api.bambuser.com"
        form = "broadcast"
        method = ".json"
        params = ["?api_key=" + self.api_key, "&limit=3"]
        request = os.path.join(bamburl, form, self.v_id, method)
        request += params
        return request
