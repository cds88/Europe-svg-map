
import * as React from 'react';
import Master from './Master';
 

import { Provider } from 'react-redux';

 
import { store } from "./reducers/ConfigureStore";

const App = () => {
    return (
        <Provider store={store} >
        <Master/>
        </Provider>
    )
}

export default App;
