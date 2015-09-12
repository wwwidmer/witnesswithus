__author__ = 'william'

import conf

api_key = conf.PERISCOPE_API_KEY

class LoaderUtil(object):
    def __init__(self, v_id):
        self.v_id = v_id
        print v_id