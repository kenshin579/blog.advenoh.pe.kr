import React from "react"
import AdSense from 'react-adsense';

const Adsense = ({}) => {
    return (
        <AdSense.Google
            client="ca-pub-8868959494983515"
            slot="5560009326"
            style={{display: 'block'}}
            layout="in-article"
            format="fluid"
        />
    )
}

export default Adsense
