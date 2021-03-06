from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
from datetime import datetime, date, time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

app = Flask(__name__)
app.secret_key = 'whisper'

def validate():
    errors = 0
    #Check first name
    if request.form['firstName'] == '':
        flash('Name cannot be blank', 'firstNameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['firstName']) == True:
        flash('Name cannot have numbers', 'firstNameError')
        errors += 1
        pass
    else:
        session['firstName'] = request.form['firstName']

    #Check last name
    if request.form['lastName'] == '':
        flash('Name cannot be blank', 'lastNameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['lastName']) == True:
        flash('Name cannot have numbers', 'lastNameError')
        errors += 1
        pass
    else:
        session['lastName'] = request.form['lastName']

    #Check birthdate
    if request.form['birthdate'] == '':
        flash('Please select Date of Birth', 'dateError')
        errors += 1
        pass
    else:
        session['birthdate'] = request.form['birthdate']
        now = datetime.now()
        birthDate = datetime.strptime(session['birthdate'], "%Y-%m-%d")

        if now > birthDate:
            pass
        else:
            errors += 1
            flash('D.O.B. must be in the past', 'dateError')

    #Check email
    if request.form['email'] == '':
        flash('E-mail cannot be blank', 'emailError')
        errors += 1
        pass
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid e-mail address', 'emailError')
        errors += 1
        pass
    else:
        session['email'] = request.form['email']

    #Check password
    if request.form['password'] == '':
        flash('Password cannot be blank', 'passwordError')
        errors += 1
        pass
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters', 'passwordError')
        errors += 1
        pass
    elif not passwordRegex.match(request.form['password']):
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'passwordError')
    else:
        session['password'] = request.form['password']

    #Check confirmation password
    if request.form['confirmPassword'] == '':
        flash('Please confirm password', 'confirmPasswordError')
        errors += 1
        pass
    elif request.form['confirmPassword'] != request.form['password']:
        flash('Passwords do not match', 'confirmPasswordError')
        errors += 1
    else:
        session['confirmPassword'] = request.form['confirmPassword']

    #See if there are any errors
    if errors > 0:
        session['password'] = ''
        session['confirmPassword'] = ''
        return False
    else:
        return True

@app.route('/')
def index():
    if 'firstName' not in session:
        session['firstName'] = ''
    if 'lastName' not in session:
        session['lastName'] = ''
    if 'birthdate' not in session:
        session['birthdate'] = ''
    if 'email' not in session:
        session['email'] = ''
    if 'password' not in session:
        session['password'] = ''
    if 'confirmPassword' not in session:
        session['confirmPassword'] = ''

    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_user():
    if validate() == False:
        return redirect('/')
    return redirect('/process')

@app.route('/process')
def show_user():
    return render_template('results.html')

@app.route('/clear', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)