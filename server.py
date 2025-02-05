from flask import Flask, request, Response
import time

app = Flask(__name__)

def generate_packets(data):
    """Simulate generating packets."""
    for i in range(5):
        yield f"Packet {i+1}: {data}\n"
        time.sleep(1)  # Simulate a delay between packets

@app.route('/post-endpoint', methods=['POST'])
def post_endpoint():
    data = request.form['data']  # Get data from POST request
    return Response(generate_packets(data), content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
