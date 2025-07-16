from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Bot tokenin
TOKEN = "7147929892:AAHkXxvAfmrtW3z7YHEEDtE9Yk8xYVgsQpk"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    # Mesaj var mı kontrolü
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        # Yanıt oluştur
        if "aşkom" in text.lower():
            reply = "Buradayım, emrindeyim 🫡💘"
        else:
            reply = "Bana 'aşkom' diye seslen 🥹"

        # Cevap gönder
        payload = {
            "chat_id": chat_id,
            "text": reply
        }
        requests.post(TELEGRAM_URL, json=payload)

    return jsonify({"ok": True})
