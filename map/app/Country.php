<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Country extends Model
{
    
    protected $fillable = [];

    public function element()
    {
        return $this->hasOne(Element::class);
    }

    public function images()
    {
        return $this->hasMany(Image::class);
    }

}
