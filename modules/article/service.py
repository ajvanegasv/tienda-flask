from models import Article
from .dto import ArticleDTO

def getAllArticles():
    articles = Article.query.all()

    return articles

def addNewArticle(payload):
    newArticle = Article(
        name=payload.name,
        value=payload.value
    )

    return newArticle

