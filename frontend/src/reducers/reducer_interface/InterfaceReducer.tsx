
import {IInterfaceState} from "./InterfaceTypes";
import {InterfaceActionTypes} from "./InterfaceActions";
import * as constants from './InterfaceActions';

const InterfaceReducerDefaultState : IInterfaceState = {
    CurrentCountry :null,
    isModalOpened: false,
    countryHovered: null,
    CurrentCountryDetails: null

}


const InterfaceReducer=(
        state = InterfaceReducerDefaultState,
        action: InterfaceActionTypes
        ):IInterfaceState => {
            switch(action.type){

        case constants.SET_CURRENT_COUNTRY_DETAILS:
            return {...state, CurrentCountryDetails:action.country };

        case constants.SET_HOVERED:
                    return { ...state, countryHovered: action.country_id };

        case constants.CLOSE_MODAL:
            return {...state, isModalOpened:false };

        case constants.OPEN_MODAL:
            return {...state, isModalOpened:true};

        case constants.SET_CURRENT_COUNTRY:
            return {...state, CurrentCountry: action.country}
        default:
            return state;
            }
        }

        
export {InterfaceReducer}


