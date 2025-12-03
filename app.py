from flask import Flask, render_template, request

app = Flask(__name__)

app.route('/', methods = ['GET', 'POST'])
def home():
    if request.methods == 'POST':
        