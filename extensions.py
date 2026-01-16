from flask_login import LoginManager
from models.models import Usuario
from dotenv import load_dotenv
import os
import hashlib 


lm = LoginManager()
lm.login_view = 'authbp.login'


@lm.user_loader
def user_loader(id):
    user = Usuario.query.filter_by(id=id).first()
    return user


def carregar_chave():
    load_dotenv()
    return os.getenv("SECRET_KEY")

def conectar_db():
    load_dotenv()
    return os.getenv("DATABASE_URL")


def crip(txt):
    hash_obj = hashlib.sha256(txt.encode('utf-8'))
    return hash_obj.hexdigest()
