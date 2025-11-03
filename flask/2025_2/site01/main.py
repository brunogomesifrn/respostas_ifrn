from flask import Flask

app = Flask(__name__, static_url_path="")

from routes import *
from routes_alunos import *

app.run()