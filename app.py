from flask import Flask, request, jsonify
import json
from elasticsearch_helper import insert_to_elasticsearch, get_all_services_status, get_service_status

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_status():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    content = json.load(file)
    insert_to_elasticsearch(content)
    return jsonify({"status": "Inserted to Elasticsearch"}), 201

@app.route('/healthcheck', methods=['GET'])
def check_all():
    return jsonify(get_all_services_status())

@app.route('/healthcheck/<service>', methods=['GET'])
def check_service(service):
    status = get_service_status(service)
    if not status:
        return jsonify({"error": f"Service {service} not found"}), 404
    return jsonify({service: status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)