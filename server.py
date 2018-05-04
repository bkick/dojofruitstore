from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry=request.form['strawberry']
    raspberry=request.form['raspberry']
    apple=request.form['apple']
    firstname=request.form['first_name']
    lastname=request.form['last_name']
    ID=request.form['student_id']
    return render_template("checkout.html",apple=apple, strawberry=strawberry,raspberry=raspberry,firstname=firstname,lastname=lastname,ID=ID)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    