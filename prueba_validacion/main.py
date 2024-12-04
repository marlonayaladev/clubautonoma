"""
GET -> Obtener info
POST -> Crear informacion 
PUT -> Actualizar Información
DELETE -> Borrar informacion
"""

from flask import Flask, jsonify, request

#Modulo Flask sirve para crear aplicaciones web
#jsonify: se utiliza para convertir objetos de python (como diccionarios) en una respuesta json
#request: Permite acceder 

app=Flask(__name__)

@app.route('/')
def root():
    return "FLASK INICIo"



@app.route('/usuarios/<dni>')
def info(dni):
    informacion = {"Nombre": "Marlon", "Dni": dni, "Telefono": "123"}

    return jsonify(informacion)

if __name__ =='__main__':
    app.run(debug=True)

