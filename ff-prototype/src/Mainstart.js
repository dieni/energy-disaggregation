import React from 'react';
import './Mainstart.css';
import Greeting from './greeting';
import Greetinfo from './greetinfo';
import Picture from './picture';
import { Link } from 'react-router-dom';
import pic from './images/smile.jpg';
import { Header, Grid, Progress } from 'semantic-ui-react';
import { Column, Row } from 'simple-flexbox';




function Mainstart() {
  return (


    <div className="bg">
      <div >
        {/* <div className="cent"> */}
        <Column flexGrow={1}>
          <Row horizontal='center' vertical='center'>
            {/* <Header as='h1' >Hello I am Pluggy</Header> */}
            <h1>Hello I am Pluggy</h1>
          </Row>
        </Column>

        {/* <Greeting /> */}
        {/* <div className="cent"> */}

        <Link to='/savinghint'>
          <Picture />
          {/* <img class="ui fluid image" src={pic} /> */}
        </Link>


        {/* <Header as='h1' >let's clean your energy household</Header> */}
        <h1>let's clean your energy household</h1>



        {/* </div> */}
        {/* <Greetinfo /> */}
        {/* <Progress percent={100} success> The progress was successful</Progress> */}

      </div>
    </div >


  );
}

export default Mainstart;






