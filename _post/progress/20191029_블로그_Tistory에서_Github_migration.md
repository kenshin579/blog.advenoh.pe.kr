# 블로그 : Tistory에서 Github migration
* 들어가며
* 개발 환경
* 블로그 마이그레이션

* 참고

**코멘트**
- [ ] 기본 tistory 블로그를 어떻게 migration 할 것인가/?

- [ ] github에 가장 쉽게 편하게 관리할 수 있는 프레임워크?가 좋을까?

- [ ] github 페이지에 도메인 이름 연결하기

- [ ] jekyll 대신 사용할 수 있는 건?
* hugo
* hexo
* gatsby <— 이걸로 선택함

advenoh.blog.com
advenoh…..io

[9. 도전기 IT 블로그 재시작](evernote:///view/838797/s7/332fde73-909f-438b-9046-195bcb86cab6/332fde73-909f-438b-9046-195bcb86cab6/)
[Jekyll Blog](evernote:///view/838797/s7/c93ead75-ce73-475a-add5-2e5f8244bd2e/c93ead75-ce73-475a-add5-2e5f8244bd2e/)

[https://docs.netlify.com/domains-https/custom-domains/](https://docs.netlify.com/domains-https/custom-domains/)
[https://serverless-stack.com/chapters/ko/custom-domain-in-netlify.html](https://serverless-stack.com/chapters/ko/custom-domain-in-netlify.html)
[https://gist.github.com/hhsnopek/356791d3b70a853cb5ef54ff8c3bc18e](https://gist.github.com/hhsnopek/356791d3b70a853cb5ef54ff8c3bc18e)
[https://heropy.blog/2018/01/10/netlify/](https://heropy.blog/2018/01/10/netlify/)
[https://levelup.gitconnected.com/how-to-host-domain-to-netlify-site-for-free-step-by-step-guide-45d0c2102db3](https://levelup.gitconnected.com/how-to-host-domain-to-netlify-site-for-free-step-by-step-guide-45d0c2102db3)
[https://velog.io/@godori/netlify-branch-sub-domain](https://velog.io/@godori/netlify-branch-sub-domain)

1. 들어가며

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : github
* Software management tool : Maven

3. 사용법

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Tistory%EC%97%90%EC%84%9C%20Github%20migration/image_3.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Tistory%EC%97%90%EC%84%9C%20Github%20migration/image_1.png)

![](%EB%B8%94%EB%A1%9C%EA%B7%B8%20%20Tistory%EC%97%90%EC%84%9C%20Github%20migration/image_2.png)

-github pages에 upload
>#
"scripts": {
"deploy": "gatsby build && gh-pages -d public -b master -r https://github.com/funnystyle/funnystyle.github.io"
},

4. 참고

* Github Page
	* [https://github.com/Integerous/Integerous.github.io](https://github.com/Integerous/Integerous.github.io)
* Dev IT Blog 모음
	* [https://github.com/sarojaba/awesome-devblog](https://github.com/sarojaba/awesome-devblog)
* Hexo vs. Hugo vs Jekyll
	* [http://open-but-closed.com/hexo-as-a-platform-for-blogging/](http://open-but-closed.com/hexo-as-a-platform-for-blogging/)
	* [https://stackshare.io/stackups/hexo-vs-hugo-vs-jekyll](https://stackshare.io/stackups/hexo-vs-hugo-vs-jekyll)
* Gatsby
	* [https://jbee.io/etc/intro-new-blog/](https://jbee.io/etc/intro-new-blog/)
	* [https://rinae.dev/posts/creating-new-blog-with-gatsby](https://rinae.dev/posts/creating-new-blog-with-gatsby)
	* [https://dennytek.com/blog/personal-site-with-gatsby-part-3](https://dennytek.com/blog/personal-site-with-gatsby-part-3)
	* [https://scotch.io/tutorials/zero-to-deploy-a-practical-guide-to-static-sites-with-gatsbyjs](https://scotch.io/tutorials/zero-to-deploy-a-practical-guide-to-static-sites-with-gatsbyjs)
	* [https://justinformentin.com/guide-to-building-a-gatsby-site](https://justinformentin.com/guide-to-building-a-gatsby-site)
* Gatsby와 Github 연동
	* [https://www.gatsbyjs.org/docs/how-gatsby-works-with-github-pages/](https://www.gatsbyjs.org/docs/how-gatsby-works-with-github-pages/)
	* [https://dev.to/flexdinesh/deploy-gatsby-sites-to-github-pages-eed](https://dev.to/flexdinesh/deploy-gatsby-sites-to-github-pages-eed)
	* [http://jarednielsen.com/deploy-gatsbyjs-github-pages-user/](http://jarednielsen.com/deploy-gatsbyjs-github-pages-user/)
* Gatsby Theme
	* [https://gatsby-starter-hero-blog.greglobinski.com](https://gatsby-starter-hero-blog.greglobinski.com/)
	* [https://www.gatsbyjs.org/starters/JaeYeopHan/gatsby-starter-bee/](https://www.gatsbyjs.org/starters/JaeYeopHan/gatsby-starter-bee/)
	* [https://www.gatsbyjs.org/starters/willjw3/gatsby-starter-developer-diary/](https://www.gatsbyjs.org/starters/willjw3/gatsby-starter-developer-diary/)
	* [http://demo.nagui.me/](http://demo.nagui.me/)
	* [https://delivan.dev](https://delivan.dev/)
* Netlify
	* [https://velog.io/@godori/netlify-branch-sub-domain](https://velog.io/@godori/netlify-branch-sub-domain)
	* [https://css-tricks.com/using-your-domain-with-a-netlify-hosted-site/](https://css-tricks.com/using-your-domain-with-a-netlify-hosted-site/)
	* [https://velog.io/@funnystyle/gatsby-로-blog-만들기-간략-정리](https://velog.io/@funnystyle/gatsby-%EB%A1%9C-blog-%EB%A7%8C%EB%93%A4%EA%B8%B0-%EA%B0%84%EB%9E%B5-%EC%A0%95%EB%A6%AC)
* DNS
	* [https://thomaskim.io/2017/06/13/using-custom-domain-to-github/](https://thomaskim.io/2017/06/13/using-custom-domain-to-github/)
* Evernote migration
	* [http://www.markwk.com/migrate-evernote-plaintext.html](http://www.markwk.com/migrate-evernote-plaintext.html)

#blog