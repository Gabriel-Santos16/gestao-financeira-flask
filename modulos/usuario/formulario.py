from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DecimalField,SelectField
from wtforms.validators import DataRequired
from flask_login import current_user


class TransacaoForm(FlaskForm):
    tipo = SelectField("tipo", choices=[('receita', 'receita'),('despesa','despesa')], validators=[DataRequired()])
    descricao = StringField('descricao', validators=[DataRequired()])
    valor = DecimalField('valor', validators=[DataRequired()])
    categoria = SelectField("categoria", choices=[], validate_choice=False, validators=[DataRequired()])
    data = DateField('data', validators=[DataRequired()])
    enviar = SubmitField('enviar')
        
        
class CategoriaForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()], render_kw={"class":"form-control" })
    tipo = SelectField("tipo", choices=[('receita', 'receita'),('despesa','despesa')], validators=[DataRequired()], render_kw={"class":"form-select"})
    salvar = SubmitField('adicionar', render_kw={"class":"btn btn-primary"})
