# views.py

from flask import render_template

from app import app

@app.route('/')
def index1():
    return render_template("index.html")

@app.route('/index.html')
def index2():
    return render_template("index.html")

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/forgot-password.html')
def forgot_password():
    return render_template("forgot-password.html")


@app.route('/404.html')
def p404():
    return render_template("404.html")

@app.route('/Administracion.html')
def administracion():
    return render_template("Administracion.html")

@app.route('/blank.html')
def blank():
    return render_template("blank.html")

@app.route('/buttons.html')
def buttons():
    return render_template("buttons.html")

@app.route('/cards.html')
def cards():
    return render_template("cards.html")

@app.route('/charts.html')
def charts():
    return render_template("charts.html")

@app.route('/Finanzas.html')
def finanzas():
    return render_template("Finanzas.html")

@app.route('/Recursos_humanos.html')
def recursos_humanos():
    return render_template("Recursos_humanos.html")

@app.route('/register.html')
def register():
    return render_template("register.html")

@app.route('/tables.html')
def tables():
    return render_template("tables.html")

@app.route('/tipos-de-activos.html')
def tipos_de_activos():
    return render_template("tipos-de-activos.html")

@app.route('/utilities-animation.html')
def utilities_animation():
    return render_template("utilities-animation.html")

@app.route('/utilities-border.html')
def utilities_border():
    return render_template("utilities-border.html")

@app.route('/utilities-color.html')
def utilities_color():
    return render_template("utilities-color.html")

@app.route('/utilities-other.html')
def utilities_other():
    return render_template("utilities-other.html")
