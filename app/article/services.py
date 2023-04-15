from app.models import Article

def getAllArticles():
    articles = Article.query.all()

    return articles
