from flask import render_template, flash, redirect, url_for
from a_eye import app,db
from a_eye.forms import LoginForm
from a_eye.models import Studies, Sequences
from flask_login import login_user, current_user, logout_user
from sqlalchemy import distinct,func
import datetime,time

#key ='68b7ecb4fe9a77eb37642a26c4f39370'



@app.route("/dashboard")
def dashboard():
	if current_user.is_authenticated:
		pourcentage={
			'relaxed' : 0,
			'lowCognitiveLoad' : 0,
			'highCognitiveLoad' : 0,
			'noFocusPoint' : 0,
			'oneFocusPoint' : 0,
			"multipleFocusPoint" : 0
		}

		sequence_datas=[]
		sequences = Sequences.query.filter_by(author=current_user)
		pourcentage['relaxed'] = sequences.filter_by(cognitiveLoad=0).count()
		pourcentage['lowCognitiveLoad'] = sequences.filter_by(cognitiveLoad=1).count()
		pourcentage['highCognitiveLoad'] = sequences.filter_by(cognitiveLoad=2).count()
		pourcentage['noFocusPoint'] = sequences.filter_by(focusPoint=0).count()
		pourcentage['oneFocusPoint'] = sequences.filter_by(focusPoint=1).count()
		pourcentage['multipleFocusPoint'] = sequences.filter_by(focusPoint=2).count()

		s = Sequences.query.filter_by(author=current_user).group_by(Sequences.scene)
		for n in s:
			dico={}
			dico['category_scene']=n.scene
			nb_sequence=sequences.filter_by(scene=n.scene).count()
			category_sequence=sequences.filter_by(scene=n.scene)
			dico['category_nb_sequences']=nb_sequence
			list_date = []
			for seq in category_sequence :
				ss=[]
				ss.append(n.scene)
				ss.append(int(time.mktime(seq.startingDate.timetuple())) * 1000)
				ss.append(int(time.mktime(seq.endingDate.timetuple())) * 1000)
				ss.append(seq.cognitiveLoad)
				ss.append(seq.focusPoint)
				list_date.append(ss)
			dico['category_dates_sequences'] = list_date
			dico['category_startingDate'] = int(time.mktime(current_user.startingDate.timetuple())) * 1000
			dico['category_endingDate'] = int(time.mktime(current_user.endingDate.timetuple())) * 1000
			dico['category_relaxed']=sequences.filter_by(scene=n.scene).filter_by(cognitiveLoad=0).count()
			dico['category_lowCognitiveLoad']=sequences.filter_by(scene=n.scene).filter_by(cognitiveLoad=1).count()
			dico['category_highCognitiveLoad']=sequences.filter_by(scene=n.scene).filter_by(cognitiveLoad=2).count()
			dico['category_noFocusPoint']=sequences.filter_by(scene=n.scene).filter_by(focusPoint=0).count()
			dico['category_oneFocusPoint']=sequences.filter_by(scene=n.scene).filter_by(focusPoint=1).count()
			dico['category_multipleFocusPoint']=sequences.filter_by(scene=n.scene).filter_by(focusPoint=2).count()
			
			sequence_datas.append(dico)

    		
	return render_template('dashboard.html', sequences=sequences, pourcentage=pourcentage,sequence_datas=sequence_datas)


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





