from re import L
from flask import Blueprint, render_template, request, redirect, url_for

from app.forms import signupForm, signinForm

auth = Blueprint('auth',__name__, template_folder='auth_templates', url_prefix='/auth')

@auth.route('/Login', methods=['GET', 'POST'])
def login():
    form = signinForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            print('This user is ready to be checked for correct username and password')
            print(form.username.data, form.password.data)
            return redirect(url_for('dashboard'))
        else:
            print('Bad form input, try again')
            return redirect(url_for('auth.login'))

    return render_template('login.html', form=form)

@auth.route('/LogoutSuccessful')
def logout():
    return render_template('logout.html')

@auth.route('/register', methods=['GET', 'POST'])
def signup():
    form = signupForm()

    if request.method =='POST':
        print(form.username.data, form.email.data, form.password.data)
        if form.validate_on_submit(): 
            print('successful new user data received')
            print(form.username.data, form.email.data, form.password.data)
            return redirect(url_for('dashboard'))
        else:
            print('Bad form input, try again')
            return redirect(url_for('auth.signup'))

    return render_template('signup.html', form=form)