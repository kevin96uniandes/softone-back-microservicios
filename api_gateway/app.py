from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Configura las URLs de tus microservicios

SERVICES = {
    'clave_maestra': 'http://localhost:3003/api/clave_maestra',
    'elementos': 'http://localhost:3002/api/elementos'
}

@app.route('/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(service, path):
    if service not in SERVICES:
        return jsonify({'error': 'Service not found'}), 404
    
    url = f"{SERVICES[service]}/{path}"
    print(f"Proxying {request.method} request to {url}")
    
    try:
        if request.method == 'GET':
            response = requests.get(url, params=request.args)
        elif request.method == 'POST':
            response = requests.post(url, json=request.json)
        elif request.method == 'PUT':
            response = requests.put(url, json=request.json)
        elif request.method == 'DELETE':
            response = requests.delete(url, json=request.json)
        
        return (response.content, response.status_code, response.headers.items())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run(port=3000, debug=True)