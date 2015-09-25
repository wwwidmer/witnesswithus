__author__ = 'william'

import conf
import urllib2
import json

api_key = conf.MEERKAT_API_KEY

class LoaderUtil(object):
    def __init__(self, v_id):
        self.v_id = v_id
        self.api_url = self.get_api_url();

    def get_viewers(self):
        request = self.api_url
        print request
        try:
            response = urllib2.urlopen(request)
            print response
            data = json.load(response)
            return data['result']['watchersCount']
        except Exception as e:
            print e
            return None

    def get_api_url(self):
        url = 'https://resources.meerkatapp.co/broadcasts/{self.v_id}/watchers?v=1.0'.format(**locals())
        return url
        
