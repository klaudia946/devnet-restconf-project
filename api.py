
from flask import Flask, request, jsonify

app = Flask(__name__)

# symulowane dane
interfaces = []
routing = []

# prosty token
AUTH_TOKEN = "12345"

def check_auth():
    token = request.headers.get("Authorization")
    if token != AUTH_TOKEN:
        return False
    return True

# INTERFACES

@app.route('/interfaces', methods=['GET'])
def get_interfaces():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(interfaces)

@app.route('/interfaces', methods=['POST'])
def create_interface():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    interfaces.append(data)
    return jsonify({"message": "Interface created"}), 201

@app.route('/interfaces/<int:id>', methods=['PUT'])
def update_interface(id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    if id >= len(interfaces):
        return jsonify({"error": "Not found"}), 404

    interfaces[id] = request.json
    return jsonify({"message": "Updated"})

@app.route('/interfaces/<int:id>', methods=['DELETE'])
def delete_interface(id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    if id >= len(interfaces):
        return jsonify({"error": "Not found"}), 404

    interfaces.pop(id)
    return jsonify({"message": "Deleted"})

# ROUTING

@app.route('/routing', methods=['GET'])
def get_routes():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(routing)

@app.route('/routing', methods=['POST'])
def add_route():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    if not data or "network" not in data:
        return jsonify({"error": "Invalid data"}), 400

    routing.append(data)
    return jsonify({"message": "Route added"}), 201


if __name__ == '__main__':
    app.run(port=5000)
