from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return 'index'

@app.route('/usuarios/<dni>')
def info(dni):
    informacion = {"Nombre": "Juan", "Dni": dni, "Tlf": "123"}  
    return jsonify(informacion), 200

if __name__ == '__main__':
    app.run(debug=True)