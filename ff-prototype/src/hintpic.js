import React from 'react'
import { Header, Image } from 'semantic-ui-react'
import headerpic from './images/smile.png';

const HeaderExampleImage = () => (
    <Header as='h3' color='black'>
        <Image circular src={headerpic} />
        <Header.Content>
            Pluggy
            <Header.Subheader color='black'>Here are your personal energy saving hints</Header.Subheader>
        </Header.Content>
    </Header>
)

export default HeaderExampleImage
