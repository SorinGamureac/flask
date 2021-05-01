from flask import Flask, request

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "This is a GET request"
    return "This is a POST request"

