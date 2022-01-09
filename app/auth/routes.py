from flask import Blueprint, render_template

from app.forms import signupForm

auth = Blueprint('auth',__name__, template_folder='auth_templates', url_prefix='/auth')

@auth.route('/Login')
def login():
    return render_template('login.html')

@auth.route('/LogoutSuccessful')
def logout():
    return render_template('logout.html')

@auth.route('/Signup')
def sign_up():
    form = signupForm()
    return render_template('signup.html', form=form)