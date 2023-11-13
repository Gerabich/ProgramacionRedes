# Creando un servidor Web con Flask para proporcionar servicios
# mediante los métodos GET, PUT, DELETE, POST
# Profesor: Gabriel Barrón R.
# AlumnoÑ Gerardo Antonio Garcia Vazquez

import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM profesores')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))


@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO profesores(nombre, correo, materia, telefono) VALUES(?,?)'
    cursor.execute(insert, [record['id'], record['nombre'], record['correo'], record['materia'], record['telefono']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM profesores WHERE correo= ?'
    cursor.execute(delete, [record['id'], record['nombre'], record['correo'], record['materia'], record['telefono']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'UPDATE profesores SET correo = ? WHERE id= ?'
    cursor.execute(delete, [record['id'], record['nombre'], record['correo'], record['materia'], record['telefono']])
    conn.commit()
    return jsonify(record)
app.run(debug=True)