from flask import Blueprint, render_template, request, redirect, url_for
from app.forms import signupForm, signinForm

# imports for working with our User model and signing users up and logins
from app.models import  db, User
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash

auth = Blueprint('auth',__name__, template_folder='auth_templates', url_prefix='/auth')

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = signinForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            print('This user is ready to be checked for correct username and password')
            print(form.username.data, form.password.data)
            return redirect(url_for('dashboard'))
        else:
            print('Bad form input, try again')
            return redirect(url_for('auth.signin'))

    return render_template('signin.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def signup():
    form = signupForm()

    if request.method == 'POST':
        if form.validate_on_submit(): 
            print('successful new user data received')
            new_user = User(form.username.data, form.email.data, form.password.data, form.first_name.data, form.last_name.data) 
            print(f'New user created - {new_user.__dict__}')
            try:
                db.session.add(new_user)
                db.session.commit() # save that change to db

            except:
                print('Username or email taken')
                return redirect(url_for('auth.signup'))

            print('New user registered!')
            login_user(new_user)
            return redirect(url_for('dashboard'))
        else:

            print('Bad form input, try again')
            return redirect(url_for('auth.signup'))

    return render_template('signup.html', form=form)

@auth.route('/logout')
def logout():
    return render_template('logout.html')