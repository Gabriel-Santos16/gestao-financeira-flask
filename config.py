from extensions import carregar_chave,conectar_db

class Config:
    SQLALCHEMY_DATABASE_URI = conectar_db()
    SECRET_KEY = carregar_chave()