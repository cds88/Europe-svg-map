export const FETCH_COUNTRIES_BEGIN = 'FETCH_COUNTRIES_BEGIN';
export const FETCH_COUNTRIES_SUCCESS = 'FETCH_COUNTRIES_SUCCESS';
export const FETCH_COUNTRIES_ERROR = 'FETCH_COUNTRIES_ERROR';

import * as dataTypes from './DataTypes';



//INTERFACES
export interface FetchCountriesBegin{
    type: typeof FETCH_COUNTRIES_BEGIN
}
 export interface FetchCountriesSuccess{
    type: typeof FETCH_COUNTRIES_SUCCESS;
    countries: dataTypes.Country[]
}
 export interface FetchCountriesError{
    type: typeof FETCH_COUNTRIES_ERROR
}
 




//TYPES
export type DataActionTypes=
    | FetchCountriesBegin 
    | FetchCountriesSuccess 
    | FetchCountriesError 
    | null

export type AppActions = DataActionTypes;


