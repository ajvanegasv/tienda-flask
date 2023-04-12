from flask import request, jsonify

from . import article_bp
from .services import getAllArticles


@article_bp.route('/articles')
def getArticles():
    articles = getAllArticles()

    return jsonify(articles)


