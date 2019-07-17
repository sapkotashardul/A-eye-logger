from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	code = StringField('code', validators=[DataRequired()])
	submit = SubmitField ('Show Datas')