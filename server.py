

# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Autorise les requêtes depuis index.html

OPENROUTER_API_KEY = "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"  # 🔑 remplace ici avec ta vraie clé

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + OPENROUTER_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": user_message}]
        }
    )

    return jsonify(response.json())

@app.route("/")
def home():
    return "✅ Serveur Flask opérationnel !"

if __name__ == "__main__":
    print("🚀 Lancement du serveur...")
    app.run(debug=True)

