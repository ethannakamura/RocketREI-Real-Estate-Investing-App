from distutils.log import warn
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import signupForm, signinForm, updateUsernameForm, updateUsernameForm

# imports for working with our User model and signing users up and logins
from app.models import  db, User
from flask_login import login_user, logout_user, current_user, login_required, user_accessed
from werkzeug.security import check_password_hash

auth = Blueprint('auth',__name__, template_folder='auth_templates', url_prefix='/auth')

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = signinForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            print('This user is ready to be checked for correct username and password')
            print(form.username.data, form.password.data)
            user = User.query.filter_by(username=form.username.data).first()
            if user is None or not check_password_hash(user.password, form.password.data):
                #username didn't exist or user gave the wrong password
                flash('_INCORRECT_USERNAME_OR_PASSWORD_PLEASE_TRY_AGAIN', category='danger')
                return redirect(url_for('auth.signin'))
            
            # there's an implied else here - the username & pass matched a user in our db
            login_user(user)
            print(current_user, current_user.__dict__)
            flash(f'_LOGIN_SUCCESSFUL', category='success')
            return redirect(url_for('auth.dashboard'))

        else:
            flash('_INCORRECT_USERNAME_OR_PASSWORD_PLEASE_TRY_AGAIN', category='danger')
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
                flash('_USERNAME_OR_EMAIL_TAKEN_PLEASE_TRY_AGAIN', category='danger')
                return redirect(url_for('auth.signup'))

            login_user(new_user)
            flash(f'_YOUR_ACCOUNT_HAS_BEEN_CREATED', category='success')
            return redirect(url_for('auth.signin'))
        else:

            flash('_INCORRECT_USERNAME_OR_PASSWORD_PLEASE_TRY_AGAIN', category='danger')
            return redirect(url_for('auth.signup'))

    return render_template('signup.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('_COME_BACK_SOON!', category='success')
    return redirect(url_for('Goodbye'))

@auth.route('/MyDashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = updateUsernameForm()
    if request.method == 'POST':
        if form.validate_on_submit() and check_password_hash(current_user.password, form.password.data):
            if User.query.filter_by(username=form.newusername.data).first():
                flash('_USERNAME_ALREADY_TAKEN_PLEASE_TRY_A_DIFFERENT_USERNAME', category='danger')
                return redirect(url_for('auth.profile'))
            else:
                current_user.username = form.newusername.data
                db.session.commit()
                flash('_USERNAME_UPDATE_SUCCESSFUL!', category='success')    
                return redirect(url_for('auth.profile'))
        else: 
            flash('_INCORRECT_PASSWORD_PLEASE_TRY_AGAIN', category='danger')    
            return redirect(url_for('auth.profile'))

    return render_template('profile.html', form=form)

