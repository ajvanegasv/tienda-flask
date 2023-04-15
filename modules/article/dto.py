from flask_restx import Namespace, fields

class ArticleDTO:
    api = Namespace('article', description='article related operations')
    article = api.model('article', {
        'name': fields.String(required=True, description='article name'),
        'value': fields.String(required=True, description='article value')
    })