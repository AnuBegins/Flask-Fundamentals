# Write a program that generates an HTML page that looks like a checkerboard.  For this assignment, you're allowed to use <table> if you want.  You could use <div> if desired.  (Note: During Web Fundamentals, we discouraged you from using <table> as we didn't want you to use <table> to position different contents of your website on different parts of the table.  For this assignment however, you are allowed to use <table>.)

#http://localhost:5000 - should display 8 by 8 checkerboard
#http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)

from flask import Flask, request, render_template

app = Flask(__name__)
print(__name__)

@app.route('/')
@app.route('//')
def printBoard():
    return render_template("checkerboard.html", cols = 8, rowz = 8)

@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/')
def printBoard1(x,y):
    return render_template("checkerboard.html", cols = x, rowz = y)

if __name__ == '__main__':
    app.run(debug=True)