import React from 'react'
import { Header, Image } from 'semantic-ui-react'
import headerpic from './images/smile.png';

const PluggyFinalHeader = () => (
    <Header as='h3' color='black'>
        <Image circular src={headerpic} />
        <Header.Content>
            Pluggy
            <Header.Subheader color='black'>your possible savings are 200€ per month</Header.Subheader>
        </Header.Content>
    </Header>
)

export default PluggyFinalHeader
