import React from 'react';
import pic from './images/smile.png';
import { Segment, Image } from 'semantic-ui-react';

// const Picture = () =>
//     <div>
//         < img src={pic}
//             style={{
//                 width: '50%',
//                 height: '50%'
//             }} />
//     </div>

const Picture = () =>

    <Image src={pic} size='medium' centered />

export default Picture