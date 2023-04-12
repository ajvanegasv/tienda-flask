from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import environ

db = SQLAlchemy();
migrate = Migrate();

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_CONNECTION')
    db.init_app(app)
    migrate.init_app(app, db)

    return app