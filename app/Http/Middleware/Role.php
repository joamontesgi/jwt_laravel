<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class Role
{

    public function handle(Request $request, Closure $next, $roles)
    {
        $rol = explode('|', $roles);
        $roleName = $request->user()->role->label;
        if (!in_array($roleName, $rol)) {
            return response()->json(['error' => 'No tienes permisos para acceder a esta ruta'], 401);
        }
        return $next($request);
    }
}
