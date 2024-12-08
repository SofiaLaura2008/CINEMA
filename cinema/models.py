from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime
from datetime import datetime
from flask_login import UserMixin
from . import db

#Tabelas de entidades simples
# Tabela de Usuario
class Usuario(db.Model, UserMixin):#User mixin adiciona os métodos necessários para o Flask-Login funcionar, como is_authenticated, is_active
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome= db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    data_nascimento = db.Column(db.Date)
    is_admin = db.Column(db.Boolean, default=False)  

    def __init__(self, nome, email, senha, data_nascimento, is_admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_nascimento = data_nascimento
        self.is_admin = is_admin

    def __repr__(self):
        return f"Usuario('{self.nome}', '{self.email}', '{self.data_nascimento}', admin={self.is_admin})"

# Tabela de Filmes
class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(200), nullable=False, index=True)
    duracao = db.Column(db.Integer, nullable=False)
    classificacao = db.Column(db.String(10), nullable=False)
    genero = db.Column(db.String(50))
    data_lancamento = db.Column(db.Date)
    foto = db.Column(db.String(255))  

# Tabela dos Cinemas
class Cinema(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    local = db.Column(db.String(255), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)

# Tabela de Salas
class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero = db.Column(db.String(10), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'), nullable=False)

    cinema = db.relationship('Cinema', backref=db.backref('salas', lazy=True))

# Tabela de Sessões
class Sessao(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filme_id = db.Column(db.Integer, db.ForeignKey('filme.id'), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('sala.id'), nullable=False)
    horario = db.Column(db.DateTime, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    filme = db.relationship('Filme', backref=db.backref('sessoes', lazy=True))
    sala = db.relationship('Sala', backref=db.backref('sessoes', lazy=True))


#Tabela de alimementos
class Alimento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False) 
    quantidade = db.Column(db.Integer, nullable=False)
    tipoDeAlimentos = db.Column(db.String(50))

#Tabela de ngócios
# Tabela de Compra de Assentos
class AssentoComprado(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sessao_id = db.Column(db.Integer, db.ForeignKey('sessao.id'), nullable=False)
    assento = db.Column(db.String(10), nullable=False)

    sessao = db.relationship('Sessao', backref=db.backref('assentos_comprados', lazy=True))

# Tabela de Compra de Sessões
class CompraSessao(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sessao_id = db.Column(db.Integer, db.ForeignKey('sessao.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    subtotal = db.Column(db.Float, nullable=False)

    sessao = db.relationship('Sessao', backref=db.backref('compras', lazy=True))



#Tabela de compra de alimentos
class CompraAlimento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alimento_id = db.Column(db.Integer, db.ForeignKey('alimento.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    preco_unitario = db.Column(db.Float, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)

    alimento = db.relationship('Alimento', backref=db.backref('compras', lazy=True))




