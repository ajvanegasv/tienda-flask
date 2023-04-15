import datetime

from extensions import db

class Article(db.Model):

	__tablename__ = 'articles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	value = db.Column(db.String)
	orders = db.relationship('orders', backref='articles', lazy=True)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

	def __init__(self, name, value):
		self.name = name
		self.value = value
	
	def __repr__(self) -> str:
		return f'<Article {self.name}>'