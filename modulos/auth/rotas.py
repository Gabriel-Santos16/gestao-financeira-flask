from flask import render_template,redirect,url_for,flash
from flask_login import logout_user, login_user
from sqlalchemy.exc import IntegrityError
from models.models import Usuario,Categoria,db
from flask_login import login_required
from .formulario import UsuarioForm
from extensions import crip
from .auth import auth



@auth.route('/login',methods=["GET","POST"])
def login():
    formulario = UsuarioForm()
    if formulario.validate_on_submit():
        user = Usuario.query.filter_by(login=formulario.login.data,senha=crip(formulario.senha.data)).first()
        if not user:
            flash("Usuario ou senha incorreto")
            redirect(url_for('authbp.login'))
        else:
            login_user(user)
            return redirect(url_for('usuariobp.home'))
    return render_template('form_logar_cadastrar.html', form=formulario, conta=True)    
      
      
@auth.route('/cadastrar',methods=["GET","POST"])           
def cadastrar():
    formulario = UsuarioForm()
    if formulario.validate_on_submit():
        try:
            user = Usuario(senha=crip(formulario.senha.data), login=formulario.login.data)
            db.session.add(user)
            db.session.commit()
            user.AdicionarCategoriasPadrao()                
            
            login_user(user)
            
            return redirect(url_for('usuariobp.home'))              
        except IntegrityError:
            flash("Ja existe um usuario com este login, por favor escolha outro")
            return redirect(url_for("authbp.cadastrar"))
  
    return render_template('form_logar_cadastrar.html', form=formulario, conta=False)  
      
      
@auth.route('/logout',methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('mainbp.home'))
