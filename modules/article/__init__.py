from flask import Blueprint
from flask_restx import Api

article_bp = Blueprint('article', __name__);
api = Api(article_bp)

from . import controller
