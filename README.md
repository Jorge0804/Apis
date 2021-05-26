# Apis
Apis (Laravel, Adonis, Flask)

BASE DE DATOS
 > Para estas practicas no se hizo ninguna migración sino que se creo la BD y tablas de manera directa, pero adjunto el script.

----------------------------------
CREATE DATABASE apidb;

CREATE TABLE personas(
  id_persona int primary key auto_increment,
  nombre varchar(80),
  edad int
);
----------------------------------

PETICIONES (Las peticiones funcionan por igual para los 3 proyectos)
- Visualizar (/MostrarRegistros) [GET]
- Agregar (/CrearRegistro) [POST]
  > nombre -
  > edad
- Editar (/EditarRegistro) [POST]
  > id - 
  > nombre - 
  > edad
- Eliminar (/EliminarRegistro) [POST]
  > id