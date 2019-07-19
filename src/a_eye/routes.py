from flask import render_template, flash, redirect, url_for
from a_eye import app,db
from a_eye.forms import LoginForm
from a_eye.models import Studies, Sequences
from flask_login import login_user, current_user, logout_user

#key ='68b7ecb4fe9a77eb37642a26c4f39370'

posts={
	'author' : 'lkj',
	'date_posted' :'lkj',
	'content' :'oiejrz',
	'title' : 'lkjer'
}

@app.route("/dashboard")
def dashboard():
	if current_user.is_authenticated:
		sequences = Sequences.query.filter_by(author=current_user)
		print(sequences)
	return render_template('dashboard.html', sequences=sequences)


@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('dashboard'))
	form = LoginForm()
	if form.validate_on_submit():
		study = Studies.query.filter_by(key=form.code.data).first()
		if study:
			login_user(study,True)
			sequences_1 = Sequences.query.filter_by(author=study)
			flash('Your datas has been collected !', 'success')
			return redirect(url_for('dashboard'))
		else:
			flash('Your key is incorrect. Please try again.', 'danger')
	return render_template('login.html', title='Login', form = form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))




#	import secrets
#	do{
#		uniq_key = secrets.token_hex(16)
#		verification = Studies.query.filter_by(key=uniq_key).first()
#	}while(verification)
#	study = Studies(key=uniq_key, startingDate=studyStartingDate, endingDate=studyEndingDate)
#	db.session.add(study)
#	for data in datas
#		sequence = Sequences(scene=data.scene, cognitiveLoad=data.cognitiveLoad, focusPoint=fata.focusPoint, startingDate=data.startingDate, endingDate=data.endingDate, author=study)
#		db.session.add(sequence)
#	db.session.commit()





