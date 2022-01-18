from flask import Blueprint, render_template, request

from app.calculators.forms import debtlincomeForm, profitincomeForm, rentalincomeForm

from flask import render_template

calculators = Blueprint('calculators',__name__, template_folder='templates')

@calculators.route('/MyRentalBoard', methods=['GET', 'POST'])
def rincome():
    form = rentalincomeForm()
    morentalincome = form.rentalincome.data
    momiscsvcincome = form.miscsvcincome.data
    form2 = debtlincomeForm()
    morentalincome = form2.rentalincome.data
    momiscsvcincome = form2.miscsvcincome.data
    form3 = profitincomeForm()
    morentalincome = form3.rentalincome.data
    momiscsvcincome = form3.miscsvcincome.data
    tmi2 = []
    tmi3 = []
    if request.method == 'POST':
        if form.validate_on_submit():
            tmi = float(morentalincome) + float(momiscsvcincome)
            tmi2.append(tmi)
            print('info received')  
        elif form2.validate_on_submit():
            tmi = float(morentalincome) + float(momiscsvcincome)
            tmi3.append(tmi)
            print('info received2')
        elif form3.validate_on_submit():
            tmi = morentalincome + momiscsvcincome
            print('info received3')
        else:
            print('info not received')

    return render_template('rentalboard.html', form=form, form2=form2, tmi2=tmi2, tmi3=tmi3)

#@calculators.route('/MyRentalBoard', methods=['GET', 'POST'])
#def rincome():
    #form = rentalincomeForm()
    #morentalincome = form.rentalincome.data
    #momiscsvcincome = form.miscsvcincome.data
    #form2 = debtlincomeForm()
    #morentalincome = form2.rentalincome.data
    #momiscsvcincome = form2.miscsvcincome.data
    #form3 = profitincomeForm()
    #morentalincome = form3.rentalincome.data
    #momiscsvcincome = form3.miscsvcincome.data
    #tmi2 = []
    #tmi3 = []
    #if request.method == 'POST':
        #if form.validate_on_submit():
            #tmi = float(morentalincome) + float(momiscsvcincome)
            #tmi2.append(tmi)
            #print('info received')  
        #elif form2.validate_on_submit():
            #tmi = float(morentalincome) + float(momiscsvcincome)
            #tmi3.append(tmi)
            #print('info received2')
        #elif form3.validate_on_submit():
            #tmi = morentalincome + momiscsvcincome
            #print('info received3')
        #else:
            #print('info not received')

    #return render_template('rentalboard.html', form=form, form2=form2, tmi2=tmi2, tmi3=tmi3)

#no returns in if statements have a dictionary