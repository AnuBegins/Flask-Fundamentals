from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods = ['POST'])         
def result():
    result = request.form  #naming the dictionary
    print(result)
    sum_items = int(result["Strawberries"]) + int(result["Blackberries"]) + int(result["Raspberries"]) + int(result["Apples"]) 
        
    return render_template("checkout.html", dict = result, total = sum_items)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug = True)    