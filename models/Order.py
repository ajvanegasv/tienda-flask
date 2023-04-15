import datetime

from extensions import db

class Order(db.Model):

    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.Integer, db.ForeignKey('articles.id'))
    city = db.Column(db.String(100))
    total = db.Column(db.Integer)
    address = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __init__(self, article, city, address) -> None:
        self.article = article
        self.city = city
        self.address = address

    def __repr__(self) -> str:
        return f'<Order {self.id}>'
