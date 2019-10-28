from json import JSONEncoder
from model.movie import Movie
import json

class MovieEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Movie):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)

