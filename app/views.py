# views.py

#Importar conector MySQL
import mysql.connector

from flask import render_template, request
from flask_table import Table, Col

from app import app

##Conexión a la BD
inf_Activos_Fijos = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin",
  database="inf_Activos_Fijos"
)
cursor = inf_Activos_Fijos.cursor()



@app.route('/')
def index1():
    return render_template("index.html")

@app.route('/index.html')
def index2():
    return render_template("index.html")

@app.route('/404.html')
def p404():
    return render_template("404.html")

@app.route('/Activo_Fijo.html')
def Activo_fijo():
    cursor.execute("select * from `activos_fijos`;")
    data = cursor.fetchall()
    print(*data)
    class activos_fijosTable(Table):
        id = Col('ID')
        descripcion = Col('Descripcion')
        departamento = Col('Departamento')
        tipo_activo = Col('Tipo de Activo')
        fecha_registro = Col('Fecha de Registro')
        valor_compra = Col('Valor Compra')
        depreciacion_acumulada = Col('Depreciación Acumulada')

    class activos_fijo(object):
        def __init__(self, id, descripcion, departamento, tipo_activo, fecha_registro, valor_compra, depreciacion_acumulada):
            self.id = id
            self.descripcion = descripcion
            self.departamento = departamento
            self.tipo_activo = tipo_activo
            self.fecha_registro = fecha_registro
            self.valor_compra = valor_compra
            self.depreciacion_acumulada = depreciacion_acumulada

    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    f = ""
    g = ""

    for a, b, c, d, e, f, g in data:
        print(a,b,c,d,e,f,g)

    activos_fijo = [activos_fijo(a, b, c, d, e, f, g)]
    table = activos_fijosTable(activos_fijo)

    return render_template("Activo_fijo.html", table = table)

@app.route('/Depreciacion.html')
def depreciacion():
    cursor.execute("select * from `calculo_depreciacion`;")
    data = cursor.fetchall()
    print(*data)
    class calculo_depreciacionTable(Table):
        id = Col('ID')
        ano_proceso = Col('Ano de proceso')
        mes_proceso= Col('Mes de proceso')
        activo_fijo = Col('Activo Fijo')
        fecha_proceso = Col('Fecha de proceso')
        monto_depreciado = Col('Monto Depreciado')
        depreciacion_acumulada = Col('Depreciación Acumulada')
        cuenta_compra = Col('Cuenta Compra')
        cuenta_depreciacion = Col('Cuenta Depreciación')

    class calculo_depreciacion(object):
        def __init__(self, id, ano_proceso, mes_proceso, activo_fijo, fecha_proceso, monto_depreciado, depreciacion_acumulada, cuenta_compra, cuenta_depreciacion):
            self.id = id
            self.ano_proceso = ano_proceso
            self.mes_proceso = mes_proceso
            self.activo_fijo = activo_fijo
            self.fecha_proceso = fecha_proceso
            self.monto_depreciado = monto_depreciado
            self.depreciacion_acumulada = depreciacion_acumulada
            self.cuenta_compra = cuenta_compra
            self.cuenta_depreciacion = cuenta_depreciacion


    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    f = ""
    g = ""
    h = ""
    i = ""

    for a, b, c, d, e, f, g, h, i in data:
        print(a,b,c,d,e,f,g,h, i)

    depreciacion = [calculo_depreciacion(a, b, c, d, e, f, g, h, i)]
    table = calculo_depreciacionTable(depreciacion)

    return render_template("Depreciacion.html", table = table)

@app.route('/btn_agregar_dp', methods=['POST'])
def btn_agregar_dp():
    ano_proceso = int(request.form['ano_proceso'])
    activos_fijos = request.form['activos_fijos']
    mes_proceso = request.form['mes_proceso']
    fecha_proceso = request.form['fecha_proceso']
    monto_depreciado = request.form['monto_dep']
    depreciacion_acumulada = request.form['depreciacion_acumulada']
    cuenta_compra = int(request.form['cuenta_compra'])
    cuenta_depreciacion = request.form['cuenta_dep']

    cursor.execute("Insert into inf_Activos_Fijos.calculo_depreciacion (cd_ano_proceso, cd_mes_proceso, id_activos_fijos, cd_fecha_proceso, cd_monto_depreciado, cd_depreciacion_acumulada, cd_cuenta_compra, cd_cuenta_depreciacion) values('"+str(ano_proceso)+"', '"+mes_proceso+"', '"+activos_fijos+"', '"+fecha_proceso+"', "+monto_depreciado+", "+depreciacion_acumulada+", '"+str(cuenta_compra)+"', '"+cuenta_depreciacion+"');")
    inf_Activos_Fijos.commit()
    return render_template("Depreciacion.html")

