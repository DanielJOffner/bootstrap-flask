from flask import Flask
from wdb.ext import WdbMiddleware

app = Flask(__name__)
app.debug = True
app.wsgi_app = WdbMiddleware(app.wsgi_app)

from app import routes