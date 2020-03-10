import {DataActionTypes} from '../reducer_data/DataActions';
import {InterfaceActionTypes} from '../reducer_interface/InterfaceActions';
 
export type AllActionTypes=
        | DataActionTypes
         | InterfaceActionTypes
         | null ;
 


export type AllAppActions = AllActionTypes