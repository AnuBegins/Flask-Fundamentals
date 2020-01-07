from flask import Flask, request, render_template

app = Flask(__name__)
print(__name__)

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route("/users", methods = ['POST'])
def create():
    print(request.form)
    print("Name", request.form["name"])
    print("E-mail", request.form["email"])
    return render_template("created.html")


if __name__ == '__main__':
    app.run(debug=True)