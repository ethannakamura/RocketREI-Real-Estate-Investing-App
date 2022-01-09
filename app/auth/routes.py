from flask import Blueprint, render_template, request, redirect, url_for

from app.forms import signupForm

auth = Blueprint('auth',__name__, template_folder='auth_templates', url_prefix='/auth')

@auth.route('/Login')
def login():
    return render_template('login.html')

@auth.route('/LogoutSuccessful')
def logout():
    return render_template('logout.html')

@auth.route('/Signup', methods=['GET', 'POST'])
def signup():
    form = signupForm()

    if request.method == 'POST':
        if form.validate_on_submit(): 
            print('successful new user data received')
            print(form.username.data, form.email.data, form.password.data)
            return redirect(url_for('home'))
        else:
            print('Bad form input, try again')
            return redirect(url_for('auth.signup'))

    return render_template('signup.html', form=form)