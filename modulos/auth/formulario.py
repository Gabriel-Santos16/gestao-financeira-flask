from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length



class UsuarioForm(FlaskForm):
    login = StringField('login', validators=[DataRequired()], render_kw={'placeholder':"digite seu login aqui"})
    senha = PasswordField('senha',validators=[DataRequired(),Length(min=8)],render_kw={'placeholder':"digite sua senha aqui"})
    enviar = SubmitField('enviar')
    

