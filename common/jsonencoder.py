from json import JSONEncoder
import json


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
