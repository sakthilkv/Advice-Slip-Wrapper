"""
Python wrapper for `Advice Slip` API at https://api.adviceslip.com/.

:author:     --  Sakthi LK
:link:       --  https://github.com/SakthiLKV
:license:    --  MIT License - http://www.opensource.org/licenses/mit-license.php
"""
import requests

base_url = "https://api.adviceslip.com/"

def get_dump(param):
    return requests.get(base_url + param).json()
     
class RandomAdvice(object):

    def __init__(self):
            data = get_dump('advice')
            try:
                self.data = data['slip']
            except:
                pass
    
    @property
    def advice(self) -> str:
        return self.data['advice']

    @property
    def id(self) -> int:
        return self.data['id']

class AdviceByID(object):
    def __init__(self,id):
        data = get_dump('advice/{}'.format(id))
        try:
            self.data = data['slip']
        except:
            pass

    @property
    def advice(self) -> str:
        try:
            return self.data['advice']
        except:
           return "ID is invalid."

    @property
    def id(self) -> int:
        try:
            return self.data['id']
        except:
           return "ID is invalid."

class SearchAdvice(object):
    def __init__(self,query):
        try:
            self.data = get_dump('advice/search/{}'.format(query))
        except:
            pass
    
    @property
    def total_results(self) -> str:
        try:
            return self.data['total_results']
        except:
           return "Query is invalid."

    @property
    def result(self):
        try:
            return self.data['slips']
        except:
           return "Query is invalid."
