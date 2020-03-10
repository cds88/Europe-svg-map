<?php

namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\JsonResource;
use App\Http\Resources\Image as ImageResource;
class Country extends JsonResource
{
 
    public function toArray($request)
    {
        return [
          'id'=>$this->id,
          'title'=>$this->title,
          'population'=>$this->population,
          'about'=>$this->about,
          'area'=>$this->area,
          'density'=>$this->density,
          'capital'=>$this->capital,
          'language'=>$this->language,
          'images'=>ImageResource::collection($this->whenLoaded('images'))
        ];
    }
}
 