from flask import Blueprint
from flask_restx import Api

api = Blueprint('article', __name__);
api = Api(api)

from . import controller
