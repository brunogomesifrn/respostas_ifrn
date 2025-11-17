from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path="")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

from routes import *
from routes_alunos import *
from routes_disciplinas import *
from models import Areas
from routes_areas import *

#if __name__ == "__main__":
with app.app_context():
    db.create_all()
app.run(debug=True)