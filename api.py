from flask import Flask, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/colors')
def get_colors():
    file_path = os.path.join(os.path.dirname(__file__), "color_history.csv")
    if not os.path.exists(file_path):
        return "Fichier color_history.csv introuvable", 404
    return send_file(file_path, mimetype="text/csv")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
