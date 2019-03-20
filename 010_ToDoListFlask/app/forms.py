from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class NewForm(FlaskForm):
    newtodo = TextAreaField('So? What next?', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Add')