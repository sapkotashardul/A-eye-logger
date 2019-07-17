from datetime import datetime
from a_eye import db

class Studies(db.Model):
	id =  db.Column(db.Integer, primary_key=True)
	key = db.Column(db.String(16), unique=True, nullable=False)
	startingDate = db.Column(db.DateTime, nullable=False)
	endingDate = db.Column(db.DateTime, nullable=False)
	sequences = db.relationship('Sequences', backref='author', lazy=True)

	def __repr__(self):
		return f"Studies('{self.startingDate}','{self.endingDate}')"

class Sequences(db.Model):
	id =  db.Column(db.Integer, primary_key=True)
	scene = db.Column(db.String(20), nullable=False)
	cognitiveLoad = db.Column(db.Integer, nullable=False)
	focusPoint = db.Column(db.Integer, nullable=False)
	startingDate = db.Column(db.DateTime, nullable=False)
	endingDate = db.Column(db.DateTime, nullable=False)
	id_study =  db.Column(db.Integer, db.ForeignKey('studies.id'), nullable=False)


	def __repr__(self):
		return f"Sequence('{self.scene}','{self.cognitiveLoad}','{self.focusPoint}','{self.startingDate}','{self.endingDate}')"
		
