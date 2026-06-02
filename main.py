from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Configuración: permite localhost para desarrollo y tu dominio de Vercel
CORS(app, resources={r"/*": {"origins": ["*"]}})

@app.route("/health", methods=["GET"])
def health_check():
    return {
        "status": "online",
        "message": "Backend operativo"
    }, 200