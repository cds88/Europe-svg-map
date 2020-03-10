
import {IDataState} from "./DataTypes";
import {DataActionTypes} from "./DataActions";
import * as constants from './DataActions';

const DataReducerDefaultState : IDataState = {
    Countries: null
}


const DataReducer=(
        state = DataReducerDefaultState,
        action: DataActionTypes
        ):IDataState => {
            switch(action.type){

        case constants.FETCH_COUNTRIES_BEGIN:
            return state;
        case constants.FETCH_COUNTRIES_SUCCESS:
            return {...state, Countries:action.countries};
        case constants.FETCH_COUNTRIES_ERROR:
            return state;
                default:
                    return state;
            }
        }

        
export {DataReducer}


