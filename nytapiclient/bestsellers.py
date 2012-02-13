import requests
import simplejson

class BestSellers:

    __API_KEY = '9b10adbc72536a67930154a2bbcfedba:4:62210421'
    __API_DOMAIN = 'http://api.nytimes.com'
    __API_ENDPOINT_ROOT = '/svc/books'
    __API_VERSION = '/v2'
    __API_ENDPOINT_LIST = '/lists'
    __API_ENDPOINT_LIST_NAMES = '/lists/names'
    
    def get_api_url(self, api_endpoint):
        return self.__API_DOMAIN            \
                + self.__API_ENDPOINT_ROOT    \
                + self.__API_VERSION        \
                + api_endpoint
    
    def append_api_key(self, url):
        return url + '?api-key=' + self.__API_KEY
    
    def get_list_names(self):
        url = self.get_api_url(self.__API_ENDPOINT_LIST_NAMES)
        final_url = self.append_api_key(url)

        r = requests.get(final_url)

        j = simplejson.loads(r.content)
        json_results = j[u'results']

        results = []
        for dict_item in json_results:
            results.append(dict_item[u'list_name'])
            
        return results
    
    def get_list(self, list_name):
        url = self.get_api_url(self.__API_ENDPOINT_LIST) + '/' + list_name
        final_url = self.append_api_key(url)
        
        r = requests.get(final_url)
        
        j = simplejson.loads(r.content)
        
        import pprint
        pprint.pprint(j)