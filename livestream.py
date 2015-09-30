
import urllib2
import json


class LoaderUtil(object):
    def __init__(self, user):
        self.user = user.replace('_', '-')
        self.api_url = self.get_api_url()

    def get_viewers(self):
        request = self.api_url
        try:
            response = (urllib2.urlopen(request))
            data = json.load(response)
            return data['channel']['currentViewerCount']
        except:
            return None

    def get_api_url(self):
        url_suffix = '.api.channel.livestream.com/2.0/info.json'
        url_prefix = 'http://x'+self.user+'x'
        return url_prefix+url_suffix
