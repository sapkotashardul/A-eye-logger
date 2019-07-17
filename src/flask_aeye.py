from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm
from datetime import datetime

#comment

app = Flask(__name__)
app.config['SECRET_KEY'] = '1b64fb8cbda13b37a1ea9a61e725c872'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

class Studies(db.Model):
	id =  db.Column(db.Integer, primary_key=True)
	key = db.Column(db.String(16), unique=True, nullable=False)
	startingDate = db.Column(db.DateTime, nullable=False)
	endingDate = db.Column(db.DateTime, nullable=False)
	sequences= db.relationship('Sequences', backref='author', lazy=True)

	def __repr__(self):
		return f"Studie('{self.startingDate}','{self.endingDate}')"

class Sequences(db.Model)
	id =  db.Column(db.Integer, primary_key=True)
	scene = db.Column(db.String(20), nullable=False)
	cognitiveLoad = db.Column(db.Integer, nullable=False)
	focusPoint = db.Column(db.Integer, nullable=False)
	startingDate = db.Column(db.DateTime, nullable=False)
	endingDate = db.Column(db.DateTime, nullable=False)
	id_study =  db.Column(db.Integer, db.ForeignKey('studies.id'), nullable=False)


	def __repr__(self):
		return f"Sequence('{self scene}','{self.cognitiveLoad}','{self.focusPoint}','{self.startingDate}','{self.endingDate}')"

posts=[
{
	'author':'pouet pouet',
	'title': 'Blog Post 1',
	'content': 'First post ocontent',
	'date_posted' : 'April 21, 2019',
},
{
	'author':'Aristée pouet',
	'title': 'Blog Post 2',
	'content': 'Second post ocontent',
	'date_posted' : 'May 21, 2019',
}]

@app.route("/dashboard")
def dashboard():
	return render_template('dashboard.html', posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.code.data == '315fb1795c0c6b9206841423a06e171d':
			flash('Your data has been collected !', 'success')
			return redirect(url_for('dashboard'))
		else:
			flash('Your key is incorrect. Please try again.', 'danger')
	return render_template('login.html', title='Login', form = form)

if __name__=='__main__':
	app.run(debug=True)