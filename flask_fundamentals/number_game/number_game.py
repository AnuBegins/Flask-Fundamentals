#Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.

#In order to generate a random number you can use the "random" python module

#In order to remove something from the session, you must pop() it off of the session dictionary. Alternatively, you may use other built-in dictionary methods, such as clear().


from flask import Flask, render_template, request, redirect, session
import random  #imports python's 'random' module
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
    session['randInt'] = random.randrange(0,100)
    print("Random int is:", session['randInt'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if guess < session['randInt']:
        # print("guest is", guess,". Too low")
        response = "Too low. Try a larger integer."
        style = "danger"
        return render_template("index.html", response = response, guess=guess, style = style)
    elif guess > session['randInt']:
        # print("guest is", guess,". Too high")
        response = "Too high ! Try again."
        style = "warning"
        return render_template("index.html", response = response, guess=guess, style = style)
    else:
        response = "Bingo! The number was "+str(session['randInt'])
        style = "success"
        return render_template("index.html", response = response, guess=guess, style = style)

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

# if __name__=="__main__":
app.run(debug=True) #run the server