@app.route('/index.html')
def dash():
    cuenta_compra = int(request.form['cuenta_compra'])
    ano_proceso = int(request.form['ano_proceso'])
    depreciacion_acumulada = request.form['depreciacion_acumulada']
    valor_compra = cuenta_compra
    ano_dep = ano_proceso
    monto_dep = valor_compra / ano_dep
    dep_ac = monto_dep
    dep_rest = valor_compra - dep_ac
    return render_template("index.html", depreciacion_acumulada=depreciacion_acumulada, monto_dep=monto_dep, dep_rest=dep_rest)

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
    cursor.execute("select * from `empleados`;")
    data = cursor.fetchall()
    print(*data)
    class empleadosTable(Table):
        id = Col('ID')
        nombre = Col('Nombre')
        cedula = Col('Cedula')
        departamento = Col('Departamento')
        tipo_persona = Col('Tipo de Persona')
        fecha_ingreso = Col('Fecha de Ingreso')
        estado = Col('Estado')

    class empleado(object):
        def __init__(self, id, nombre, cedula, departamento, tipo_persona, fecha_ingreso, estado):
            self.id = id
            self.nombre = nombre
            self.cedula = cedula
            self.departamento = departamento
            self.tipo_persona = tipo_persona
            self.fecha_ingreso = fecha_ingreso
            self.estado = estado

    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    f = ""
    g = ""

    for a, b, c, d, e, f, g in data:
        print(a,b,c,d,e,f,g)

    empleados = [empleado(a, b, c, d, e, f, g)]
    table = empleadosTable(empleados)

    return render_template("Empleados.html", table = table)

@app.route('/Administracion.html')
def administracion():
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

    a = ""
    b = ""
    c = ""

    for a, b, c in data:
        print(a,b,c)

    departamentos = [departamento(a, b, c)]
    table = departamentosTable(departamentos)

    return render_template("Administracion.html", table = table)

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

    a = ""
    b = ""
    c = ""

    for a, b, c in data:
        print(a,b,c)

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

    a = ""
    b = ""
    c = ""

    for a, b, c in data:
        print(a,b,c)

    departamentos = [departamento(a, b, c)]
    table = departamentosTable(departamentos)

    return render_template("Recursos_humanos.html", table = table)

@app.route('/Asientos_contables.html')
def tables():
    return render_template("Asientos_contables.html")

@app.route('/btn_agregar_ac', methods=['POST'])
def btn_agregar_ac():
    descripcion = request.form['descripcion']
    tipo_inventario = request.form['tipo_inventario']
    cuenta_contable = request.form['cuenta_contable']
    tipo_movimiento = request.form['tipo_movimiento']
    fecha_asiento = request.form['fecha_asiento']
    monto_asiento = request.form['monto_asiento']
    estado = request.form['estado']
    cursor.execute("SELECT * FROM `asientos_contables`;")
    data = cursor.fetchall()

    class asientos_contablesTable(Table):
        id = Col('ID')
        descripcion = Col('Descripcion')
        tipo_inventario = Col('tipo_inventario')
        cuenta_contable = Col('cuenta_contable')
        tipo_movimiento = Col('tipo_movimiento')
        fecha_asiento = Col('fecha_asiento')
        monto_asiento = Col('monto_asiento')
        estado = Col('Estado')

    class asientos_contables(object):
        def __init__(self, id, descripcion, tipo_inventario, cuenta_contable, tipo_movimiento, fecha_asiento, monto_asiento, estado):
            self.id = id
            self.descripcion = descripcion
            self.tipo_inventario = tipo_inventario
            self.cuenta_contable = cuenta_contable
            self.tipo_movimiento = tipo_movimiento
            self.fecha_asiento = fecha_asiento
            self.monto_asiento = monto_asiento
            self.estado = estado

    a = ""
    b = ""
    c = ""
    d = ""
    e = ""
    f = ""
    g = ""
    h = ""

    for a, b, c, d, e, f, g, h in data:
        print(a,b,c,d,e, f, g, h)

    activos = [asientos_contables(a, b, c, d, e, f, g, h)]
    table = asientos_contablesTable(activos)

    cursor.execute("Insert into inf_Activos_Fijos.asientos_contables (ac_descripcion, ac_tipo_inventario, ac_cuenta_contable, ac_tipo_movimiento, ac_fecha_asiento, ac_monto_asiento, ac_estado) values('"+descripcion+"', '"+tipo_inventario+"', '"+cuenta_contable+"', '"+tipo_movimiento+"', "+fecha_asiento+", "+monto_asiento+", "+estado+");")
    inf_Activos_Fijos.commit()
    return render_template("Asientos_contables.html", table = table)


@app.route('/Tipos-de-activos.html')
def tipos_de_activos():
    cursor.execute("select * from `tipo_activos`;")
    data = cursor.fetchall()
    print(*data)
    class tipo_activosTable(Table):
        id = Col('ID')
        descripcion = Col('Descripcion')
        cuenta_compra = Col('Cuenta Compra')
        cuenta_depreciacion = Col('Cuenta Depreciacion')
        estado = Col('Estado')

    class tipo_activo(object):
        def __init__(self, id, descripcion, cuenta_compra, cuenta_depreciacion, estado):
            self.id = id
            self.descripcion = descripcion
            self.cuenta_compra = cuenta_compra
            self.cuenta_depreciacion = cuenta_depreciacion
            self.estado = estado

    a = ""
    b = ""
    c = ""
    d = ""
    e = ""

    for a, b, c, d, e in data:
        print(a,b,c,d,e)

    activos = [tipo_activo(a, b, c, d, e)]
    table = tipo_activosTable(activos)

    return render_template("tipos-de-activos.html", table = table)

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
