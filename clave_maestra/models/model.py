from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime

Base = declarative_base()
db = SQLAlchemy()


class ClaveMaestra(db.Model):
    __tablename__ = 'claves_maestras'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)


class ClaveMaestraSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ClaveMaestra
        load_instance = True