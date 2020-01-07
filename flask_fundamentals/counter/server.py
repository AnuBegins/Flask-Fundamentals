from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def visits():
    if 'visits' not in session:
        session['visits'] = 1
    session['visits'] = session['visits']
    return render_template("index.html", visits = int(session["visits"]))

@app.route('/increment', methods=['POST'])
def increment():
    session['visits'] += 2
    return redirect('/') 

@app.route('/destroy_session')
def destroy():
    print("Visits is:", session["visits"])
    session.clear()
    return redirect('/')

# if __name__=="__main__":
app.run(debug=True) #run the server
