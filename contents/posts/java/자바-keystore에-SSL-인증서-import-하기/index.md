---
title: "자바 keystore에 SSL 인증서 import 하기"
description: "자바 keystore에 SSL 인증서 import 하기"
date: 2019-01-09
update: 2019-01-09
tags:
  - ssl
  - keystore
  - import
  - java
  - certificate
  - 인증서
  - 자바
---

## 1. 들어가며

회사에서 [Zencoder API](https://support.brightcove.com/zencoder) 을 사용하게 되어 자바에서 작업을 시작하려는데, 아래와 같이 SSLHandshakeException이 발생해서 뭔가 문제인지 구글링을 하게 되었습니다. 이미 아시는 분들도 많지만, 다시 한번 정리를 해봤습니다.

- Zencoder API 작업 요청 주소 \* [https://app.zencoder.com/api/v2/jobs](https://app.zencoder.com/api/v2/jobs)

**Exception 발생 화면**

![](image_13.png)

## 2. 개발 환경

실제 작성한 코드는 많지 않고 테스트를 쉽게 하려고 간단하게 유닛 테스트로 작성했습니다. github에 올린 코드를 참조해주세요.

- OS : Mac OS
- IDE: Intellij
- Java : JDK 1.8
- Source code : [github](https://github.com/kenshin579/tutorials-java-examples/tree/master/java-ssl-keystore-import-test)
- Software management tool : Maven

## 3. 해결책

이 문제를 해결하는 방법은 크게 2가지가 있습니다.

- 코딩상에서 직접 인증서 유효성 체크 하지 않기 (비추)
- 해당 인증서 자바 keystore에 저장하기 (추천 방식)

### 3.1 코드 상에서 직접 인증서 유효성 체크 하지 않기

자바 코드로 인증서 체크를 하지 않도록 HttpsConnection의 설정을 변경하는 방식입니다. 아래 코드에 대한 자세한 설명은 생략하도록 하겠습니다.

```java
@Test
public void test_disable_certificate_from_code() {
   disableCertificateCheck(); //#1

   Assertions.assertThatCode(this::connectHttps).doesNotThrowAnyException();
}

private void disableCertificateCheck() {
   // Create a trust manager that does not validate certificate chains
   TrustManager[] trustAllCerts = new TrustManager[] {
         new X509TrustManager() {
            public java.security.cert.X509Certificate[] getAcceptedIssuers() {
               return new X509Certificate[0];
            }

            public void checkClientTrusted(
                  java.security.cert.X509Certificate[] certs, String authType) {
            }

            public void checkServerTrusted(
                  java.security.cert.X509Certificate[] certs, String authType) {
            }
         }
   };

   // Install the all-trusting trust manager
   try {
      SSLContext sc = SSLContext.getInstance("SSL");
      sc.init(null, trustAllCerts, new java.security.SecureRandom());
      HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());
   } catch (GeneralSecurityException e) {
   }
}
```

### 3.2 해당 인증서 자바 keystore에 저장하기 (추천 방식)

자바 keystore에 인증서를 등록하는 방법에는 크게 2가지가 있습니다. 명령어 창에서 하던지 아니면 Portecle GUI 프로그램을 사용해도 상관없습니다.

#### 3.2.1 Portecle GUI 사용하기

자바 keystore에 인증서를 등록하기전에 유닛 테스트를 실행하면, SSLHandshakeException이 발생합니다.

```java
@Test
public void test_after_import_certificate() {
   Assertions.assertThatCode(this::connectHttps).doesNotThrowAnyException();
}
```

[Portecle](http://portecle.sourceforge.net/) 은 keystore를 관리해주는 자바로 짠 GUI 프로그램입니다. 자바로 짜여 있어서 플롯폼 상관없이 어디서든 실행할 수 있습니다.

**1. 다운로드 한후 압축 풀기**

아래 링크에서 프로그램을 다운로드한 후 압축을 원하는 폴더에 풀어줍니다.

[https://sourceforge.net/projects/portecle/files/latest/download](https://sourceforge.net/projects/portecle/files/latest/download)

**2. Portecle 실행**

인증서 등록 후 저장 시 root 권한 필요하므로 sudo로 프로그램을 실행합니다.

```bash
$ sudo java -jar portecle.jar
```

![](image_10.png)

**3. 접속 사이트에서 인증서를 다운로드합니다.**

메뉴에서 **Examine > Examine SSL/TSL Connection…** 을 클릭하고 접속하려는 사이트 주소를 입력 후 **OK 버튼** 을 클릭합니다.

![](image_5.png)

![](image_8.png)

클릭 후에 인증서를 볼 수 있습니다. 이 내용을 저장하려면 **PEM Encoding 버튼** 클릭 후 **Save 버튼** 을 눌려 저장합니다.

![](image_9.png)

![](B42B7B20-2C07-4BF6-8E43-65A2207B4521.png)

**4. 자바 keystore에 등록하기**

원하는 자바 버전의 **\$JAVA_HOME_lib_security/cacerts** 파일을 열어서 새로운 인증서를 추가하고 저장하면 끝납니다.

설치된 자바 홈 폴더를 확인하고 싶으면 **java_home 명령어** 로 확인할 수 있습니다.

```bash
$ /usr/libexec/java_home -V
```

메뉴에서 열기 버튼을 클릭해서 cacerts 파일을 찾아 오픈하면 암호를 입력하게 되어 있습니다. **디폴트 암호 값은 changeit** 입니다.

![](7258033D-D720-4B51-8FB0-AA198B5FBCB0.png)

![](image_2.png)

현재 등록된 인증서 목록입니다.

![](image_11.png)

새로운 인증서를 추가하기 위해 메뉴 임포트 버튼을 클릭하고 다운로드한 인증서를 선택합니다.

![](73801762-680A-4DC8-93D6-B67E6185E9BF.png)

파일 선택 이후 여러 질문에 **Yes 버튼** 을 클릭하면 새로운 인증서가 추가된 것을 목록에서 확인할 수 있습니다.

![](image_4.png)

다시 유닛 테스트를 실행하면 Exception 없이 잘 실행되는 것을 확인할 수 있습니다. 자 그면, 명령어 창에서 등록하는 방법을알아보겠습니다.

#### 3.2.2 명령어창에서 자바 keystore에 인증서 임포트하기

명령어 창에서도 인증서를 다운로드하고 등록할 수 있습니다.

**1. 인증서 다운로드하기**

```bash
$ openssl s_client -connect [app.zencoder.com:443](http://app.zencoder.com:443/) | tee appzencoder.certlog
$ openssl x509 -inform PEM -in appzencoder.certlog -text -out appzencoder.certdata
$ openssl x509 -inform PEM -text -in appzencoder.certdata
```

**2. 자바 keystore에 새로운 인증서 추가하기**

```bash
$ sudo keytool -importcert -file ./appzencoder.certdata -alias [app.zencoder.com](http://app.zencoder.com/) -keystore \$JAVA_HOME/jre_lib_security/cacerts -storepass changeit
```

입력이후 질문이 나오면 yes 를 입력하면 등록이 완료됩니다.

![](image_6.png)

## 4. 참고

- Java의 keystore에 SSL 인증서 import 하기
    - [https://www.lesstif.com/pages/viewpage.action?pageId=12451848](https://www.lesstif.com/pages/viewpage.action?pageId=12451848)
    - [https://stackoverflow.com/questions/2893819/accept-servers-self-signed-ssl-certificate-in-java-client](https://stackoverflow.com/questions/2893819/accept-servers-self-signed-ssl-certificate-in-java-client)
- Certificate 다운로드 방법
    - [https://www.lesstif.com/pages/viewpage.action?pageId=16744456](https://www.lesstif.com/pages/viewpage.action?pageId=16744456)
    - [https://stackoverflow.com/questions/33284588/error-when-connecting-to-url-pkix-path-building-failed](https://stackoverflow.com/questions/33284588/error-when-connecting-to-url-pkix-path-building-failed)

