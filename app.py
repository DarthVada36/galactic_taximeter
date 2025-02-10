from flask import Flask, render_template, request, jsonify

from taximetro import Taximetro


app = Flask(__name__)


taximetro = Taximetro()


@app.route('/get_prices', methods=['GET'])
def get_prices():
    return jsonify(taximetro.precios)

# Ruta de inicio
@app.route('/')
def index():
    return render_template("index.html")


# Ruta para iniciar el taxímetro
@app.route("/start", methods=["POST"])
def start_trip():
    respuesta = taximetro.iniciar_viaje()
    return jsonify(respuesta)


# Ruta para cambiar el estado del taxímetro
@app.route("/change_state", methods=["POST"])
def change_state():
    data = request.get_json()
    nuevo_estado = data.get("estado", "").upper()

    if nuevo_estado not in ["MOVIMIENTO", "PARADO"]:
        return jsonify({"error": "Estado inválido"}), 400

    respuesta = taximetro.cambiar_estado(nuevo_estado)

    # Asegurar que se devuelven siempre los valores correctos
    return jsonify({
        "estado": nuevo_estado,  # El estado correcto
        "tarifa_acumulada": round(respuesta.get("tarifa_acumulada", 0.00), 2)
    })

# Finalizar viaje
@app.route("/stop", methods=["POST"])
def stop_trip():
    respuesta = taximetro.finalizar_viaje()
    
    return jsonify({
        "estado": respuesta.get("estado", "PARADO"),  
        "tarifa_total": round(respuesta.get("tarifa_total", 0.00), 2)  
    })

if __name__ == '__main__':
    print("Iniciando Flask en: http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)
