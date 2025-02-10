from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from taximetro import Taximetro
import time


app = Flask(__name__)
socketio = SocketIO(app)  # Habilita WebSocket
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
        "estado": taximetro.estado_actual,  # El estado correcto
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

def actualizar_tarifa():
    while True:
        tarifa_actualizada = taximetro.obtener_tarifa_acumulada()  # Obtener tarifa actual
        socketio.emit("update_tarifa", {"tarifa": tarifa_actualizada})  
        time.sleep(0.5)  # Actualiza cada 0.5 segundos

if __name__ == '__main__':
    import threading
    threading.Thread(target=actualizar_tarifa, daemon=True).start()
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
