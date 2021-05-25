<?php

namespace App\Http\Controllers;

use App\Models\personas;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Http\Request;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Support\Facades\DB;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function MostrarRegistros(){
        echo json_encode(personas::all());
    }

    public function CrearRegistro(Request $r){
        $persona = new personas();
        $persona->nombre = $r->input('nombre');
        $persona->edad = $r->input('edad');
        $persona->save();

        echo  json_encode(array(
            'mensaje' => 'Usuario registrado',
            'registro' => $persona
        ));
    }

    public function EditarRegistro(Request $r){
        $persona = personas::find($r->id);
        if ($persona){
            $mensaje = 'Se editó el usuario';

            $persona->nombre = $r->input('nombre');
            $persona->edad = $r->input('edad');
            $persona->update();
        } else{
            $mensaje = 'No se encontró ninguna persona con este id';
        }

        echo json_encode(array(
            'mensaje' =>$mensaje,
            'registro' => $persona
        ));
    }

    public function EliminarRegistro(Request $r){
        $persona = personas::find($r->id);
        if ($persona){
            $persona->delete();
            $mensaje = 'Se eliminó el siguiente registro';
        } else{
            $mensaje = 'No se encontró ninguna persona con este id';
        }

        echo json_encode(array(
            'mensaje' =>$mensaje,
            'registro' => $persona
        ));
    }
}
