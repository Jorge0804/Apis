from flask import jsonify
from flask_restful import Resource, reqparse
from models import PersonasModel
from config import db

#argumentos/parametros para tomar de los requests
args_persona = reqparse.RequestParser()
args_persona.add_argument('nombre',type=str)
args_persona.add_argument('edad',type=int)

#clase con los métodos de las rutas por verbos(GET, POST)
class UsuarioModel(Resource):
    def get(self):
        try:
            response = UsuarioModel.query.all()
            response = [{
                'id_persona':i.id_persona,
                'nombre':i.nombre,
                'edad':i.edad,
                'created_at':i.created_at,
                'updated_at':i.updated_at} for i in response]
            return jsonify(response)
        except:
            return {
                'error' : 'Error al obtener los usuarios flask'
            }