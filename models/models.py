from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class Transacao(db.Model):
    __tablename__ = 'transacao'
    
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.ForeignKey('usuario.id'), nullable=False)
    tipo = db.Column(db.Enum('receita', 'despesa'))
    descricao = db.Column(db.String(50))
    valor = db.Column(db.Numeric(precision=10, scale=2))
    categoria = db.Column(db.String(50))
    data = db.Column(db.Date)
    


class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.ForeignKey('usuario.id'), nullable=False)
    nome = db.Column(db.String(50))
    tipo = db.Column(db.Enum('receita', 'despesa'))
    
    
    

class Usuario(UserMixin,db.Model):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(100))
    transacoes = db.relationship('Transacao', backref='usuario', lazy=True)
    categorias = db.Relationship('Categoria', backref='usuario', lazy=True)
    
    def AdicionarCategoriasPadrao(self):
        categorias_despesa = [Categoria(id_usuario=self.id, nome=cat,tipo='despesa') for cat in ['alimentacao','contas','roupas','educacao','saude']]
        for cat in categorias_despesa:
            db.session.add(cat)
        db.session.commit()
        
        categorias_receita = [Categoria(id_usuario=self.id, nome=cat,tipo='receita') for cat in ['salario','hora extra','investimentos']]
        for cat in categorias_receita:
            db.session.add(cat)
        db.session.commit()
        
    
    