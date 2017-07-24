from Models.modeldao import ModelDAO
from flask_restful import Resource, reqparse
import json
import werkzeug




parser= reqparse.RequestParser()

parser.add_argument('file',type=werkzeug.datastructures.FileStorage,location='files',required=True,help="The training data file is required")



class ModelList(Resource):
    def get(self):
        models=[];
        model1=ModelDAO('121','7/18/2017','abc',123,'http://xyz.com')
        model2=ModelDAO('555','7/18/2017','abc',123,'http://xyz.com')
        models.append(model1)
        models.append(model2)
        return json.dumps([o.__dict__ for o in models])

    def post(self):
        args=parser.parse_args()
        csvfile=args.file



