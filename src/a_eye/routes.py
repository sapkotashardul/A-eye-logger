from flask import render_template, flash, redirect, url_for
from a_eye import app
from a_eye.forms import LoginForm
from a_eye.models import Studies, Sequences

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
