import React from "react"
import {Script} from "gatsby";

const Analytics = ({}) => {
    return (
        <div>
            <Script async src="https://www.googletagmanager.com/gtag/js?id=G-B0KLVK60W1"></Script>
            <Script>
                {`
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-B0KLVK60W1');
        `}
            </Script>
        </div>
    )
}

export default Analytics
