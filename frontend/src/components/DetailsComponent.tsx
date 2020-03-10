
import * as React from "react";


import { AllAppActions } from '../reducers/actions/AllActionsTypes';

import { ThunkDispatch }  from "redux-thunk";
import { bindActionCreators }  from 'redux';
import {AppState} from "../reducers/ConfigureStore";
import {connect} from 'react-redux';

import * as dataTypes from '../reducers/reducer_data/DataTypes';

import DetailsContentComponent from './DetailsContentComponent';

import {AnimatePresence, motion} from 'framer-motion';

export interface DetailsProps{}

interface LinkStateToProps{
    countries : dataTypes.Country[];
    currentCountry : string;
}

const mapStateToProps=(state:AppState,
ownProps:DetailsProps):LinkStateToProps=>
({
    countries: state.DataReducer.Countries,
    currentCountry: state.InterfaceReducer.CurrentCountry

  } ) 

interface LinkDispatchToProps{}

const mapDispatchToProps=(
    dispatch: ThunkDispatch<any, any, AllAppActions>,
    ownProps: DetailsProps
):LinkDispatchToProps=>({})

type Props =DetailsProps & LinkStateToProps & LinkDispatchToProps;

const DetailsComponent=(Props:Props)=>{

    if(!Props.countries || Props.countries.length===0){
        return <h1>LOADING INFO</h1>
    }
    if(!Props.currentCountry){
        return <h1>SELECT COUNTRY</h1>
    }

return (
  <div className="col-xs-12 col-sm-12 col-md-12 col-lg-2 additional-content">
    <div id="additional-content-wrapper">


      

      <DetailsContentComponent 
      id={Props.countries[parseInt(Props.currentCountry)-1].country.id }
      title={Props.countries[parseInt(Props.currentCountry) - 1].country.title} content={Props.countries[parseInt(Props.currentCountry) - 1].country.about} />

 
    </div>
  </div>
);

}

export default connect(mapStateToProps, mapDispatchToProps)(DetailsComponent)
