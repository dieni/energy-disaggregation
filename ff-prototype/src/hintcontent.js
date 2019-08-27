import React from 'react'
import { Button, Card, Image, ButtonGroup } from 'semantic-ui-react'
import bulb from './images/bulb.jpg'
import { Link } from 'react-router-dom';


const CardExampleGroups = () => (
    <Card>
        <Card.Content>
            <Image floated='right' size='medium' src={bulb} />
            <Card.Header>Hint#1</Card.Header>
            {/* <Card.Meta>Friends of Elliot</Card.Meta> */}
            <Card.Description>
                Change your light bulbs to LED bulbs and <strong>save</strong> up to 150€ each year
            </Card.Description>
        </Card.Content>
        <Card.Content extra>
            <Button.Group>
                <Link to='/savinghinttwo' >
                    <Button negative fluid>Decline</Button>
                    {/* <Button.Or /> */}
                </Link>
                <Link to='/savinghinttwo' >
                    <Button positive fluid>Accept</Button>
                </Link >
            </Button.Group>
        </Card.Content>
    </Card>

)

export default CardExampleGroups

