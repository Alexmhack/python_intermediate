from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
	__tablename__ = "flights"
	id = db.Column(db.Integer, primary_key=True)
	origin = db.Column(db.String, nullable=False)
	destination = db.Column(db.String, nullable=False)
	duration = db.Column(db.Integer, nullable=False)
