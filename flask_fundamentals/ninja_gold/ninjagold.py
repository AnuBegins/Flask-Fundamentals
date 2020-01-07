import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    dict = {
        "Grow-Op": [10,20],
        'Bordello': [5,10],
        'Dojo': [2,5],
        'Ca$ino': [0,50]
    }

    if 'count' not in session:
        session['count'] = 0
    if 'color' not in session:
        session['color'] = 0

    if session['color']  == 1:
        session['color'] = "text-danger"
    else:
        session['color'] = "text-success"

    if 'activity_log' not in session:
        session['activity_log'] = []

    return render_template('index.html', dict = dict)

@app.route('/process_money', methods=['POST'])
def getMoney():
    dict = {
        "Grow-Op": [10,20],
        'Bordello': [5,10],
        'Dojo': [2,5],
        'Ca$ino': [0,50]
    }

    time_stamp = datetime.now().strftime("%Y/%m/%d %I:%M%p")
    location = request.form['getCoin']
    if location == 'Ca$ino':
        casino_up = random.randint(0, 1)  #binary outcome: did player win or lose at casino? If win, variable = 0, else variable = 1
        if casino_up == 0:
            casino_add = random.randrange(1, 51)

        elif casino_up == 1:
            casino_add = random.randrange(-50,0)

        session['color'] = casino_up
        session['count'] += casino_add
        session['count'] = max(session['count'], 0)
        activity = "At casino, won " + str(casino_add) + " pieces of gold.... " + str(time_stamp)
        session['activity_log'].append(activity)
    else:
        coin_range = dict.get(location)
        add_coins = random.randrange(int(coin_range[0]), int(coin_range[1])+1 )
        session['count'] += add_coins
        session['color'] = 0
        activity = 'From the '+location+', got '+ str(add_coins) + " pieces of gold.... "  + str(time_stamp)
        session['activity_log'].append(activity)

    return redirect('/')

@app.route('/reset', methods=['POST'])
def resetSession():
    session.clear()
    return redirect('/')

app.run(debug = True)
