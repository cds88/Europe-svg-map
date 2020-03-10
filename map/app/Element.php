<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Element extends Model
{
    protected $fillable = [];   

    public function country()
    {
        return $this->belongsTo(Country::class);
    }
}
