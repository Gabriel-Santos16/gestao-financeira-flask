from flask import render_template,request,redirect,url_for,flash
from flask_login import current_user,login_required
from datetime import datetime
from models.models import Transacao,Categoria,db
from .formulario import TransacaoForm,CategoriaForm
from .user import user
import inspect




@user.route("/")
@login_required
def home():
    usuario = current_user
    return render_template('user_home.html', usuario=usuario)


@user.route("/transacoes")
@login_required
def transacoes():
    usuario = current_user
    return render_template('transacoes.html', usuario=usuario)


@user.route("/nova-transacao",methods=['GET','POST'])
@login_required
def add_transacao():
    categorias_renda = [cat.nome for cat in current_user.categorias if cat.tipo=='receita']
    categorias_despesa = [cat.nome for cat in current_user.categorias if cat.tipo=='despesa']

    form = TransacaoForm()
    
    if form.validate_on_submit():
        nova_transacao = Transacao(id_usuario=current_user.id ,
                            tipo=form.tipo.data,
                            descricao=form.descricao.data,
                            valor=form.valor.data,
                            data=form.data.data,
                            categoria=form.categoria.data)
        db.session.add(nova_transacao)
        db.session.commit()
        
        return redirect(url_for('usuariobp.add_transacao'))

    return render_template('form_transacao.html', form=form, rendas=categorias_renda,gastos=categorias_despesa)


@user.route('/editar-transacao/<int:id>',methods=["GET","POST"])
@login_required
def editar_transacao(id):
    categorias_renda = [cat.nome for cat in current_user.categorias if cat.tipo=='receita']
    categorias_despesa = [cat.nome for cat in current_user.categorias if cat.tipo=='despesa']
    
    transacao_selecionada = Transacao.query.filter_by(id=id).first()
    form = TransacaoForm(obj=transacao_selecionada)
    
    if form.validate_on_submit():
        form.populate_obj(transacao_selecionada)           
        db.session.commit()
        return redirect(url_for('usuariobp.home'))
    return render_template('form_transacao.html', transacao_selecionada=transacao_selecionada, rendas=categorias_renda, gastos=categorias_despesa, form=form, edit=True)


@user.route('/excluir/<objeto>/<int:id>', methods=["DELETE"])
@login_required
def excluir(objeto,id):
    if objeto=="transacao":
        registro = Transacao.query.filter_by(id=id).first()
    elif objeto=="categoria":
        registro = Categoria.query.filter_by(id=id).first()
        
    db.session.delete(registro)
    db.session.commit()
    return {"delete":"ok"}
    
    
@user.route('/categorias')
@login_required
def categorias():
    return render_template('categorias.html',categorias=current_user.categorias)


@user.route('/nova-categoria',methods=["GET","POST"])
@login_required
def add_categoria():
    formulario = CategoriaForm()
    if formulario.validate_on_submit():
        nova_categoria = Categoria(id_usuario=current_user.id,nome=formulario.nome.data, tipo=formulario.tipo.data)
        db.session.add(nova_categoria)
        db.session.commit()
        return redirect(url_for("usuariobp.add_categoria"))
    return render_template('form_categoria.html',form=formulario)


@user.route('/editar-categoria/<int:id>',methods=["GET","POST"])
@login_required
def editar_categoria(id):
    categoria_selecionada = Categoria.query.filter_by(id=id).first()
    form = CategoriaForm(obj=categoria_selecionada)
    form.salvar.label.text="salvar"
    if form.validate_on_submit():
        form.populate_obj(categoria_selecionada)
        db.session.commit()
        return redirect(url_for("usuariobp.categorias"))
        
    return render_template("form_categoria.html", form=form,)


@user.route('/teste')
def teste():
    return "teste"