# run.py

from app import app
from flask import flask

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
