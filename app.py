# Importar psycopg2 para establecer una coneccion con la base de datos escuela_magica alojada en postgresql
import psycopg2

# Establecer conexion con la base de datos
conn = psycopg2.connect(
    host="localhost", 
    database="escuela_magica",
    user="postgres",
    password="12345"
)
#importar framework flask y sus caracteristicas
from flask import Flask, request, jsonify
#importar random para hacer la asignacion aleatoria de grimorios
import random
#importar pandas y openpyxl para leer y extraer datos del archivo excel: Tipos de Magia.xlsx
import pandas as pd
import openpyxl

app = Flask(__name__)

# Consultar todas las solicitudes.
@app.route('/solicitudes', methods=['GET'])
def obtener_solicitudes():
    cur = conn.cursor()
    cur.execute("SELECT * FROM solicitudes")
    solicitudes = cur.fetchall()
    cur.close()
    return jsonify(solicitudes)

# Consultar asignaciones de Grimorios.
@app.route('/grimorios', methods=['GET'])
def obtener_grimorios():
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, grimorio, portada FROM solicitudes")
    grimorios = cur.fetchall()
    cur.close()
    return jsonify(grimorios)


# Enviar solicitud de ingreso.
@app.route('/solicitudes', methods=['POST'])
def insertar_usuario():
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    identificacion = request.json['identificacion']
    edad = str(request.json['edad'])
    afinidad_magica = request.json['afinidad_magica']
    grimorio = None
    portada = None
    # Leer el archivo Excel
    df = pd.read_excel('./documentos/Tipos de Magia.xlsx', sheet_name='Sheet1')

    # Convierte la columna 'afinidad_magica' en una lista de Python
    afinidades = df['afinidad_magica'].tolist()


     # Validar los requerimientos en los campos solicitados
    if (not nombre.isalpha() or len(nombre) > 20 or 
        not apellido.isalpha() or len(apellido) > 20 or 
        not identificacion.isalnum() or len(identificacion) > 10 or 
        not edad.isdigit() or len(edad) != 2 or 
        # Validar que la afinidad mágica sea una de las permitidas
        afinidad_magica not in afinidades):
        #afinidad_magica not in ['Magia de Oscuridad', 'Magia de Luz', 'Magia de Fuego', 'Magia de Agua', 'Magia de Viento', 'Magia de Tierra']):
        return jsonify({"mensaje": "La solicitud ha sido rechazada"}), 400

    # Asignar grimorios aleatoriamente
    grimorios_nombre = {1: 'Sinceridad', 2: 'Esperanza', 3: 'Amor', 4: 'Buena Fortuna', 5: 'Desesperación'}
    tréboles = {1: 'Trébol de 1 hoja', 2: 'Trébol de 2 hojas', 3: 'Trébol de 3 hojas', 4: 'Trébol de 4 hojas', 5: 'Trébol de 5 hojas'}

    grimorio = grimorios_nombre[random.randint(1, 5)]
    portada = tréboles[list(grimorios_nombre.keys())[list(grimorios_nombre.values()).index(grimorio)]]

    cur = conn.cursor()
    cur.execute("INSERT INTO solicitudes (nombre, apellido, identificacion, edad, afinidad_magica, grimorio, portada) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nombre, apellido, identificacion, edad, afinidad_magica, grimorio, portada))
    

    conn.commit()
    cur.close()
    return jsonify({"mensaje": "Solicitud insertada correctamente"})

# Actualizar solicitud de ingreso.
@app.route('/solicitudes/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    identificacion = request.json['identificacion']
    edad = request.json['edad']
    afinidad_magica = request.json['afinidad_magica']
    grimorio = request.json['grimorio']
    portada = request.json['portada']

    cur = conn.cursor()
    cur.execute(f"UPDATE solicitudes SET nombre = '{nombre}', apellido = '{apellido}', identificacion = '{identificacion}', edad = '{edad}', afinidad_magica = '{afinidad_magica}', grimorio = '{grimorio}', portada = '{portada}' WHERE id = {id}")
    conn.commit()
    cur.close()
    return jsonify({"mensaje": "Solicitud actualizada correctamente"})

# Actualizar estatus de solicitud.
@app.route('/estatus/<int:id>', methods=['PUT'])
def actualizar_estatus(id):
    estatus = request.json['estatus']

    cur = conn.cursor()
    cur.execute(f"UPDATE solicitudes SET estatus = '{estatus}' WHERE id = {id}")
    conn.commit()
    cur.close()
    return jsonify({"mensaje": "Estatus de solicitud actualizada correctamente"})

# Eliminar solicitud de ingreso.
@app.route('/solicitudes/<int:id>', methods=['DELETE'])
def eliminar_solicitudes(id):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM solicitudes WHERE id = {id}")
    conn.commit()
    cur.close()
    return jsonify({"mensaje": "Solicitud eliminada correctamente"})

if __name__ == '__main__':
    app.run(debug=True)
