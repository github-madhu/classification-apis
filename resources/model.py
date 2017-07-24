from flask_restful import Resource,reqparse
from Models.modeldao import ModelDAO
import json
from common.jsonencoder import MyEncoder


parser = reqparse.RequestParser()


class Model(Resource):
    def get(self,modelId):
     object =  ModelDAO('121','7/18/2017','abc',123,'http://xyz.com')
     return json.dumps(object.__dict__)


