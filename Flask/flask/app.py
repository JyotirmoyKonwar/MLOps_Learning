from flask import Flask

'''
Creating an instance of the Flask Class which will be the WSGI(Web Server Gateway Interface) application.
'''
# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to da dawg house!"

@app.route("/index")
def index():
    return "Dis is da index"


if __name__ == "__main__":
    app.run(debug=True)