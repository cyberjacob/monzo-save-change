import os

from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////tmp/flask_app.db')

CLIENT_ID_KEY = "clientId"
CLIENT_SECRET_KEY = "clientSecret"
CLIENT_TOKEN_KEY = "clientToken"

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

class Config(db.Model):
    key = db.Column(db.String(32), primary_key=True)
    value = db.Column(db.String(128))

    @staticmethod
    def insert_or_update(key, value):
        obj = Config.query.get(key)
        if obj:
            obj.value = value
            db.session.commit()
        else:
            db.session.add(Config(key=key, value=value))
            db.session.commit()

try:
    for x in db.session.query(Config):
        pass
except exc.ProgrammingError:
    db.create_all()


@app.route('/', methods=['GET'])
def index():
    return send_from_directory("static", "config.html")

@app.route('/', methods=['POST'])
def submit_config():
    Config.insert_or_update(CLIENT_ID_KEY, value=request.form['Client ID'])
    Config.insert_or_update(CLIENT_SECRET_KEY, value=request.form['Client Secret'])
    return redirect("https://auth.getmondo.co.uk/?response_type=code&redirect_uri="+request.form['Redirect URL']+"/auth&client_id="+request.form['Client ID'])

@app.route('/webhook')
def webhook():
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
