from app.models import Article
from app import db

def getAllArticles():
    articles = db.session.execute(Article).scalars()

    return articles
