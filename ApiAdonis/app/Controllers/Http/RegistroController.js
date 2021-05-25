'use strict'

const Database = use('Database')
const Persona = use('App/Models/Persona')

class RegistroController {
  async MostrarRegistros (){
    return await Persona.all();
  }

  async CrearRegistro({request}){
    const persona = new Persona();
    persona.nombre = request.input('nombre');
    persona.edad = request.input('edad');
    persona.save();

    return {
      mensaje: 'Usuario resgitrado',
      registro: persona
    };
  }

  async EditarRegistro({request}){
    const persona = await Persona.find(request.input('id'));
    let mensaje;
    if (persona){
      persona.nombre = request.input('nombre');
      persona.edad = request.input('edad');
      persona.save();

      mensaje = 'Se editó el usuario';
    } else {
      mensaje = 'No se encontró ninguna persona con este id';
    }

    return {
      mensaje: mensaje,
      registro: persona
    };
  }

  async EliminarRegistro({request}){
    const persona = await Persona.findOrFail(request.input('id'));
    let mensaje;
    if (persona){
      persona.delete();

      mensaje = 'Se eliminó el usuario';
    } else {
      mensaje = 'No se encontró ninguna persona con este id';
    }

    return {
      mensaje: mensaje,
      registro: persona
    };
  }
}

module.exports = RegistroController
