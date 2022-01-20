from flask import Blueprint, render_template, request

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

            print('info received')
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
            print('info received')

        else:
            print('info not received')

    return render_template('moincexp.html', form2=form2, calc2=calc2)


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

            print('info received')
        else:
            print('info not received')

    return render_template('moincexp.html', form3=form3, calc3=calc3)

@calculators.route('/InvestmentAmount', methods=['GET', 'POST'])
def requiredinvestment():
    form4 = requiredinvestmentForm()
    onlydownpayment = form4.downpayment.data
    onlyclosingcosts = form4.closingcosts.data
    onlyrehabbudget = form4.rehabbudget.data
    onlycontingencyfund = form4.contingencyfund.data

    calc4 = []

    if request.method == 'POST':
        if form4.validate_on_submit():
            res5 = float(onlydownpayment) + float(onlyclosingcosts) + float(onlyrehabbudget) + float(onlycontingencyfund)
            resfivepointfive = int(res5)

            calc4.append(resfivepointfive)

            print('info received')
        else:
            print('info not received')

    return render_template('moincexp.html', form4=form4, calc4=calc4)

@calculators.route('/CashonCashReturn', methods=['GET', 'POST'])
def cashoncash():
    form5 = cashoncashreturnForm()
    myannualcashflow = form.annualcashflow.data
    mytotalinvestment = form.totalinvestment.data

    calc5 = []

    if request.method == 'POST':
        if form5.validate_on_submit():

            res6 = float(myannualcashflow) / float(mytotalinvestment)
            ressixpointfive = float(res6) * float(100)
            calc5.append(ressixpointfive)

            print('info received')
        else:
            print('info not received')

    return render_template('moincexp.html', form5=form5, calc5=calc5)

# Coding Option #2 
#----submit form rendering all form results bus only as separate list values [111,222.333]
# found out that I can import numpy, and numpy has various math methods add/divide/multiply:
# numpy.prod(multiply list items)

#@calculators.route('/MyRentalBoard', methods=['GET', 'POST'])
#def rincome():
    #form = rentalinvestingForm()
    #morentalincome = form.rentalincome.data
    #momiscsvcincome = form.miscsvcincome.data
    #moproptax = form.proptax.data
    #moinsurance = form.insurance.data

    #res1 = [morentalincome, momiscsvcincome]
    #res2 = [moproptax, moinsurance]
    #calc1 = [res1, res2]
    #if request.method == 'POST':
        #if form.validate_on_submit():
            #print('info received')  
        #else:
            #print('info not received')

    #return render_template('rentalboard.html', form=form, calc1=calc1, res1=res1, res2=res2)

# Coding Option #1
#----second submit not validating second form only validating first form
#@calculators.route('/MyRentalBoard', methods=['GET', 'POST'])
#def rincome():
    #form = rentalincomeForm()
    #morentalincome = form.rentalincome.data
    #momiscsvcincome = form.miscsvcincome.data
    #form2 = rentalexpensesForm() <--you'll have to create an expenses form for this
    #moproptax = form2.proptax.data
    #moinsurance = form2.insurance.data
    #tmi2 = []
    #tmi3 = []
    #if request.method == 'POST':
        #if form.validate_on_submit():
            #tmi = float(morentalincome) + float(momiscsvcincome)
            #tmi2.append(tmi)
            #print('info received1')  
        #elif form2.validate_on_submit():
            #tmi = float(moproptax) + float(moinsurance)
            #tmi3.append(tmi)
            #print('info received2')
        #else:
            #print('info not received')

    #return render_template('rentalboard.html', form=form, form2=form2, tmi2=tmi2, tmi3=tmi3)

#no returns in if statements have a dictionary