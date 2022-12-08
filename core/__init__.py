from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'OneS2023'

from core import routes