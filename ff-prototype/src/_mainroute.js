import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Mainstart from './Mainstart';
import hint from './hint';
import hinttwo from './hinttwo';
import chooseproject from './chooseproject';
import fin from './fin'

//https://blog.pusher.com/getting-started-with-react-router-v4/
const MainRoute = () => (
    <Switch>
        <Route exact path='/' component={Mainstart}></Route>
        <Route exact path='/savinghint' component={hint}></Route>
        <Route exact path='/savinghinttwo' component={hinttwo}></Route>
        <Route exact path='/chooseproject' component={chooseproject}></Route>
        <Route exact path='/fin' component={fin}></Route>
    </Switch>
);

export default MainRoute;