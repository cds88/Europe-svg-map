
import * as React from "react";


import { AllAppActions } from '../reducers/actions/AllActionsTypes';

import { ThunkDispatch }  from "redux-thunk";
import { bindActionCreators }  from 'redux';
import {AppState} from "../reducers/ConfigureStore";
import {connect} from 'react-redux';

import {CSSTransition, TransitionGroup} from 'react-transition-group';
import {motion} from 'framer-motion';
export interface DetailsContentProps{
    id: number;
    title:string;
    content: string;


}

interface LinkStateToProps{}

const mapStateToProps=(state:AppState,
ownProps:DetailsContentProps):LinkStateToProps=>
({ } ) 

interface LinkDispatchToProps{}

const mapDispatchToProps=(
    dispatch: ThunkDispatch<any, any, AllAppActions>,
    ownProps: DetailsContentProps
):LinkDispatchToProps=>({})

type Props =DetailsContentProps & LinkStateToProps & LinkDispatchToProps;

const DetailsContentComponent=(Props:Props)=>{
return (
  <TransitionGroup>
    <CSSTransition
      key={JSON.stringify(Props.id)}
      timeout={900}
      classNames="fade"
    >
      <div>
        <h1>{Props.title}</h1>
        <p>{Props.content}</p>
      </div>
    </CSSTransition>
  </TransitionGroup>
);

}

export default connect(null, null)(DetailsContentComponent)
