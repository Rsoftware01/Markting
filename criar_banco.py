from fakepinterest import database, app
from fakepinterest.models import Usuario, Info, OutraInfo

with app.app_context():
    database.create_all()