import React from "react"
import AdSense from 'react-adsense';

const Adsense = ({}) => {
    return (
        <div>
            <script async
                    src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8868959494983515"
                    crossOrigin="anonymous"></script>
            <!-- BlogArticleBottomAd -->
            <ins className="adsbygoogle"
                 style="display:block"
                 data-ad-client="ca-pub-8868959494983515"
                 data-ad-slot="5560009326"
                 data-ad-format="auto"
                 data-full-width-responsive="true"></ins>
            <script>
                (adsbygoogle = window.adsbygoogle || []).push({});
            </script>
        </div>
    )
}

export default Adsense
