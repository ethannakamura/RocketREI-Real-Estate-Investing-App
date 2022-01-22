
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#below code was used for Coding Options #2 and #3 in creating calculator forms in the rentalboard route:

class initialincomeandexpensesForm(FlaskForm):
    # - addition - calculate total monthly income
    rentalincome = StringField('rentalincome', validators=[DataRequired()])
    miscsvcincome = StringField('miscsvcincome', validators=[DataRequired()])
    submit = SubmitField('Calculate!')

    # - addition - calculate total monthly expenses 
    proptax = StringField('proptax', validators=[DataRequired()])
    insurance = StringField('insurance', validators=[DataRequired()])
    watersewer = StringField('watersewer', validators=[DataRequired()])
    garbage = StringField('garbage', validators=[DataRequired()])
    electricity = StringField('electric', validators=[DataRequired()])
    gas = StringField('gas', validators=[DataRequired()])
    hoafees = StringField('hoafees', validators=[DataRequired()])
    lawn = StringField('lawn', validators=[DataRequired()])
    vacancy = StringField('vacancy', validators=[DataRequired()])
    repairs = StringField('repairs', validators=[DataRequired()])
    capex = StringField('capex', validators=[DataRequired()])
    propmgmt = StringField('propmgmt', validators=[DataRequired()])
    mortgage = StringField('mortgage', validators=[DataRequired()])
    submit = SubmitField('Calculate!')

class totalincomeandexpensesForm(FlaskForm):
    # - substraction - calculate total monthly cash flow (total income - total expenses)
    totalincome =  StringField('totalincome', validators=[DataRequired()])
    totalexpenses =  StringField('totalincome', validators=[DataRequired()])
    submit = SubmitField('Calculate!')

class totalmonthlycashflowForm(FlaskForm):
    # - multiplication - calculate total monthly income (totalmonthlycashflow * 12)
    totalmonthlycashflow =  StringField('totalincome', validators=[DataRequired()])
    submit = SubmitField('Calculate!')

class requiredinvestmentForm(FlaskForm):
    # - addition - calculate total investment (total investment = dp + cc + rb + cf)
    downpayment = StringField('proptax', validators=[DataRequired()])
    closingcosts = StringField('proptax', validators=[DataRequired()])
    rehabbudget = StringField('proptax', validators=[DataRequired()])
    contingencyfund = StringField('proptax', validators=[DataRequired()])
    submit = SubmitField('Calculate!')

class cashoncashreturnForm(FlaskForm):
    # - division - calculate the cash on cash return (annual cash flow divided(/) by total invesment multiplied(*) by 100)
    annualcashflow = StringField('proptax', validators=[DataRequired()])
    totalinvestment = StringField('proptax', validators=[DataRequired()])
    #cashoncashperecentage = StringField('proptax', validators=[DataRequired()])
    submit = SubmitField('Calculate!')


#below code was used for Coding Options #1 in creating calculator forms in the rentalboard route:

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