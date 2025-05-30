from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Texter!"

@app.route('/login')
def login():
    return "Login Page"
