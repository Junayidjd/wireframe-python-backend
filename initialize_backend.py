import os

# Folder structure
folders = [
    "wsi-viewer-backend/app",
    "wsi-viewer-backend/static/images",
]

# Files and their content
files = {
    "wsi-viewer-backend/app/__init__.py": "",
    "wsi-viewer-backend/app/routes.py": """
from flask import Blueprint

bp = Blueprint('routes', __name__)

@bp.route('/get_bounding_boxes')
def get_bounding_boxes():
    # This function will be implemented later
    pass
""",
    "wsi-viewer-backend/static/images/whole_slide_image.dzi": "",
    "wsi-viewer-backend/output.json": """
{
    "detection_results": [
        {"x": 0.1, "y": 0.2, "width": 0.3, "height": 0.4},
        {"x": 0.5, "y": 0.6, "width": 0.2, "height": 0.3}
    ]
}
""",
    "wsi-viewer-backend/requirements.txt": "Flask",
    "wsi-viewer-backend/app.py": """
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/get_bounding_boxes')
def get_bounding_boxes():
    with open('output.json', 'r') as f:
        data = json.load(f)
    return jsonify(data['detection_results'])

if __name__ == '__main__':
    app.run(debug=True)
""",
    "wsi-viewer-backend/README.md": """
# WSI Viewer Backend

This is the backend for the Whole Slide Image (WSI) Viewer project.
"""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content.strip())

print("Backend folder and files initialized successfully!")