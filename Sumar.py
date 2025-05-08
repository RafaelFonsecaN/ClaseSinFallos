from flask import Flask, request, jsonify
import math
app = Flask(__name__)

@app.route('/sumar', methods=['GET'])
def calcular_raiz():
  try:
    numero1 = float(request.args.get('numero1'))
    numero2 = float(request.args.get('numero2'))
    
    resultado = numero1 + numero2
    return jsonify({'La suma es igual a': resultado})
  except (TypeError, ValueError):
    return jsonify({'error':'Parametro invalido, se requiere un numero'}),400

if __name__ == '__main__':
  app.run(debug=True)
