#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 23:00:42 2018

@author: ArunRam
"""
# Create a server file that generates 5 different http responses for the following 5 url requests:

# localhost:5000 - have it say "Hello World!" - Hint: If you have only one route that your server is listening for, it must be your root route ("/")
# localhost:5000/dojo - have it say "Dojo!"

# localhost:5000/say/flask - have it say "Hi Flask".  Have function say() handle this routing request.
# localhost:5000/say/michael - have it say "Hi Michael" (have the same function say() handle this routing request)
# localhost:5000/say/john - have it say "Hi John!" (have the same function say() handle this routing request)

# localhost:5000/repeat/35/hello - have it say "hello" 35 times! - You will need to convert a string "35" to an integer 35.  To do this use int().  For example int("35") returns 35.  If the user request localhost:5000/repeat/80/hello, it should say "hello" 80 times.
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times! (have this be handled by the same route function as #6)


from flask import Flask, request  # Import Flask and other modules to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
print(__name__)          # Just for fun, print __name__ to see what it is
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    return 'Hello World !'  # Return the string 'Hello World!' as a response.

@app.route('/dojo')
def dojo():
    print("-"*80)
    print("Dojo!")
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    print(name)
    if name == "John":
        return "Hi "+name+"!"
    return "Hi "+name

@app.route('/repeat/<count>/<strng>')
def repeat(count,strng):
    counter = int(count)
    strng = strng+" "
    return strng * counter
    

# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(name)
#     return "hello "+name

# @app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id


if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
