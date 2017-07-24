from flask import Flask
from flask_restful import Api
from resources.model import Model
from resources.modellist import ModelList

app = Flask(__name__)
api = Api(app)

api.add_resource(Model,'/model/<int:modelId>',endpoint='model')
api.add_resource(ModelList,'/model',endpoint='models')


if __name__ == '__main__':
    app.run(debug=True,threaded=True)

