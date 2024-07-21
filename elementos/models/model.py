from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime
import uuid

Base = declarative_base()
db = SQLAlchemy()


class Elemento(db.Model):
    __tablename__ = 'elemento'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_elemento = db.Column(db.String)
    tipo = db.Column(db.String)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    notas = db.Column(db.String)

    __mapper_args__ = {
        'polymorphic_identity': 'ELEMENTO',
        'polymorphic_on': tipo
    }

class ElementoSecreto(Elemento):
    __tablename__ = 'elemento_secreto'
    
    id = db.Column(db.Integer, db.ForeignKey('elemento.id'), primary_key=True)
    secreto = db.Column(db.String)
    clave_id = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'SECRETO',
    }

class ElementoLogin(Elemento):
    __tablename__ = 'elemento_login'
    
    id = db.Column(db.Integer, db.ForeignKey('elemento.id'), primary_key=True)
    usuario = db.Column(db.String)
    url = db.Column(db.String)
    email = db.Column(db.String)
    clave_id = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'LOGIN',
    }

class ElementoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Elemento
        load_instance = True

class ElementoSecretoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ElementoSecreto
        load_instance = True

class ElementoLoginSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ElementoLogin
        load_instance = True