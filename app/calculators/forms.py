
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

#class rentalincomeForm(FlaskForm):
    #rentalincome = StringField('rentalincome', validators=[DataRequired()])
    #miscsvcincome = StringField('miscsvcincome', validators=[DataRequired()])
    #submit = SubmitField()

#class debtlincomeForm(FlaskForm):
    #rentalincome = StringField('rentalincome', validators=[DataRequired()])
    #miscsvcincome = StringField('miscsvcincome', validators=[DataRequired()])
    #submit = SubmitField()

#class profitincomeForm(FlaskForm):
    #crentalincome = StringField('rentalincome', validators=[DataRequired()])
    #cmiscsvcincome = StringField('miscsvcincome', validators=[DataRequired()])
    #c#csubmit = SubmitField()