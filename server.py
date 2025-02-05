from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)
clients = {}

@app.route('/attach', methods=['POST'])
def attach():
    client_id = request.json.get('client_id')
    if client_id in clients:
        return jsonify({"message": "Client already attached"}), 400
    clients[client_id] = {"status": "attached", "ip": request.remote_addr, "port": request.environ.get('REMOTE_PORT')}  
    print(f"Client attached: {clients[client_id]}")

    return jsonify({"message": "Client attached successfully"}), 200

@app.route('/send_traffic', methods=['POST'])
def send_traffic():
    client_id = request.json.get('client_id')
    if client_id not in clients:
        return jsonify({"message": "Client not attached"}), 400

    def traffic_logic():
        while clients[client_id]["status"] == "attached":
            print(f"Sending traffic to client {client_id}")
            time.sleep(0.05)  # Simulate traffic sending delay of 50ms

    traffic_thread = threading.Thread(target=traffic_logic)
    traffic_thread.start()
    return jsonify({"message": "Traffic started"}), 200

@app.route('/detach', methods=['POST'])
def detach():
    client_id = request.json.get('client_id')
    if client_id not in clients:
        return jsonify({"message": "Client not attached"}), 400
    clients[client_id]["status"] = "detached"
    return jsonify({"message": "Client detached successfully"}), 200

@app.route('/get_client_info', methods=['GET', 'POST'])
def get_client_info():
    client_ip = request.remote_addr
    client_port = request.environ.get('REMOTE_PORT')

    return {
        "client_ip": client_ip,
        "client_port": client_port
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)