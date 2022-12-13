from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def fetch_api():
    url = "https://pvp.qq.com/web201605/js/herolist.json"
    response = requests.get(url)
    data = response.json()
    with open('herolist.json', 'w') as f:
        json.dump(data, f)
    return jsonify(data)

if __name__ == '__main__':
    app.run()
