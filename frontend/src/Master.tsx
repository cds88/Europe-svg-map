import DetailsContentComponent from "./components/DetailsContentComponent" 
import ModalComponent from "./components/ModalComponent" 

import DetailsComponent from "./components/DetailsComponent" 
import TrakComponent from "./components/TrakComponent" 
 
import EuropeComponent from "./components/EuropeComponent"
 
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import "bootstrap/dist/css/bootstrap.css";
import './styles/Master.scss';
import styled from "styled-components";
import axios from 'axios';
import { AllAppActions } from './reducers/actions/AllActionsTypes';
import { connect } from 'react-redux';
import { ThunkDispatch } from "redux-thunk";
import { bindActionCreators } from 'redux';
import { AppState } from "./reducers/ConfigureStore";
import {FetchCountries} from './reducers/actions/AllActions';
import {GetCurrentCountry} from './reducers/actions/AllActions';
 
import {Country} from './reducers/reducer_data/DataTypes';

export interface MasterProps {

}

interface LinkStateToProps{
  currentCountry: string;
  isModalOpened: boolean;
}
const mapStateToProps=(state:AppState, ownProps: MasterProps):LinkStateToProps=>({
  currentCountry: state.InterfaceReducer.CurrentCountry,
  isModalOpened: state.InterfaceReducer.isModalOpened
})  
interface LinkDispatchToProps{
    fetchCountries:()=>void;
    getCurrentCountry:()=> void;
}
const mapDispatchToProps=(dispatch: ThunkDispatch<any, any, AllAppActions>, ownProps: MasterProps):LinkDispatchToProps=>({
    fetchCountries: bindActionCreators(FetchCountries, dispatch),
    getCurrentCountry: bindActionCreators(GetCurrentCountry, dispatch)
})
type Props = MasterProps & LinkStateToProps & LinkDispatchToProps;
const Master = (Props: Props) => {

  let imageGallery: any = null;
  const [image, setImage] = React.useState(null);
  const galleryPrev = () => {
    imageGallery.slickPrev();
  }
  const galleryNext = () => {
    imageGallery.slickNext();
  }
 
    React.useEffect(
        ()=>{
      
            Props.fetchCountries();
        },[])
    
    React.useEffect(()=>{
      
     
    },[Props.currentCountry])
 
 
    return (
      <div className="container-fluid">
 
        <div className="row" id="main-page">


          <EuropeComponent isModalOpened={Props.isModalOpened}/>
          <DetailsComponent />

        {Props.isModalOpened ?
          // <div className="modalic">
          //   <p style={{color:"white"}}>  {Props.currentCountry} </p>
          // </div> 
          <ModalComponent isModalOpened={Props.isModalOpened} country_id={Props.currentCountry}/>
          
          : null

        }
 
        </div>
 

      </div>
    );

}

export default connect(mapStateToProps, mapDispatchToProps)(Master);





