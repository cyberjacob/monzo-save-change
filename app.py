import os

from flask import Flask, request, redirect, url_for, render_template
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
    key = db.Column(db.String(10), primary_key=True)
    value = db.Column(db.String(128))

try:
    for x in db.session.query(Config):
        pass
except exc.ProgrammingError:
    db.create_all()


@app.route('/', methods=['GET'])
def index():
    x = ""
    for instance in db.session.query(Config):
        x += instance.key+" - "+instance.value+"<br/>"
    return x

@app.route('/webhook')
def webhook():
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
