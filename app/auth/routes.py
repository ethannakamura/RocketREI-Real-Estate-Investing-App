from flask import Blueprint, render_template
auth = Blueprint('auth',__name__, template_folder='auth_templates')

@auth.route('/Login')
def login():
    return render_template('login.html')

@auth.route('/LogoutSuccessful')
def logout():
    return render_template('logout.html')

@auth.route('/Signup')
def sign_up():
    return render_template('signup.html')