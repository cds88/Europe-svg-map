
    import * as React from "react";
 

    import { AllAppActions } from '../reducers/actions/AllActionsTypes';

    import { ThunkDispatch }  from "redux-thunk";
    import { bindActionCreators }  from 'redux';
    import {AppState} from "../reducers/ConfigureStore";
    import {connect} from 'react-redux';

    export interface DefaultProps{}

    interface LinkStateToProps{}

    const mapStateToProps=(state:AppState,
    ownProps:DefaultProps):LinkStateToProps=>
    ({ } ) 

    interface LinkDispatchToProps{}

    const mapDispatchToProps=(
        dispatch: ThunkDispatch<any, any, AllAppActions>,
        ownProps: DefaultProps
    ):LinkDispatchToProps=>({})

    type Props =DefaultProps & LinkStateToProps & LinkDispatchToProps;

    const DefaultComponent=(Props:Props)=>{
    return(
        <div> </div>
    )
    
    }

    export default connect(null, null)(DefaultComponent)
    