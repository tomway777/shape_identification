from flask import Blueprint
from flask_restful import Api
from resources.identifier import Identifier

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


#Router api
api.add_resource(Identifier, '/identifier')











