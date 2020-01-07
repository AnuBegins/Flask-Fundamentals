from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def play(x=3):
    return render_template("playground.html", times = int(x), color = "blue")

@app.route("/play/<x>")
def playTimes(x):
    return render_template("playground.html", times = int(x), color = "blue")

@app.route("/play/<x>/<color>")
def playTimesColor(x, color):
    return render_template("playground.html", times = int(x), color = color)

if __name__=='__main__':


    app.run(debug=True)