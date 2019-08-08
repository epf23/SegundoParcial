# views.py

#Importar conector MySQL
import mysql.connector

from flask import render_template, request
from flask_table import Table, Col

from app import app

##Conexión a la BD
inf_Activos_Fijos = mysql.connector.connect(
  host="localhost",
  user="estefania",
  passwd="password",
  database="inf_Activos_Fijos"
)
cursor = inf_Activos_Fijos.cursor()



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

@app.route('/Activo_Fijo.html')
def Activo_fijo():
    return render_template("Activo_fijo.html")

@app.route('/Depreciacion.html')
def depreciacion():
    return render_template("Depreciacion.html")

@app.route('/btn_agregar_dp', methods=['POST'])
def btn_agregar_dp():
    ano_proceso = request.form['ano_proceso']
    activos_fijos = request.form['activos_fijos']
    mes_proceso = request.form['mes_proceso']
    fecha_proceso = request.form['fecha_proceso']
    monto_depreciado = request.form['monto_dep']
    depreciacion_acumulada = request.form['dep_acu']
    cuenta_compra = request.form['cuenta_co']
    cuenta_depreciacion = request.form['cuenta_dep']
    valor_compra = cuenta_compra
    ano_dep = ano_proceso
    monto_dep = valor_compra / ano_dep
    dep_ac = monto_dep
    dep_rest = valor_compra - dep_ac
    
    cursor.execute("Insert into inf_Activos_Fijos.calculo_depreciacion (cd_ano_proceso, cd_mes_proceso, id_activos_fijos, cd_fecha_proceso, cd_monto_depreciado, cd_depreciacion_acumulada, cd_cuenta_compra, cd_cuenta_depreciacion) values('"+ano_proceso+"', '"+mes_proceso+"', '"+activos_fijos+"', '"+fecha_proceso+"', "+monto_depreciado+", "+depreciacion_acumulada+"', "+cuenta_compra+", "+cuenta_depreciacion");")
    inf_Activos_Fijos.commit()
    return render_template("Depreciacion.html")

@app.route('/btn_agregar_af', methods=['POST'])
def btn_agregar_af():
    descripcion = request.form['descripcion']
    departamento = request.form['departamento']
    vcompra = request.form['valor_compra']
    depreciacion_acumulada = request.form['depreciacion_acumulada']
    tactivo = request.form['row-1-office']
    fregistro = request.form['fecharegistro']

    cursor.execute("Insert into inf_Activos_Fijos.activos_fijos (act_descripcion, act_departamento, act_tipo_activo, act_fecha_registro, act_valor_compra, act_depreciacion_acumulada) values('"+descripcion+"', '"+departamento+"', '"+tactivo+"', '"+fregistro+"', "+vcompra+", "+depreciacion_acumulada+");")
    inf_Activos_Fijos.commit()
    return render_template("Activo_fijo.html")

@app.route('/btn_agregar_ta', methods=['POST'])
def btn_agregar_ta():
    descripcion = request.form['descripcion']
    ccompra = request.form['cuenta_compra']
    cdepreciacion = request.form['cuenta_depreciacion']
    estado = request.form['row-1-office']

    cursor.execute("Insert into inf_Activos_Fijos.tipo_activos (ta_descripcion, ta_CCCompra, ta_CCDepreciacion, ta_estado) values('"+descripcion+"', '"+ccompra+"', '"+cdepreciacion+"', '"+estado+"');")
    inf_Activos_Fijos.commit()
    return render_template("tipos-de-activos.html")

@app.route('/Empleados.html')
def Empleados():
    return render_template("Empleados.html")

@app.route('/Administracion.html')
def administracion():
    return render_template("Administracion.html")

@app.route('/get_data_ta')
def get_data_ta():
    cursor.execute("select * from `tipo_activos`;")
    data = cursor.fetchall()

@app.route('/btn_agregar_e', methods=['POST'])
def btn_agregar_e():
    nombre = str(request.form.get('nombre', False))
    cedula = str(request.form.get('cedula', False))
    departamento = str(request.form.get('departamento', False))
    fingreso = str(request.form.get('fingreso', False))
    tipopersona = str(request.form.get('row-1-office', False))
    estado = str(request.form.get('row-2-office', False))

    cursor.execute("Insert into inf_Activos_Fijos.empleados (emp_nombre, emp_cedula, emp_departamento, emp_tipo_persona, emp_fecha_ingreso, emp_estado) values('"+nombre+"', '"+cedula+"', '"+departamento+"', '"+tipopersona+"','2019-08-08', '"+estado+"');")
    inf_Activos_Fijos.commit()
    return render_template("Empleados.html")

@app.route('/btn_agregar_a', methods=['POST'])
def btn_agregar_a():
    descripcion = str(request.form.get('descripcion', False))
    estado = str(request.form.get('row-1-office', False))

    cursor.execute("Insert into inf_Activos_Fijos.departamentos (dep_descripcion, dep_estado) values('"+descripcion+"', '"+estado+"');")
    inf_Activos_Fijos.commit()
    return render_template("Administracion.html")

@app.route('/btn_agregar_f', methods=['POST'])
def btn_agregar_f():
    descripcion = request.form['descripcion']
    estado = request.form['row-1-office']

    cursor.execute("Insert into inf_Activos_Fijos.departamentos (dep_descripcion, dep_estado) values('"+descripcion+"', '"+estado+"');")
    inf_Activos_Fijos.commit()
    return render_template("Finanzas.html")

@app.route('/btn_agregar_rh', methods=['POST'])
def btn_agregar_rh():
    descripcion = request.form['descripcion']
    estado = request.form['row-1-office']

    cursor.execute("Insert into inf_Activos_Fijos.departamentos (dep_descripcion, dep_estado) values('"+descripcion+"', '"+estado+"');")
    inf_Activos_Fijos.commit()
    return render_template("Recursos_humanos.html")

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
    cursor.execute("select * from `departamentos`;")
    data = cursor.fetchall()
    print(*data)
    class departamentosTable(Table):
        id = Col('ID')
        descripcion = Col('Descripcion')
        estado = Col('Estado')

    class departamento(object):
        def __init__(self, id, descripcion, estado):
            self.id = id
            self.descripcion = descripcion
            self.estado = estado

    for a, b, c in data:
        print(a,b,c)
        a = a
        b = b
        c = c

    departamentos = [departamento(a, b, c)]
#    departamentos = ""
#    i = 0
#    while i < (len(tabla)%3 == 0):
#        tabla.insert(0,"")
#        departamentos = departamento[(str(tabla[(i*3)+1]), str(tabla[(i*3)+2]), str(tabla[(i*3)+3]))]
#        i +=1

    table = departamentosTable(departamentos)

    return render_template("Finanzas.html", table = table)

@app.route('/Recursos_humanos.html')
def recursos_humanos():
    return render_template("Recursos_humanos.html")

@app.route('/register.html')
def register():
    return render_template("register.html")

@app.route('/tables.html')
def tables():
    return render_template("tables.html")

@app.route('/Tipos-de-activos.html')
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
