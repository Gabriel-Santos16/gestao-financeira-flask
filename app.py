from flask import Flask
from modulos.auth.auth import auth
from modulos.main.main import main
from modulos.usuario.user import user
from config import Config
from models.models import db
from extensions import lm




app = Flask("__name__")
app.config.from_object(Config)

lm.init_app(app)
db.init_app(app)     



app.register_blueprint(user)
app.register_blueprint(main)
app.register_blueprint(auth)



if __name__=="__main__":
    with  app.app_context():
        db.create_all()
    app.run(debug=True)

    