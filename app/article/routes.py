from flask import request, jsonify, Response

from . import article_bp
from .services import getAllArticles

@article_bp.route('/articles', methods=['GET'])
def getArticles():
    articles = getAllArticles()
    
    return Response(jsonify(articles))

