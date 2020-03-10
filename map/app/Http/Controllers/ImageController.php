<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\Log;
use App\Image;
use App\Http\Resources\Image as ImageResource;
use Illuminate\Http\Request;

class ImageController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
         //$out = new \Symfony\Component\Console\Output\ConsoleOutput();
       //$out->writeln("Hello from Terminal");
        
        // Log::channel('stderr')->info('Something happened!');


        $images = Image::with('country')->get();
        
        //return ImageResource::collection(Image::with('country')->get());
        return ImageResource::collection(Image::paginate(50));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create(Request $request)
    {
 

    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */

    public function create_dir(String $pathname)
    {



    }
    public function store(Request $request)
    {
       
        
        $out = new \Symfony\Component\Console\Output\ConsoleOutput();
        //$out->writeln( $request->input('name') );

       

        //$out->writeln("its ok ");
        if($request->hasFile('image')){


            $country_name = $request->input('country_name');
            $country_id   = $request->input('country_id');


            $imageNameWithExt = $request->file('image')->getClientOriginalName();

 
             $filename         = pathinfo($imageNameWithExt, PATHINFO_FILENAME);
 
             $extension        = $request->file('image')->getClientOriginalExtension();
           $filenameToStore  = $filename . '_' . time() . '.' . $extension;

             $out->writeln($filenameToStore);



           // $out->writeln($country_name."  ".$country_id);
          //  $out->writeln(public_path());
            
            // if( !is_dir('images/') ){
            //     mkdir('images/');
         
            // }

            // if( !is_dir('images/'.$country_name)){
            //     mkdir('images/'.$country_name);
            
            // }
            
           
           // $imagename=$request->image->getClientOriginalName();
        
           
        $request->image->storeAs('public/images/' . $country_name, $filenameToStore);


        $image = new Image;
        $image->country_id = $request->input('country_id');
        $image->path       = $filenameToStore;
        $image->save();
        }
        else{
            $out->writeln("not any files");
        }




        
    // $entityBody = file_get_contents('php://input');

      //  dd($request);
     //   Log::channel('stderr')->info($request->input());

 

        // $image = $request->isMethod('put') ? Image::findOrFail       ($request->image_id) : new Image;

        // $image->id = $request->input('image_id');
        // $image->title = $request->input('title')

    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
