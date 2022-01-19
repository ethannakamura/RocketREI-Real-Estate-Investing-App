from flask import Blueprint, render_template, request

from app.calculators.forms import rentalinvestingForm

from flask import render_template

calculators = Blueprint('calculators',__name__, template_folder='templates')

@calculators.route('/MyRentalBoard', methods=['GET', 'POST'])
def rincome():
    form = rentalinvestingForm()
    morentalincome = form.rentalincome.data
    momiscsvcincome = form.miscsvcincome.data
    moproptax = form.proptax.data
    moinsurance = form.insurance.data
    mowatersewer = form.watersewer.data
    mogarbage = form.garbage.data
    moelectricity = form.electricity.data
    mogas = form.gas.data
    mohoafees = form.hoafees.data
    molawn = form.lawn.data
    movacancy = form.vacancy.data
    morepairs = form.repairs.data
    mocapex = form.capex.data
    mopropmgmt = form.propmgmt.data
    momortgage = form.mortgage.data
    mototalincome = form.totalincome.data
    mototalexpenses = form.totalexpenses.data

    calc1 = []
    if request.method == 'POST':
        if form.validate_on_submit():
            res1 = float(morentalincome) + float(momiscsvcincome)
            resonepointfive = int(res1)
            res2 = float(moproptax) + float(moinsurance) + float(mowatersewer) + float(mogarbage) + float(moelectricity) + float(mogas) + float(mohoafees) + float(molawn) + float(movacancy) + float(morepairs) + float(mocapex) + float(mopropmgmt) + float(momortgage)
            restwopointfive = int(res2)
            res3 = float(mototalincome) + float(mototalexpenses)
            resthreepointfive = int(res3)
            calc1.append(resonepointfive)
            calc1.append(restwopointfive)
            calc1.append(resthreepointfive)
            print('info received') 
        else:
            print('info not received')

    return render_template('rentalboard.html', form=form, calc1=calc1)

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