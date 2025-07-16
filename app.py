from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print(f"Gelen sinyal: {data}")
    return "Sinyal alındı!", 200

@app.route('/', methods=['GET'])
def root():
    return "Askom Sinyal Botu Aktif 🟢"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
