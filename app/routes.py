from app import db
from flask import render_template, current_app as app
from flask_login import login_required

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/MyRentalBoard')
@login_required
def rentalboard():
    return render_template('rentalboard.html')

@app.route('/RocketCRM')
@login_required
def rocketcrm():
    return render_template('rocketcrm.html')

@app.route('/MyWholesaling')
@login_required
def wholesaling():
    return render_template('wholesaling.html')

@app.route('/MyHouseFlipping')
def flipping():
    return render_template('flipping.html')

@app.route('/InitialPropertyIncomeExpenses')
@login_required
def incexp():
    return render_template('incexp.html')

@app.route('/MonthlyIncomeExpenses')
@login_required
def moincexp():
    return render_template('moincexp.html')

@app.route('/MonthlyCashflow')
@login_required
def mocashflow():
    return render_template('mocashflow.html')

@app.route('/InvestmentAmount')
@login_required
def requiredinvestment():
    return render_template('requiredinvestment.html')

@app.route('/CashonCashReturn')
@login_required
def cashoncash():
    return render_template('cashoncash.html')

@app.route('/FairMarketRent')
@login_required
def fairmarketrent():
    return render_template('fairmarketrent.html')


@app.route('/Loggedout')
def Goodbye():
    return render_template('logout.html')
