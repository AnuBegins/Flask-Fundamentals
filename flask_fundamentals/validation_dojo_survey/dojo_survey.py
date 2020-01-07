from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="whisper"

# our index route will handle rendering our form
@app.route('/')
def index():
    dojo_list = ['San Jose', 'Seattle', 'Austin', 'Chicago','Tulsa' ]
    language_list = ['None', 'Python', 'Java', 'JavaScript', 'C#', 'C++' ]
    return render_template("index.html", dojo_list = dojo_list, language_list=language_list)

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

    if len(request.form['Name']) < 1:
        flash('This field cannot be empty.')
        return redirect('/')
    if len(request.form['Message']) < 1:
        flash('Please add a comment')
        return redirect('/')
    elif len(request.form['Message']) >= 121:
        flash('Comment is longer than 120 characters.')
        return redirect('/')
   
    #print("Name:", request.form["Name"])
    #print("Dojo:", request.form['Dojo'])
    #print("Language", request.form['Language'])
    #print("Message", request.form['Message'])

    return render_template("result.html", result = result)

@app.route('/danger')
def danger():
    print("User tried to visit /danger. Redirected to /")
    return redirect('/') # redirects back to the '/' route

@app.route('/reset', methods=['POST'])
def resetSession():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug = True) #run the server
