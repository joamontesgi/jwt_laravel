<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;


/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/


Route::post('login', [AuthController::class, 'login']);
Route::post('register', [AuthController::class, 'register']);

Route::middleware(['auth:api', 'role:admin|docente'])->group(function () {
    Route::post('logout', [AuthController::class, 'logout']);
});
Route::middleware(['auth:api', 'role:admin'])->group(function () {
    Route::get('/admin', function () {
        return "admin";
    });
});

Route::middleware(['auth:api', 'role:docente'])->group(function () {
    Route::get('/docente', function () {
        return "docente";
    });
});
