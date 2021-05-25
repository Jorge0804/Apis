from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import PersonasModel
from flask_restful import Resource, reqparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/apidb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

req_persona = reqparse.RequestParser()
req_persona.add_argument('nombre',type=str)
req_persona.add_argument('edad',type=int)


@app.route('/MostrarRegistros')
def MostrarRegistros():
    try:
        response = PersonasModel.query.all()
        response = [{
           'id_persona':i.id_persona,
           'nombre':i.nombre,
           'edad':i.edad,
           'created_at':i.created_at,
           'updated_at':i.updated_at
           }
           for i in response]
        return jsonify(response)
    except:
        return jsonify({
            'mensaje':'No se encontró ningun usuario'
        })

@app.route('/CrearRegistro', methods = ['POST'])
def CrearRegistro():
    try:
        persona = PersonasModel(
            nombre = request.form['nombre'],
            edad = request.form['edad']
        )
        db.session.add(persona)
        db.session.commit()

        return {
            'mensaje': 'Usuario registrado',
            'registro': persona.nombre
        }
    except:
        return {
            'mensaje': 'No se pudo hacer el registro'
        }

@app.route('/EditarRegistro', methods = ['POST'])
def EditarRregistro():
    try:
        persona = PersonasModel.query.filter_by(id_persona = request.form['id']).first()
        persona.id_persona = request.form['id']
        persona.nombre = request.form['nombre']
        persona.edad = request.form['edad']
        db.session.commit()

        return {
            'mensaje': 'Se editó el registro',
            'registro': persona.nombre
        }
    except:
        return {
            'mensaje':'No se encontró ninguna persona con este id'
        }

@app.route('/EliminarRegistro', methods = ['POST'])
def EliminarRegistro():
    persona = PersonasModel.query.get(request.form['id'])
    db.session.delete(persona)
    db.session.commit()
    return {
           'mensaje': 'Se eliminó el registro',
           'registro': ' '
    }