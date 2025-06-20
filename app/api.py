from flask import Flask, request, jsonify
from app.reservas import verificar_disponibilidad

app = Flask(__name__)
reservas = []

@app.route('/reservas', methods=['POST'])
def reservar():
    data = request.get_json()
    disponible = verificar_disponibilidad(reservas, data)

    if disponible:
        reservas.append(data)
        return jsonify({"message": "Reserva exitosa"}), 201
    else:
        return jsonify({"message": "Sala no disponible"}), 409