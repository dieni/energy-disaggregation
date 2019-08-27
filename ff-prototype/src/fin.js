import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './fin.css';
import PluggyFinalHeader from './pluggyheadertwo'
import ButtonExampleGroup from './radiobuttons'
import { Header, Icon, Button, Form } from 'semantic-ui-react'



function fin() {
    return (
        <div className='bckg'>
            <PluggyFinalHeader />
            <Header as='h1' color='black'>How much of your savings do you want to donate?</Header>
            <div className="ctr">
                <Header as='h1' textAlign='right'>
                    <Icon name='plug' />
                    <Header.Content>200€</Header.Content>
                </Header>

                {/* <Button.Group>
                    <Button>20%</Button>
                    <Button>5%</Button>
                    <Button>0%</Button>
                </Button.Group> */}
                {/* <Form> */}
                {/* <Form.Group> */}
                <Form.Field label='20%' control='input' type='radio' name='htmlRadios' />
                <Form.Field label='10%' control='input' type='radio' name='htmlRadios' />
                <Form.Field label='00%' control='input' type='radio' name='htmlRadios' />
                {/* </Form.Group> */}
                {/* </Form> */}
                <Button positive content='Submit' />
            </div>
        </div >
    );
}

export default fin;