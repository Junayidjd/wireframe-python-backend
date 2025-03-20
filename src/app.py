from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Root route
@app.route('/')
def home():
    return "Welcome to the Flask Backend!"

@app.route('/get_bounding_boxes')
def get_bounding_boxes():
    try:
        # Update the path to output.json
        with open('output.json', 'r') as f:
            data = json.load(f)
        
        # Debugging: Print the type and content of inference_results
        print("Type of inference_results:", type(data['inference_results']))
        print("Content of inference_results:", data['inference_results'])

        # Agar inference_results string hai, toh use JSON mein convert karein
        if isinstance(data['inference_results'], str):
            inference_results = json.loads(data['inference_results'])
        else:
            inference_results = data['inference_results']
        
        detection_results = inference_results['output']['detection_results']
        return jsonify(detection_results)
    except json.JSONDecodeError as e:
        print("JSON Decode Error:", e)
        return jsonify({"error": "Invalid JSON format in inference_results"}), 500
    except KeyError as e:
        print("Key Error:", e)
        return jsonify({"error": "Missing key in JSON data"}), 500
    except Exception as e:
        print("Unexpected Error:", e)
        return jsonify({"error": "An unexpected error occurred"}), 500

# Ensure the static/images folder exists
static_folder = os.path.join(os.path.dirname(__file__), 'static', 'images')
if not os.path.exists(static_folder):
    os.makedirs(static_folder)

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(static_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)