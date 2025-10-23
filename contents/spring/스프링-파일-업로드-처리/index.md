---
title: "스프링 파일 업로드 처리"
description: "스프링 파일 업로드 처리"
date: 2019-01-02
update: 2019-01-02
tags:
  - web
  - spring
  - file
  - upload
  - springboot
  - 파일업로드
  - 스프링
---


## 1. 들어가며

이번 포스팅에서는 스프링에서 파일 업로드를 어떻게 구현할 수 있는지에 대해서 알아보도록 하겠습니다. 스프링에서는 단일 파일 업로드뿐만이 아니라 아래와 같은 여러 방법으로 파일 업로드 기능을 제공합니다.

- 단일 파일 업로드
- 다중 파일 업로드
- 파일 업로드 + 추가 정보 by @RequestParam 개별로
- 파일 업로드 + 추가 정보 by @ModelAttribute 한번에 클래스와 매핑

스프링은 MultipartResolver 인터페이스와 아래 2가지 구현체로 파일 업로드를 지원합니다.

- Servlet 3.0 Multipart Request 사용
    - 구현체 : StandardServletMultipartResolver
    - 파일(XML, JavaConfig)로 설정만 하면 된다.
- Apache Commons FileUpload API 사용
    - 구현체 : CommonsMultipartResolver
    - Servlet 3 환경에만 국한된 것은 아니지만, Servlet 3.x 컨테이너에서도 똑같이 작동한다 \* pom.xml에 라이브러리를 추가해야 한다

## 2. 개발 환경

