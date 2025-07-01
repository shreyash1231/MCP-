from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.expanduser("~/mcp_workspace")
os.makedirs(BASE_DIR, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_files():
    folder = request.form.get("folder")
    if not folder:
        return jsonify({"error": "Folder name is missing"}), 400

    folder_path = os.path.join(BASE_DIR, folder)
    os.makedirs(folder_path, exist_ok=True)

    for f in request.files.getlist("files"):
        rel_path = f.filename
        file_path = os.path.join(folder_path, rel_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        f.save(file_path)

    return jsonify({"status": "Folder uploaded", "path": folder})

@app.route("/list", methods=["POST"])
def list_files():
    data = request.json
    folder = data.get("folder")
    if not folder:
        return jsonify({"error": "Folder name is required"}), 400

    folder_path = os.path.join(BASE_DIR, folder)
    if not os.path.exists(folder_path):
        return jsonify({"error": "Folder not found"}), 404

    all_files = []
    for root, _, files in os.walk(folder_path):
        for name in files:
            rel_path = os.path.relpath(os.path.join(root, name), folder_path)
            all_files.append(rel_path)
    return jsonify({"files": all_files})

@app.route("/read", methods=["POST"])
def read_file():
    data = request.json
    folder = data.get("folder")
    filename = data.get("filename")

    if not folder or not filename:
        return jsonify({"error": "Folder and filename are required"}), 400

    path = os.path.join(BASE_DIR, folder, filename)
    if not os.path.exists(path):
        return jsonify({"error": "File not found"}), 404

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return jsonify({"error": f"Error reading file: {str(e)}"}), 500

    return jsonify({"content": content})

@app.route("/create", methods=["POST"])
def create_file():
    data = request.json
    folder = data.get("folder")
    filename = data.get("filename")
    content = data.get("content", "")

    if not folder or not filename:
        return jsonify({"error": "Folder and filename are required"}), 400

    path = os.path.join(BASE_DIR, folder, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        return jsonify({"error": f"Error creating file: {str(e)}"}), 500

    return jsonify({"status": "File created"})

@app.route("/edit", methods=["POST"])
def edit_file():
    data = request.json
    folder = data.get("folder")
    filename = data.get("filename")
    content = data.get("content")

    if not folder or not filename or content is None:
        return jsonify({"error": "Folder, filename, and content are required"}), 400

    path = os.path.join(BASE_DIR, folder, filename)
    if not os.path.exists(path):
        return jsonify({"error": "File not found"}), 404

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        return jsonify({"error": f"Error editing file: {str(e)}"}), 500

    return jsonify({"status": "File edited"})

@app.route("/delete", methods=["POST"])
def delete_file():
    data = request.json
    folder = data.get("folder")
    filename = data.get("filename")

    if not folder or not filename:
        return jsonify({"error": "Folder and filename are required"}), 400

    path = os.path.join(BASE_DIR, folder, filename)
    print("Deleting file at:", path)
    if os.path.exists(path):
        try:
            os.remove(path)
            return jsonify({"status": "File deleted"})
        except Exception as e:
            return jsonify({"error": f"Error deleting file: {str(e)}"}), 500

    return jsonify({"error": "File not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
