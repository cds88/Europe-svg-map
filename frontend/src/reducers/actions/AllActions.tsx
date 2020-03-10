import * as dataConstants from '../reducer_data/DataActions';
import * as dataTypes from '../reducer_data/DataTypes';
import * as interfaceConstants from '../reducer_interface/InterfaceActions'
 

import { Dispatch } from "redux";
import { AppState } from '../ConfigureStore';
import {AllAppActions} from './AllActionsTypes';
import axios from 'axios';


//METHODS
export const SetCurrentCountryDetails=(country: dataTypes.Country):AllAppActions=>({
                type: interfaceConstants.SET_CURRENT_COUNTRY_DETAILS,
                country
})
            export const SetHovered=(country_id:string):AllAppActions=>({
                type: interfaceConstants.SET_HOVERED,
                country_id
})
            export const CloseModal=():AllAppActions=>({
                type: interfaceConstants.CLOSE_MODAL
})
            export const OpenModal=():AllAppActions=>({
                type: interfaceConstants.OPEN_MODAL
})
            export const FetchCountriesBegin=():AllAppActions=>({
                type: dataConstants.FETCH_COUNTRIES_BEGIN
})
            export const FetchCountriesSuccess=(countries: dataTypes.Country[]):AllAppActions=>({
                type: dataConstants.FETCH_COUNTRIES_SUCCESS,
                countries
})
            export const FetchCountriesError=():AllAppActions=>({
                type: dataConstants.FETCH_COUNTRIES_ERROR
})
            export const SetCurrentCountry=(country: string):AllAppActions=>({
                type: interfaceConstants.SET_CURRENT_COUNTRY,
                country
})
 
export const FetchCountries=()=>{
    return(dispatch: Dispatch<AllAppActions>, getState:()=>AppState)=>{

 
        dispatch(FetchCountriesBegin());
        axios.get('http://127.0.0.1:8000/api/elements').then(e=> dispatch(FetchCountriesSuccess(  (e.data.data ))) )


    }
}
export const SetCountry=(country_id:string)=>{
    return(dispatch: Dispatch<AllAppActions>, getState:()=>AppState)=>{
        
        dispatch(SetCurrentCountry(country_id));
 

    }
}
export const ResetCurrentCountryDetails=()=>{
    return(dispatch: Dispatch<AllAppActions>, getState:()=>AppState)=>{

    }

}
export const GetCurrentCountry=()=>{
    return(dispatch: Dispatch<AllAppActions>, getState:()=>AppState)=>{
        var currentCountry = getState().InterfaceReducer.CurrentCountry;
        var countries = getState().DataReducer.Countries;
        console.log(countries);
        console.log("O CRAP");

        //return getState().DataReducer.Countries[parseInt(currentCountry)]
    }
}

export const OpenModalController=()=>{
    return(dispatch: Dispatch<AllAppActions>, getState:()=>AppState)=>{
        
        var country_id = getState().InterfaceReducer.CurrentCountry;

        var countries = getState().DataReducer.Countries
        var current_country = countries[parseInt(country_id)-1];
        dispatch(SetCurrentCountryDetails(current_country));
        dispatch(OpenModal());

    }
}