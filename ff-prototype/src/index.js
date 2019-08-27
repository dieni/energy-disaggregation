import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Mainstart from './Mainstart';
// import mainpage from './mainpage';
import * as serviceWorker from './serviceWorker';
import 'semantic-ui-css/semantic.min.css';
import { BrowserRouter } from 'react-router-dom';
import App from './App';



ReactDOM.render((
    <BrowserRouter>
        <App />
    </BrowserRouter>
), document.getElementById('root'));
// registerServiceWorker();