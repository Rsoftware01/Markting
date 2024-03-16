import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

# Configurações do Flask
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "84a79d3c4b03d8747677517aa12c1ef54b044b62"

# Inicialização das extensões
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"
login_manager.login_view = "info2"
login_manager.login_view = "info3"
login_manager.login_view = "resultados"

# Configuração do logger para o SQLAlchemy
#logging.basicConfig()
#logger = logging.getLogger("sqlalchemy.engine")
#logger.setLevel(logging.INFO)

# Configuração do handler do logger para imprimir no console
#handler = logging.StreamHandler()
#handler.setLevel(logging.INFO)
#logger.addHandler(handler)

# Filtrando apenas mensagens INFO com resultados
#logger.addFilter(lambda record: record.levelno == logging.INFO and "cached since" in record.msg)

# Import dos blueprints ou módulos
from fakepinterest import routes

