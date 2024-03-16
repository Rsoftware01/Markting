import logging
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

# Configurações do Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "84a79d3c4b03d8747677517aa12c1ef54b044b62"

# Inicialização das extensões
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

# Configuração do logger para imprimir no console
logging.basicConfig()
logger = logging.getLogger("server")
logger.setLevel(logging.INFO)

# Configuração do handler do logger para imprimir no console
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)

# Import dos blueprints ou módulos
from fakepinterest import routes
