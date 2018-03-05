import os

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    import json
    return json.dumps(os.environ)

@app.route('/webhook')
def webhook():
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
