
from csv import reader
from io import StringIO

import requests
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)




@app.route('/')
def index():
    return "Welcome to Configuration Service!"




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
