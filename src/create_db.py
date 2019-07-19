from flask import render_template, flash, redirect, url_for
from a_eye import app,db
from a_eye.forms import LoginForm
from a_eye.models import Studies, Sequences
from flask_login import login_user, current_user, logout_user
import datetime

date1_study1=datetime.datetime(2019,7,19,10,15)
break1_study1 = datetime.datetime(2019,7,19,10,25)
break2_study1 = datetime.datetime(2019,7,19,10,35)
break3_study1 = datetime.datetime(2019,7,19,10,40)
break4_study1 = datetime.datetime(2019,7,19,10,45)
break5_study1 = datetime.datetime(2019,7,19,10,57)
break6_study1 = datetime.datetime(2019,7,19,11)
break7_study1 = datetime.datetime(2019,7,19,11,15)
break8_study1 = datetime.datetime(2019,7,19,11,22)
date2_study1=datetime.datetime(2019,7,19,11,25)

date1_study2=datetime.datetime(2018,5,12,15,26)
break1_study2=datetime.datetime(2018,5,12,15,30)
break2_study2=datetime.datetime(2018,5,12,15,36)
break3_study2=datetime.datetime(2018,5,12,15,41)
break4_study2=datetime.datetime(2018,5,12,15,43)
break5_study2=datetime.datetime(2018,5,12,15,48)
date2_study2=datetime.datetime(2018,5,12,15,52)

# studies_database=[{
# 	'key' : '00a4203ad1851302c7c9cae80b89e55f',
# 	'startinDate' : date1_study1,
# 	'endingDate' : date2_study1,
# },
# {
# 	'key' : '57564ee9efa9b8dbb103ed08ec0995ea',
# 	'startinDate' : date1_study2,
# 	'endingDate' : date2_study2,
# }]

study_1 = Studies(key='00a4203ad1851302c7c9cae80b89e55f',startingDate=date1_study1,endingDate=date2_study1)
study_2 = Studies(key='57564ee9efa9b8dbb103ed08ec0995ea', startingDate=date1_study2,endingDate=date2_study2)

# database=[
# {
# 	'scene' : 'Youtube',
# 	'startingDate' : date1_study1,
# 	'endingDate' : break1_study1,
# 	'cognitiveLoad' : 0,
# 	'focusPoint' : 1,
# 	'author' : study_1

# },
# {
# 	'scene' : 'Youtube',
# 	'startingDate' : date1_study1,
# 	'endingDate' : break1_study1,
# 	'cognitiveLoad' : 0,
# 	'focusPoint' : 1,
# 	'author' : study_1
# }]

database_1=[
{
	'scene' : 'Youtube',
	'startingDate' : break1_study1,
	'endingDate' : break2_study1,
	'cognitiveLoad' : 0,
	'focusPoint' : 2,
	'author' : study_1	
},
{
	'scene' : 'Youtube',
	'startingDate' : break2_study1,
	'endingDate' : break3_study1,
	'cognitiveLoad' : 2,
	'focusPoint' : 2,
	'author' : study_1	
},
{
	'scene' : 'Maths',
	'startingDate' : break3_study1,
	'endingDate' : break4_study1,
	'cognitiveLoad' : 2,
	'focusPoint' : 2,
	'author' : study_1	
},
{
	'scene' : 'Maths',
	'startingDate' : break4_study1,
	'endingDate' : break5_study1,
	'cognitiveLoad' : 1,
	'focusPoint' : 1,
	'author' : study_1	
},
{
	'scene' : 'Environnement',
	'startingDate' : break5_study1,
	'endingDate' : break6_study1,
	'cognitiveLoad' : 0,
	'focusPoint' : 0,
	'author' : study_1	
},
{
	'scene' : 'Environnement',
	'startingDate' : break6_study1,
	'endingDate' : break7_study1,
	'cognitiveLoad' : 2,
	'focusPoint' : 0,
	'author' : study_1	
},
{
	'scene' : 'Environnement',
	'startingDate' : break7_study1,
	'endingDate' : break8_study1,
	'cognitiveLoad' : 0,
	'focusPoint' : 0,
	'author' : study_1	
},
{
	'scene' : 'Environnement',
	'startingDate' : break7_study1,
	'endingDate' : break8_study1,
	'cognitiveLoad' : 2,
	'focusPoint' : 1,
	'author' : study_1	
},
{
	'scene' : 'People',
	'startingDate' : date1_study2,
	'endingDate' : break1_study2,
	'cognitiveLoad' : 1,
	'focusPoint' : 1,
	'author' : study_2	
},
{
	'scene' : 'People',
	'startingDate' : break1_study2,
	'endingDate' : break2_study2,
	'cognitiveLoad' : 2,
	'focusPoint' : 1,
	'author' : study_2	
},
{
	'scene' : 'People',
	'startingDate' : break2_study2,
	'endingDate' : break3_study2,
	'cognitiveLoad' : 2,
	'focusPoint' : 2,
	'author' : study_2	
},
{
	'scene' : 'Youtube',
	'startingDate' : break3_study2,
	'endingDate' : break4_study2,
	'cognitiveLoad' : 2,
	'focusPoint' : 1,
	'author' : study_2	
},
{
	'scene' : 'Youtube',
	'startingDate' : break4_study2,
	'endingDate' : break5_study2,
	'cognitiveLoad' : 1,
	'focusPoint' : 1,
	'author' : study_2	
},
{
	'scene' : 'People',
	'startingDate' : break5_study2,
	'endingDate' : date2_study2,
	'cognitiveLoad' : 0,
	'focusPoint' : 0,
	'author' : study_2	
}
]

db.session.remove()

for data in database_1 :
	db.session.add(Sequences(scene=data['scene'],startingDate=data['startingDate'],endingDate=data['endingDate'],cognitiveLoad=data['cognitiveLoad'], focusPoint=data['focusPoint'], author=data['author']))
db.session.commit()