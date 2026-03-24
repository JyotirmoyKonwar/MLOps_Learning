from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to da dawg house!</h1></html>"

@app.route("/index",methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Yo! {name}!'
    return render_template('form.html')

@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Yo! {name}!'
    return render_template('form.html')

@app.route('/success/<int:score>') # variable rule
def success(score):
    return "Yo marks is "+ str(score)

@app.route('/result/<int:score>')
def result(score):
    res=""
    if score>=  50:
        res = "PASS"
    else:
        res = "FAIL"

    exp = {'score':score, 'res':res }

    return render_template('result1.html',result = exp)

if __name__ == "__main__":
    app.run(debug=True)