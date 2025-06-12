import base64
import json
import os
from google.cloud import pubsub_v1
from flask import Flask, request

app = Flask(__name__)
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(os.environ['PROJECT_ID'], os.environ['TOPIC_NAME'])

@app.route('/', methods=['POST'])
def index():
    envelope = request.get_json()
    if not envelope:
        return 'No JSON received', 400

    gcs_data = envelope.get('message', {}).get('data')
    if not gcs_data:
        return 'No data in message', 400

    decoded_data = json.loads(base64.b64decode(gcs_data).decode('utf-8'))
    file_name = decoded_data['name']
    file_size = decoded_data.get('size', '0')
    file_format = file_name.split('.')[-1] if '.' in file_name else 'unknown'

    metadata = {
        'file_name': file_name,
        'size': file_size,
        'format': file_format
    }

    publisher.publish(topic_path, json.dumps(metadata).encode('utf-8'))
    print(f"Published: {metadata}")
    return 'OK', 200
