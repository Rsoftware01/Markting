from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mulheresevento_user:oc6NoMNYCTfvujz8pN5Ght3Bth5YsXFZ@dpg-cnk732n109ks73b6r22g-a.oregon-postgres.render.com/mulheresevento"
app.config["SECRET_KEY"] = "84a79d3c4b03d8747677517aa12c1ef54b044b62"

database = SQLAlchemy(app)
bcrypt =Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"
login_manager.login_view = "info3"
login_manager.login_view = "info3"
login_manager.login_view = "resultados"

from fakepinterest  import routes

