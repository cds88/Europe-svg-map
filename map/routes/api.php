<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider     within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});


Route::get('countries', array('middleware'=>'cors', 'uses'=>'CountryController@index'));

Route::get('elements', array('middleware'=>'cors', 'uses'=>'ElementController@index') );

Route::get('images', array('middleware'=>'cors',
'uses'=>'ImageController@index'));

Route::post('image', array('middleware'=>'cors', 'uses'=>'ImageController@store')); 