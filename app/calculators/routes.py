from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.calculators.forms import initialincomeandexpensesForm, totalincomeandexpensesForm, totalmonthlycashflowForm, requiredinvestmentForm, cashoncashreturnForm

from flask import render_template

calculators = Blueprint('calculators',__name__, template_folder='templates')

@calculators.route('/InitialPropertyIncomeExpenses', methods=['GET', 'POST'])
def incexp():
    form1 = initialincomeandexpensesForm()
    morentalincome = form1.rentalincome.data
    momiscsvcincome = form1.miscsvcincome.data
    moproptax = form1.proptax.data
    moinsurance = form1.insurance.data
    mowatersewer = form1.watersewer.data
    mogarbage = form1.garbage.data
    moelectricity = form1.electricity.data
    mogas = form1.gas.data
    mohoafees = form1.hoafees.data
    molawn = form1.lawn.data
    movacancy = form1.vacancy.data
    morepairs = form1.repairs.data
    mocapex = form1.capex.data
    mopropmgmt = form1.propmgmt.data
    momortgage = form1.mortgage.data

    calc1 = []

    if request.method == 'POST':
        if form1.validate_on_submit():
            res1 = float(morentalincome) + float(momiscsvcincome)
            resonepointfive = int(res1)

            res2 = float(moproptax) + float(moinsurance) + float(mowatersewer) + float(mogarbage) + float(moelectricity) + float(mogas) + float(mohoafees) + float(molawn) + float(movacancy) + float(morepairs) + float(mocapex) + float(mopropmgmt) + float(momortgage)
            restwopointfive = int(res2)

            calc1.append(resonepointfive)
            calc1.append(restwopointfive)

            flash1 = str(resonepointfive)
            flash2 = str(restwopointfive)
            final = (f'Your Monthly Rental Income: ${flash1} & Rental Expenses: ${flash2}')

            print('info received')
            flash(final, category='success')
            return redirect(url_for('moincexp'))
        else:
            print('info not received')

    return render_template('incexp.html', form1=form1, calc1=calc1)

@calculators.route('/MonthlyIncomeExpenses', methods=['GET', 'POST'])
def moincexp():
    form2 = totalincomeandexpensesForm()
    mototalincome = form2.totalincome.data
    mototalexpenses = form2.totalexpenses.data

    calc2 = []

    if request.method == 'POST':
        if form2.validate_on_submit():
            res3 = float(mototalincome) - float(mototalexpenses)
            resthreepointfive = int(res3)
            calc2.append(resthreepointfive)


            flash1 = str(resthreepointfive)
            final = (f'Your Total Monthly Cashflow: ${flash1}')

            print('info received')
            flash(final, category='success')
            return redirect(url_for('mocashflow'))

        else:
            print('info not received')

    return render_template('moincexp.html', form2=form2, calc2=calc2)

# here they only type in monthly cashflow you db return their result so they can enter it and
# you only have them enter annualcashflow at the end to calculate cashoncashreturn
@calculators.route('/MonthlyCashflow', methods=['GET', 'POST'])
def mocashflow():   
    form3 = totalmonthlycashflowForm()
    annualcashflow = form3.totalmonthlycashflow.data

    calc3 = []

    if request.method == 'POST':
        if form3.validate_on_submit():
            res4 = float(annualcashflow)
            resfourpointfive = int(res4) * int(12)
            calc3.append(resfourpointfive)

            flash1 = str(resfourpointfive)
            final = (f'Your Annual Cashflow: ${flash1}')

            print('info received')
            flash(final, category='success')
            return redirect(url_for('requiredinvestment'))

        else:
            print('info not received')

    return render_template('mocashflow.html', form3=form3, calc3=calc3)

@calculators.route('/InvestmentAmount', methods=['GET', 'POST'])
def requiredinvestment():
    form4 = requiredinvestmentForm()
    annualcashflow = form4.annualcashflow.data
    onlydownpayment = form4.downpayment.data
    onlyclosingcosts = form4.closingcosts.data
    onlyrehabbudget = form4.rehabbudget.data
    onlycontingencyfund = form4.contingencyfund.data

    calc4 = []

    if request.method == 'POST':
        if form4.validate_on_submit():
            anncashmath = float(annualcashflow)
            reqinvestmentmath = float(onlydownpayment) + float(onlyclosingcosts) + float(onlyrehabbudget) + float(onlycontingencyfund)

            anncash = int(anncashmath)
            reqinvestment = int(reqinvestmentmath)

            calc4.append(anncash)
            calc4.append(reqinvestmentmath)

            flash1 = str(anncash)
            flash2 = str(reqinvestment)
            final = (f'Your Annual Cashflow: ${flash1} & Required Investment: ${flash2}')

            print('info received')
            flash(final, category='success')
            return redirect(url_for('cashoncash'))
        else:
            print('info not received')

    return render_template('requiredinvestment.html', form4=form4, calc4=calc4)

@calculators.route('/CashonCashReturn', methods=['GET', 'POST'])
def cashoncash():
    form5 = cashoncashreturnForm()
    myannualcashflow = form5.annualcashflow.data
    mytotalinvestment = form5.totalinvestment.data

    calc5 = []

    if request.method == 'POST':
        if form5.validate_on_submit():

            res6 = float(myannualcashflow) / float(mytotalinvestment)
            ressixpointfive = float(res6) * float(100)
            ressixpointfive = round(ressixpointfive, 2)
            calc5.append(ressixpointfive)

            print('info received')
            flash("An ideal Cash on Cash Return is anything higher than or in between 8-12%, if your result is in this range IT'S A DEAL!", category='success')
        else:
            print('info not received')

    return render_template('cashoncash.html', form5=form5, calc5=calc5)