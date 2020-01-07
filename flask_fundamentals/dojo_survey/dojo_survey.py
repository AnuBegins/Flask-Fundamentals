from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

# the server is listening for a POST request to:
# localhost:5000/users
# we define the route below such that the route matches the action of our form - '/users'
# similarly we need to allow specific methods - 'POST' in this case

@app.route('/result', methods=['POST'])
def result():
    print("Got Post Info")
    result = request.form
    print(result)

    # recall the name attributes we added to our form inputs
    # to access the data that the user input into the fields we use request.form['name_of_input']

    # name = request.form["Name"]
    print("Name:", request.form["Name"])

    # dojo = request.form['dojo']
    print("Dojo:", request.form['Dojo'])

    # language = request.form['language']
    print("Language", request.form['Language'])
    
    # message = request.form['message']
    print("Message", request.form['Message'])

    return render_template("result.html", result = result)

@app.route('/danger')
def danger():
    print("User tried to visit /danger. Redirected to /")
    return redirect('/') # redirects back to the '/' route

if __name__=="__main__":
    app.run(debug = True) #run the server
