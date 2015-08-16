__author__ = 'wwidmer'

import urllib2
import json


# bambuser.com/broadcast/json?username=swillwodmer?api_key=asbdbahsdhsdjbasd

api_key = "dcc4ffb5afd1e14049e8dda4c0d5b0c3"
username = "swillwodmor"

class BambConnector(object):
    def __init__(self, username, v_id, api_key):
        self.api_key = api_key
        self.user = username
        self.v_id = v_id

    def getJsonData(self):
        request = self.getURL()
        try:
            response = urllib2.urlopen(request)
            data = json.load(response)
            return data['result']#['vid']#['views_total']
        except:
            return "ERROR REQUEST DENIED"

    def getURL(self):
        bamburl = "http://api.bambuser.com/"
        form = "broadcast"
        method = ".json"
        params = ["?api_key="+self.api_key, "&limit=3"]
        request = bamburl + form + "/" + str(self.v_id) + method + params[0] #+ params[1]
        return request
