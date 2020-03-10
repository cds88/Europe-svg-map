
    import * as React from "react";
 

    import { AllAppActions } from '../reducers/actions/AllActionsTypes';

    import { ThunkDispatch }  from "redux-thunk";
    import { bindActionCreators }  from 'redux';
    import {AppState} from "../reducers/ConfigureStore";
    import {connect} from 'react-redux';

    export interface TrakProps{}

    interface LinkStateToProps{}

    const mapStateToProps=(state:AppState,
    ownProps:TrakProps):LinkStateToProps=>
    ({ } ) 

    interface LinkDispatchToProps{}

    const mapDispatchToProps=(
        dispatch: ThunkDispatch<any, any, AllAppActions>,
        ownProps: TrakProps
    ):LinkDispatchToProps=>({})

    type Props =TrakProps & LinkStateToProps & LinkDispatchToProps;

    const TrakComponent=(Props:Props)=>{
    return(
        <div> </div>
    )
    
    }

    export default connect(null, null)(TrakComponent)
    