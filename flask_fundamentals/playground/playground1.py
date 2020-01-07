#Level 1 Playground
#When a user visits http://localhost:5000/play, have it render 
#three beautiful looking blue boxes.  Please use a template to render this.

from flask import Flask, request, render_template

app = Flask(__name__)
print(__name__)

@app.route('/')

@app.route('/play')
@app.route('/play/')
def printBlockz():
    return render_template("index.html", blocks = 3, color = "blue")

@app.route('/play/<int:count>')
@app.route('/play/<int:count>/')
def printBlocks(count):
    return render_template("index.html", blocks = count, color = "blue")

@app.route('/play/<int:count>/<color>')
@app.route('/play/<int:count>/<color>/')
def printBlocksColor(count, color):
    return render_template("index.html", blocks = count, color = color)

if __name__ == '__main__':
    app.run(debug=True)