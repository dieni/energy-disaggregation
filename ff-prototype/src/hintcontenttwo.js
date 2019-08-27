import React from 'react'
import { Button, Card, Image } from 'semantic-ui-react'
import fridge from './images/fridge.jpg'
import { Link } from 'react-router-dom';


const HintCardTwo = () => (
    <Card>
        <Card.Content>
            <Image floated='right' size='medium' src={fridge} />
            <Card.Header>Hint#2</Card.Header>
            {/* <Card.Meta>Friends of Elliot</Card.Meta> */}
            <Card.Description>
                Replace your old fridge with n exo-friendly one and <strong>save</strong> up to 200€ each year
            </Card.Description>
        </Card.Content>
        <Card.Content extra>
            <Link to='/chooseproject' >
                <Button negative>
                    Decline
                    </Button>
            </Link>
            <Link to='/chooseproject' >
                <Button positive>
                    Accept
          </Button>
            </Link >
        </Card.Content>
    </Card>

)

export default HintCardTwo
