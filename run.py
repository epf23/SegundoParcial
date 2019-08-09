# run.py

from app import app

if __name__ == '__main__':
    app.run()

@app.route('/')
def index1():
    return render_template("index.html")
