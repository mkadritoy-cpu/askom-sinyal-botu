from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Bot tokenin
TOKEN = "7147929892:AAHkXxxvAfmrtl8z7YHEEDtE9Yk8xYVesQk"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print("🔵 Gelen veri:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        print("🟡 Chat ID:", chat_id)
        print("🟡 Text:", text)

          Yanıt mesajı
        reply = "Bot çalışıyor aşkom ❤️"
        payload = {
            "chat_id": chat_id,
            "text": reply
        }

        response = requests.post(TELEGRAM_URL, json=payload)
        print("🟢 Telegram yanıtı:", response.status_code, response.text)

    return jsonify({"ok": True})
