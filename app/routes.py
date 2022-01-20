from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/MyDashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/MyRentalBoard')
def rentalboard():
    return render_template('rentalboard.html')

@app.route('/RocketCRM')
def rocketcrm():
    return render_template('rocketcrm.html')

@app.route('/MyWholesaling')
def wholesaling():
    return render_template('wholesaling.html')

@app.route('/MyHouseFlipping')
def flipping():
    return render_template('flipping.html')

@app.route('/MyIncomeExpenses')
def incexp():
    return render_template('incexp.html')