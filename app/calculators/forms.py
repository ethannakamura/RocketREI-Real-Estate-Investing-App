
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class rentalincomeForm(FlaskForm):
    rentalincome = StringField('rentalincome', validators=[DataRequired()])
    miscsvcincome = StringField('miscsvcincome', validators=[DataRequired()])
    submit = SubmitField()

class debtlincomeForm(FlaskForm):
    rentalincome = StringField('rentalincome', validators=[DataRequired()])
    miscsvcincome = StringField('miscsvcincome', validators=[DataRequired()])
    submit = SubmitField()

class profitincomeForm(FlaskForm):
    rentalincome = StringField('rentalincome', validators=[DataRequired()])
    miscsvcincome = StringField('miscsvcincome', validators=[DataRequired()])
    submit = SubmitField()