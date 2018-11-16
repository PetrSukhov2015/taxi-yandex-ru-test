import requests

class HttpRequest(object):
    def __init__(self,url,data=None):
        self.url=url
        self.data=data

    def get_code(self):

        proxyDict = {'https': 'https://sukhov:123@firewall:3128'}
        proxyDict = {'http': 'http://sukhov:123@firewall:3128'}
        response = requests.get(self.url,proxies=proxyDict)
        if '200'!=response.status_code:
            print (response.text)
