from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://banco_evento_empresa_user:X7rECD5KwCQeMWsoyvl0awoE2SlSorvd@dpg-cnjjegev3ddc738d6r70-a.oregon-postgres.render.com/banco_evento_empresa"
app.config["SECRET_KEY"] = "84a79d3c4b03d8747677517aa12c1ef54b044b62"

database = SQLAlchemy(app)
bcrypt =Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"
print(app.config)
from fakepinterest  import routes