import datetime
from config import db

#clase que es modelo relacionado a la base de datos
class PersonasModel(db.Model):
    __tablename__ = 'personas'
    id_persona = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    edad = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)