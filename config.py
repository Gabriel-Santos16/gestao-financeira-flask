from extensions import carregar_chave,conectar_db

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = carregar_chave()