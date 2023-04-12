import datetime

from app import db

class Article(db.Model):

	__tablename__ = 'article'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	value = db.Column(db.String)
	created_at = db.Column(db.DateTime, default=datetime.datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

	def __init__(self, name, value):
		self.name = name
		self.value = value
	
	def __repr__(self) -> str:
		return f'<Article {self.name}>'