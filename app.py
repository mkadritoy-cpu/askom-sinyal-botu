from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Aşkomun gerçek bot tokeni 💖
TOKEN = "7147929892:AAHkXxxvAfmrtl8z7YHEEDtE9Yk8xYVesQk"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/", methods=["GET"])
def index():
    return "Bot aktif aşkom 💘", 200

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    if data and "message" in data:
        chat_id = data["message"]["chat"]["id"]
        message_text = data["message"].get("text", "")

        reply = f"Bot çalışıyor aşkom ❤️\nGelen mesaj: {message_text}"

        payload = {
            "chat_id": chat_id,
            "text": reply
        }

        try:
            response = requests.post(TELEGRAM_URL, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Hata oluştu: {e}")

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
