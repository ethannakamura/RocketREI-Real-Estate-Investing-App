from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/InitialPropertyIncomeExpenses')
def incexp():
    return render_template('incexp.html')

@app.route('/MonthlyIncomeExpenses')
def moincexp():
    return render_template('moincexp.html')

@app.route('/MonthlyCashflow')
def mocashflow():
    return render_template('mocashflow.html')

@app.route('/InvestmentAmount')
def requiredinvestment():
    return render_template('requiredinvestment.html')

@app.route('/CashonCashReturn')
def cashoncash():
    return render_template('cashoncash.html')

@app.route('/Loggedout')
def Goodbye():
    return render_template('logout.html')