from flask import request, jsonify, Response

from .dto import ArticleDTO
from .service import getAllArticles, addNewArticle

api = ArticleDTO.api
_article = ArticleDTO.article

@api.route('/articles', methods=['GET'])
def getArticles():
    articles = getAllArticles()
    
    return Response(jsonify(articles))

@api.expect(_article, validate=True)
@api.response(201, 'Article created.')
@api.route('/articles', methods=['POST'])
def addArticle():
    payload = request.json
    article = addNewArticle(payload)

    return jsonify(article)


