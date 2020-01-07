from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes
# Routing rules and rest of server.py below

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

# the server is listening for a POST request to:
# localhost:5000/users
# we define the route below such that the route matches the action of our form - '/users'
# similarly we need to allow specific methods - 'POST' in this case

#submitting the form takes us to the POST /users route, which is handled by the create_user function, where we store the POST data in session
#the create_user method redirects us teo the GET /show route, which is handled by the show_user function, whre we render the user.html template and pass along the necessary info to the view
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    if 'name' in session:
        print('name exists!')
    else:
        print("key 'name' does NOT exist")

    # recall the name attributes we added to our form inputs
    # to access the data that the user input into the fields we use request.form['name_of_input']
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show') # redirects to the page that shows name and email

@app.route('/show', methods=['GET'])
def show_user():
    return render_template('user.html')

if __name__=="__main__":
    app.run(debug=True) #run the server