- OS : Mac OS
- IDE: Intellij
- Java : JDK 1.8
    - JDK 9 이상 사용하면 javax_xml_bind/JAXBException 못찾는 이슈가 있다.
    - 해결 : [https://github.com/ohnosequences/sbt-s3-resolver/issues/58](https://github.com/ohnosequences/sbt-s3-resolver/issues/58)
- Source code : [github](https://github.com/kenshin579/tutorials-java/tree/master/spring-mvc-xml-fileupload)
- Software management tool : Maven

## 3. 파일 업로드을 위한 설정

파일 업로드를 위해 스프링에서 필요한 기본 설정에 대해서 알아봅시다. 언급했던 것처럼 스프링에서는 2가지 방법으로 파일 업로드를 설정할 수 있습니다. 본 포스팅에서는 첫 번째 StandardServletMultipartResolver 리졸뷰 위주로 설명을 하도록 하겠습니다. 두 번째인 CommonsMultipartResolver 리졸뷰를 사용해도 됩니다. 스프링 설정하는 경험이 있으면 어느 것을 사용하던 큰 어려움이 없을 것으로 생각됩니다. 필요한 내용은 참고 링크들을 참조해주시면 될 것 같아요.

- Servlet 3.0 Multipart Request (이 방법 위주로 설명)
    - standardServletMultipartResolver
- Apache Commons FileUpload API
    - CommonsMultipartResolver

### 3.1 스프링 및 파일 업로드 제한 설정

#### 3.1.1 StandardServletMultipartResolver 사용시 설정

Bean XML 정의 파일 설정
**1. StandardServletMultipartResolver 빈을 스프링에 등록**

```xml
파일 : spring-mvc-xml-fileupload_src_main_webapp_WEB-INF/spring-mvc-config.xml
<bean id="multipartResolver" class="org.springframework.web.multipart.support.StandardServletMultipartResolver" />
```

**2. 서블릿 설정에서 multipart-config을 선언**

```xml
파일 : spring-mvc-xml-fileupload_src_main_webapp_WEB-INF/web.xml

<servlet>
    <servlet-name>hello-dispatcher</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    <init-param>
        <param-name>contextConfigLocation</param-name>
        <param-value>_WEB-INF_spring-mvc-config.xml</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
    <multipart-config>
        <max-file-size>209715200</max-file-size>
        <max-request-size>209715200</max-request-size>
        <file-size-threshold>0</file-size-threshold>
    </multipart-config>
</servlet>
```

Multipart-config에서 여러 옵션을 설정하여 파일 업로드를 제한할 수 있습니다.

- **location** - 파일 업로드 시 임시로 저장하는 절대 경로이다
    - 디폴트 값 : "
- **maxFileSize** - 파일당 최대 파일 크기이다
    - 디폴트 값 : 제한없음
- **maxRequestSize** - 파일 한 개의 용량이 아니라 multipart/form-data 요청당 최대 파일 크기이다 (여러 파일 업로드 시 총 크기로 보면 된다) \* 디폴트 값: 제한없음
- **fileSizeThreshold** - 업로드하는 파일이 임시로 파일로 저장되지 않고 메모리에서 바로 스트림으로 전달되는 크기의 한계를 나타낸다
    - 디폴트 값: 0
    - ex. 1024 \* 1024 = 1MB 설정하면 파일이 1MB이상인 경우만에만 임시 파일로 저장된다

**JavaConfig 설정**

**1. StandardServletMultipartResolver 빈을 스프링에 등록**



```java
파일 : spring-mvc-javaconfig-fileupload-form/src/main/java/com/boraji/tutorial/spring/config/WebConfig.java
  
@Configuration
@EnableWebMvc
@ComponentScan(basePackages = { "com.boraji.tutorial.spring.controller" })
public class WebConfig extends WebMvcConfigurerAdapter {
    …(생략)...

    @Bean
    public MultipartResolver multipartResolver() {
        StandardServletMultipartResolver multipartResolver = new StandardServletMultipartResolver();
        return multipartResolver;
    }
}
```

**2. Multipart-config 설정을** **MultipartConfigElement 객체로 등록**



```java
파일 : spring-mvc-javaconfig-fileupload-form/src/main/java/com/boraji/tutorial/spring/config/MyWebAppInitializer.java
  
public class MyWebAppInitializer extends AbstractAnnotationConfigDispatcherServletInitializer {
    private static int MAX_FILE_ZIZE = 10 * 1024 * 1024;
    …(생략)...
    @Override
    protected void customizeRegistration(Dynamic registration) {
        MultipartConfigElement multipartConfig = new MultipartConfigElement("tmp_upload", MAX_FILE_ZIZE, MAX_FILE_ZIZE, 0);
        registration.setMultipartConfig(multipartConfig);
    }
}
```

**2.1 (다른 방법) @MultipartConfig 어노테이션으로 파일 업로드 제한 설정**
커스텀 서블릿을 생성하고 @MultipartConfig 어노테이션으로 multipart-config을 설정할 수 있습니다. 이 설정은 자세히 다루지 않겠습니다. 추가 설명은 [@MultipartConfig❲Servlet 3.x❳ 블로그](http://blog.naver.com/PostView.nhn?blogId=junsu60&logNo=220439479589) 를 참고해주세요.

```java
@MultipartConfig(location=/tmp,
fileSizeThreshold=0,
maxFileSize=5242880, //5 MB
maxRequestSize=20971520) //20 MB
public class FileUploadServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    //handle file upload
}
```

#### 3.1.2 CommonsMultipartResolver 사용시 설정

StandardServletMultipartResolver와 다르게 CommonsMultipartResolver 리졸뷰 사용 시 추가로 pom.xml 파일에 commons-fileupload 라이브러리를 추가해야 합니다.

**Dependency 추가**

```xml
<dependency>
    <groupId>commons-fileupload</groupId>
    <artifactId>commons-fileupload</artifactId>
    <version>1.3.3</version>
</dependency>
```

스프링 설정은 Bean 정의 파일이나 JavaConfig으로 설정 가능합니다.

**Bean XML 정의 파일 설정**

스프링 설정에 CommonsMultipartResolver 빈을 등록합니다.

```xml
<bean id="multipartResolver" class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
<property name="maxUploadSize" value="10485760"/>
<property name=“maxUploadSizePerFile" value="10485760”/>
<property name="maxInMemorySize" value=“0"/>
</bean>
```

**JavaConfig 설정**



```java
파일 : spring-mvc-javaconfig-fileupload-ajax/src/main/java/com/boraji/tutorial/spring/config/WebConfig.java
  
@Configuration
@EnableWebMvc
@ComponentScan(basePackages = { "com.boraji.tutorial.spring.controller" })
public class WebConfig extends WebMvcConfigurerAdapter {
    private final int MAX*SIZE = 10 * 1024 \- 1024;
    …(생략)...
    @Bean
    public MultipartResolver multipartResolver() {
        CommonsMultipartResolver multipartResolver = new CommonsMultipartResolver();
        multipartResolver.setMaxUploadSize(MAX_SIZE); 10MB
        multipartResolver.setMaxUploadSizePerFile(MAX_SIZE); 10MB
        multipartResolver.setMaxInMemorySize(0);
        return multipartResolver;
    }
}
```

## 4. 파일 업로드 예제들

지금까지는 스프링 관련 설정을 다루었습니다. 이제 뷰와 컨트롤러 단에서 어떻게 파일을 업로드할 수 있는지 알아보겠습니다. 파일을 업로드하는 방법에는 여러 가지가 있습니다. 예제를 통해서 서로 다른 점도 확인하겠습니다.

### 4.1 단일 파일 업로드

단일 파일을 업로드하는 예제입니다. 뷰는 HTML의 input 태그 file 속성으로 작성하여 form 방식으로 파일 업로드를 할 수 있습니다. form 태그의 enctype 속성은 multipart/form-data로 세팅하여 브라우져가 파일 업로드 방식으로 동작하도록 설정합니다.

**enctype 속성 값 목록**

| 값                                | 설명                                               |
| --------------------------------- | -------------------------------------------------- |
| multipart/form-data               | 파일 업로드시 사용 (인코딩 하지 않음)              |
| application_x-www-form_urlencoded | 디폴트값으로 모든 문자를 인코딩                    |
| text/plain                        | 공백은 + 기호로 변환함. 특수문자는 인코딩하지 안함 |

```html
<h3>단일 파일 업로드</h3>
<form action="singleFileUpload" method="post" **enctype**="multipart/form-data">
  <table>
    <tr>
      <td>Select File</td>
      <td><input type="**file**" name="**mediaFile**" /></td>
      <td>
        <button type="submit">Upload</button>
      </td>
    </tr>
  </table>
</form>
```

**브라우져에서의 뷰 화면**

![](/media/spring/스프링-파일-업로드-처리/image_8.png)

컨트롤러에서 업로드한 파일은 MultipartFile 변수를 사용하여 전달받습니다. MultipartFile 클래스는 파일에 대한 정보(파일 이름, 크기등)와 파일 관련 메서드(ex. 파일 저장)를 제공합니다. 대표적으로 사용하는 메서드는 다음과 같고 더 자세한 사항은 API를 참고해주세요.

- transferTo() : 파일을 저장한다
- getOriginalFilename() : 파일 이름을 String 값으로 반환한다
- getSize() : 파일 크기를 반환한다
- getInputStream() : 파일에 대한 입력 스트림을 얻어온다

```java
@PostMapping("/singleFileUpload")
public String singleFileUpload(@RequestParam("mediaFile") **MultipartFile** file, Model model)
throws IOException {

    // Save mediaFile on system
    if (!file.getOriginalFilename().isEmpty()) {
        file.transferTo (new File(DOWNLOAD_PATH + "/" + SINGLE_FILE_UPLOAD_PATH, file.getOriginalFilename()));
        model.addAttribute("msg", "File uploaded successfully.");
    } else {
        model.addAttribute("msg", "Please select a valid mediaFile..");
    }
    return "fileUploadForm";
}
```

Request parameter로 넘겨주는 파일 이름이 mediaFile로 넘겨줘서 @RequestRaram(“mediaFile”) 어노테이션으로 지정하였습니다. 그리고 파일이 빈파일이 아니면 정해진 다운로드 경로에 저장하고 결과 메시지는 fileUploadForm 뷰에 Model 클래스를 통해서 전달합니다.

> 번외 Tips
> Rest API 구현을 할 때 데이터 형식을 JSON으로 많이 사용해서 클라이언트와 서버 간에 주고받습니다. JSON 타입으로 주고받을때 기본적으로 encoding을 해서 보냅니다. 보내는 데이터가 적은 양이면 문제가 되지 않지만, 대용량의 JSON인 경우에는 성능에 큰 영향을 주게 됩니다. 이런 경우에 JSON 데이터를 stream으로 보내고 컨트롤러에서 MultipartFile로 받으면 스트림형식으로그냥 받기 때문에 성능이 많이 좋아집니다. 프로젝트 진행 시고려해볼 만한 부분입니다.

### 4.2 다중 파일 업로드

여러 파일을 업로드하는 방식은 단일 파일 업로드 예제와 매우 유사합니다. 차이점은 뷰에서 multiple 속성을 추가하여야사용자가 여러 파일을 선택할 수 있도록 해야 합니다.

```html
<h3>다중 파일 업로드</h3>
<form action="multipleFileUpload" method="post" enctype="multipart/form-data">
  <table>
    <tr>
      <td>Select Files</td>
      <td><input type="file" name="mediaFile" **multiple="multiple" ** /></td>
      <td>
        <button type="submit">Upload</button>
      </td>
    </tr>
  </table>
</form>
```

**브라우져에서의 뷰 화면**

![](/media/spring/스프링-파일-업로드-처리/image_1.png)

컨트롤러에서는 MultipartFile 변수를 배열로 선언하여 여러 파일을 받을 수 있도록 합니다. 배열을 loop으로 돌면서 각 파일을 정해진 경로에 저장합니다. MultipartFile 클래스에서 제공하는 transferTo 메서드로 저장할 수도 있지만, 직접 OutpuStream 클래스로 파일을 저장할 수도 있습니다.

```java
@PostMapping("/multipleFileUpload")
public String multipleFileUpload(@RequestParam("mediaFile") **MultipartFile[]** files,
Model model) throws IOException {

    Save mediaFile on system
    for (MultipartFile file : files) {
        if (!file.getOriginalFilename().isEmpty()) {
            BufferedOutputStream outputStream = new BufferedOutputStream(
            new FileOutputStream(
            new File(DOWNLOAD_PATH + "/" + MULTI_FILE_UPLOAD_PATH, file.getOriginalFilename())));

            outputStream.write(file.getBytes());
            outputStream.flush();
            outputStream.close();
        } else {
            model.addAttribute("msg", "Please select at least one mediaFile..");
            return "fileUploadForm";
        }
    }
    model.addAttribute("msg", "Multiple files uploaded successfully.");
    return "fileUploadForm";
}
```

### 4.3 파일 업로드 + 추가 정보 by @RequestParam

이번 예제는 파일과 다른 입력 정보를 같이 보내는 예제입니다. 추가 입력을 받을 수 있도록 form을 수정합니다.

```html
<h3>파일 업로드 + 추가 정보 by @RequestParam</h3>
<form
  action="singleFileUploadWithAdditionalData"
  method="post"
  enctype="multipart/form-data"
>
  Creator:<br />
  <input type="text" **name="creator" ** />
  <br />
  CallbackUrl:<br />
  <input type="text" **name="callbackUrl”** >
  <br />
  <input type="file" **name="mediaFile" ** />
  <br /><br />
  <button type="submit">Upload</button>
</form>
```

**브라우져에서의 뷰 화면**

![](/media/spring/스프링-파일-업로드-처리/image_7.png)

컨트롤러에서는 각 변수에 @RequestParam 어노테이션을 선언하여 입력 데이터를 개별로 받을 수 있게 합니다.

```java
@PostMapping("/singleFileUploadWithAdditionalData")
public String singleFileUploadWith(@RequestParam("mediaFile") MultipartFile **file**,
@RequestParam final String **creator**, @RequestParam final String **callbackUrl**, Model model) throws IOException {

  log.info("creator : {}", creator);
  log.info("callbackUrl : {}", callbackUrl);

  // Save mediaFile on system
  if (!file.getOriginalFilename().isEmpty()) {
    file.transferTo(new File(DOWNLOAD_PATH + "/" + SINGLE_FILE_UPLOAD_AND_EXTRA_DATA1_PATH, file.getOriginalFilename()));
    model.addAttribute("msg", "File uploaded successfully.");
  } else {
    model.addAttribute("msg", "Please select a valid mediaFile..");
  }
  return "fileUploadForm";
}
```

### 4.4 파일 업로드 + 추가 정보 by @ModelAttribute

4.3 예제에서는 입력 데이터를 개별 변수에 저장하는 방식이었습니다. 하지만, 입력하는 데이터가 많을 때는 메서드인자가 많이 늘어나는 단점이 있습니다. @ModelAttribute어노테이션을 이용하면 입력한 데이터를 클래스로 한 번에 매핑 할 수 있습니다.

클래스 매핑을 위해 Form에서 입력하는 데이터 이름과 같은 변수를 포함하는 클래스를 아래와 같이 생성합니다.

```java
@Data
public class MediaVO {
  private String creator;
  private String callbackUrl;
  private MultipartFile mediaFile;
}
```

사용자 입력 데이터를 받을 클래스 MediaVO를 인자로 선언합니다.

```java
@RequestMapping(value = "/uploadFileModelAttribute", method = RequestMethod.POST)
public String singleFileUploadWith( **@ModelAttribute MediaVO mediaVO**, Model model) throws IOException {
  MultipartFile file = mediaVO.getMediaFile();

  log.info("mediaVO: {}", mediaVO);

  // Save mediaFile on system
  if (!file.getOriginalFilename().isEmpty()) {
    file.transferTo(new File(DOWNLOAD_PATH + "/" + SINGLE_FILE_UPLOAD_AND_EXTRA_DATA2_PATH, file.getOriginalFilename()));

  model.addAttribute("msg", "File uploaded successfully.");
  } else {
    model.addAttribute("msg", "Please select a valid mediaFile..");
  }
  return "fileUploadForm";
}
```

업로드 파일과 입력 데이터는 MediaVO에 포함되어 있어서 원하는 데이터를 getter로 가져와 로직에서 사용합니다.

지금까지 스프링을 이용해서 파일 업로드를 알아보았습니다. 다음 시간에는 스프링 컨트롤러 예외처리에 대해서 알아보겠습니다.

## 5. 참고

- File Upload with Spring
    - [https://www.baeldung.com/spring-file-upload](https://www.baeldung.com/spring-file-upload)
    - [http://ktko.tistory.com/entry/Spring-단일파일-다중파일-업로드하기](http://ktko.tistory.com/entry/Spring-%EB%8B%A8%EC%9D%BC%ED%8C%8C%EC%9D%BC-%EB%8B%A4%EC%A4%91%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C%ED%95%98%EA%B8%B0)
    - [http://websystique.com/springmvc/spring-mvc-4-file-upload-example-using-commons-fileupload/](http://websystique.com/springmvc/spring-mvc-4-file-upload-example-using-commons-fileupload/)
    - [http://websystique.com/springmvc/spring-mvc-4-file-upload-example-using-multipartconfigelement/](http://websystique.com/springmvc/spring-mvc-4-file-upload-example-using-multipartconfigelement/)
    - [https://blog.hanumoka.net/2018/09/06/spring-20180906-spring-file-upload/](https://blog.hanumoka.net/2018/09/06/spring-20180906-spring-file-upload/)
    - [http://cornswrold.tistory.com/74](http://cornswrold.tistory.com/74)
- @Multipartconfig
    - [http://programmertech.com/program/jee/java-file-upload-using-servlet3-and-file-download](http://programmertech.com/program/jee/java-file-upload-using-servlet3-and-file-download)
    - [https://javaee.github.io/tutorial/servlets011.html#BABFGCHB](https://javaee.github.io/tutorial/servlets011.html#BABFGCHB)
    - [http://blog.naver.com/PostView.nhn?blogId=junsu60&logNo=220439479589](http://blog.naver.com/PostView.nhn?blogId=junsu60&logNo=220439479589)
      _ [https://www.ibm.com/developerworks/community/blogs/9e635b49-09e9-4c23-8999-a4d461aeace2/entry/160?lang=en](https://www.ibm.com/developerworks/community/blogs/9e635b49-09e9-4c23-8999-a4d461aeace2/entry/160?lang=en)
- File Upload Progress Bar
    - [https://www.boraji.com/spring-4-mvc-jquery-ajax-file-upload-example-with-progress-bar](https://www.boraji.com/spring-4-mvc-jquery-ajax-file-upload-example-with-progress-bar)

