import React from 'react'
import { Button, Icon, Image, Item, Label } from 'semantic-ui-react'
import pv from './images/pv.jpg'
import battery from './images/recycle.jpg'
import { Link } from 'react-router-dom';
import './Mainstart.css';


const paragraph = <Image src='https://react.semantic-ui.com/images/wireframe/short-paragraph.png' />

const ItemExampleDivided = () => (
    // <div className="bg">
    < Item.Group divided>

        <Item>
            <Item.Image src={pv} />

            <Item.Content>
                <Item.Header as='a'>GreenPV</Item.Header>
                <Item.Meta>
                    <span className='cinema'>Energy production</span>
                </Item.Meta>
                <Item.Description>Lorem ipsum dolor sit amet</Item.Description>
                <Item.Extra>
                    <Link to='/fin' >
                        <Button primary floated='right'>
                            Choose
            <Icon name='right chevron' />
                        </Button>
                    </Link>
                    {/* <Label>Limited</Label> */}
                </Item.Extra>
            </Item.Content>
        </Item>

        <Item>
            <Item.Image src={battery} />

            <Item.Content>
                <Item.Header as='a'>Battery Recycler</Item.Header>
                <Item.Meta>
                    <span className='cinema'>Recycling</span>
                </Item.Meta>
                <Item.Description>Lorem ipsum dolor sit amet</Item.Description>
                <Item.Extra>
                    <Link to='/fin' >
                        <Button primary floated='right'>
                            Choose
            <Icon name='right chevron' />
                        </Button>
                    </Link>
                </Item.Extra>
            </Item.Content>
        </Item>
    </Item.Group >
    // </div>
)

export default ItemExampleDivided
