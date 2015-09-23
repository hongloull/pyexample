import json

s = '{"name": "ACME", "shares": 50, "price": 490.1}'


class JsonObj(object):

    def __init__(self, d):
        self.__dict__ = d


obj = json.loads(s, object_hook=JsonObj)
print(obj.name)
