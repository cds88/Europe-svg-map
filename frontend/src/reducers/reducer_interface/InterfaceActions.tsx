export const SET_CURRENT_COUNTRY_DETAILS = 'SET_CURRENT_COUNTRY_DETAILS';
export const SET_HOVERED = 'SET_HOVERED';
export const CLOSE_MODAL = 'CLOSE_MODAL';
export const OPEN_MODAL = 'OPEN_MODAL';
export const SET_CURRENT_COUNTRY = 'SET_CURRENT_COUNTRY';

import {Country} from '../reducer_data/DataTypes';



//INTERFACES
export interface SetCurrentCountryDetails{
    type: typeof SET_CURRENT_COUNTRY_DETAILS
    country: Country
}
 export interface SetHovered{
    type: typeof SET_HOVERED;
    country_id: string;
}
 export interface CloseModal{
    type: typeof CLOSE_MODAL
}
 export interface OpenModal{
    type: typeof OPEN_MODAL
}
 export interface SetCurrentCountry{
    type: typeof SET_CURRENT_COUNTRY;
    country : string;
 
}
 




//TYPES
export type InterfaceActionTypes=
    | SetCurrentCountryDetails 
    | SetHovered 
    | CloseModal 
    | OpenModal 
    | SetCurrentCountry 
    | null

export type AppActions = InterfaceActionTypes;


