from flask import Flask
from os import environ

from .extensions import (db, migrate)
from .article import article_bp



def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_CONNECTION')
    db.init_app(app)
    migrate.init_app(app, db)

    #Blueprint register
    app.register_blueprint(article_bp)

    return app

