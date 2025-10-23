---
title: "Jaeger에 대한 소개"
description: "Jaeger에 대한 소개"
date: 2022-07-22
update: 2022-07-22
tags:
  - jaeger
  - telemetry
  - trace
  - monitor
  - msa
  - 분산추적
---

> 본 내용은 저희 Platform Engineering 팀내 CNCF 스터디를 위해 준비한 자료입니다. 저희가 하는 로봇 플랫폼 개발에 관심이 있는 분들은 아래 링크를 참고해주시고 도전적이고 열정적으로 같이 일하실 분은 많이 지원해주세요.
>
> - 네이버는 왜 제2사옥 1784를 지었을 까요?  https://www.youtube.com/watch?v=WG7JHLfClEo
> - 네이버 랩스 - https://www.naverlabs.com/

## 1.What is Jaeger?

### 1.1 Distributed Tracing?

마이크로 서비스와 같이 여러 컴포넌트로 분리된 분산 환경에서 로그로만 문제점을 파악하기는 쉽지 않다. 특히 마이크로 서비스의 대부분의 문제점은 여러 개의 다른 서비스 간의 통신 이슈(ex. wrong request, latency)인 경우가 많고 이런 환경에서 문제의 근본 원인을 빠르게 찾기는 쉽지 않다.

> Distributed Tracing (분석 추적)?
>
> - *‘call-stacks’ for distributed services.*
> - 분산 추적은 분산 시스템을 통해 흐르는 서비스 요청을 추적하고 관찰하는 것이다



![Distributed Tracing](distributed-tracing.png)


#### Distributed Tracing의 기본 아이디어

- 실행되는 컨포넌트마다 실행 시간과 추가 정보 수립
- 수집한 정보를 DB에 저장
- DB에 저장된 정보를 가지고 컨포넌트간의 연관관계를 재조합해서 Visualization 도구로 표시함

### 1.2 Jaeger?

Jaeger는 2015년 Uber가 만든 오픈 소스 Distributed Tracing System이다. Jaeger는 처음부터 OpenTracing 표준을 지원하도록 설계되었다. (표준화는 업체 중립적인 Tracing 데이터 모델링)



#### 1.2.1 Tracing Specification

- OpenTracing
    - CNCF project로 현재 deprecated 됨
    - OpenTracing Observability 백엔드 서버에 telemetry data (metrics, log, traces)를 전송하기 위해 vendor-netural 표준화된 API를 제공한다
    - 개발자는 OpenTracing API 표준화에 맞게 직접 라이브러리를 구현해야 한다
- OpenCensus
    - Google의 오픈 소스 커뮤니티 프로젝트
    - OpenCensus는 개발자가 자기 어플리케이션을 계측해서 백엔드로 telemetry data를 전송할 수 있도록 언어별 라이브러리 세트를 제공한다
- OpenTelemetry (OTel)
    - OpenTracing + OpenCensus 프로젝트가 하나로 merge됨
    - 2019년에 CNCF Incubation 프로젝트로 채택됨
    - 프로젝트 성숙도는 아직 Incubating level에 있음
    - Trace, metric, log 와 같은 원격 측정 데이터를 기기, 생성, 수집 및 내보내기 위한 공급 업체-중립 오픈 소스 관찰 프레임워크이다


#### Reference

- https://opencensus.io/
- https://opentracing.io/
- https://opentelemetry.io/docs/concepts/what-is-opentelemetry/



#### 1.2.2 History

- Dapper (Google) : Foundation of all tracers
    - Tracing 관련 주제는 1990년도 부터 나오기 시작
    - Google의 논문 [Dapper, a Large-Scale Distributed Systems Tracing Infrastructure](https://research.google/pubs/pub36356/), 2010 발표이후 주류로 자리 매김하게 됨
- [Zipkin](https://zipkin.io/) and OpenZipkin (Twitter)
    - 최초의 Open Source Tracing system
    - 2012년 Twitter에서 공개
- [Jaeger](https://www.jaegertracing.io/) (Uber)
    - 2015년 Uber에 의해서 만들어졌고 2017년에 오픈소스로 공개함
    - 2017년 9월에 CNCF Incubation 프로젝트로 채택됨
    - 2019년에 Jaeger는 Graduated 프로젝트로 승인됨
- StackDriver Trace -> [Cloud Trace](https://cloud.google.com/trace?hl=ko) (Google)
- [X-Ray](https://aws.amazon.com/ko/xray/) (AWS)



![Trace History](image-20220718232202127.png)



#### 1.2.3 Feature

- High Scalability 고려해서 설계됨
    - collector의 auto-scaling을 지원함

- OpenTracing과 OpenTelemetry을 지원함
    - 처음부터 OpenTracing 표준을 지원하도록 설계됨
    - v1.35 이후, Jaeger 백엔드는 OpenTelemetry SDK로부터 trace data를 수신할 수 있음
- Modern Web UI (React 개발)
- Cloud Native Deployment
    - Jaeger 백엔드 도커 이미지로 배포 가능하도록 지원
- Zipkin과의 역호환성도 지원
- Topology Graphs
    - Jaeger UI에서 2가지 타입의 서비스 그래프가 있음
        - System Archiecture, Deep Dependency Graph
- Sampling
    - Adaptive sampling 지원

- 다중 스토리지 백엔드 지원
    - Memory (기본), Cassandra, Elasticsearch
- Post-collection data processing pipeline (coming soon)
- Service Performance Monitoring (SPM)

#### 1.2.4 Tracing 용어와 친해지기

##### Span
- 분산 추척에서는 가장 기본이 되는 블록 단위로 분산 시스템에서 실행되는 작업 단위를 나타낸다
    - ex. HTTP request, call to DB
- Span은 다음과 같은 정보가 있다
    - Span Name (operation Name)
    - Start/Finish Timestamp
    - Span Tags, Logs (key:value)
    - Span Context : 서비스에서 다른 서비스로 전달이 될 때 Trace에서 각 Span를 구별할 수 있는 추척 정보 (ex. Span id, Trace id)

##### Trace
- Trace는 시스템 전반에서 데이터/실행 경로를 나타낸다
- 1개 이상의 Span으로 이루어져 있고 여러 개의 Span이 모여서 하나의 Trace를 완성하게 된다

##### Instrumentation
- Application(ex. DB)에 따라 여러 library를 오픈소스로 제공
- Instrumentation library를 통해서 Span으로 생성함


![OpenTracing](OpenTracing1.png)

## 2. Jaeger Tracing Architecture

Jaeger는 추적 데이터를 수집, 저장, 표시해주기 위해 여러 구성 요소로 이루어져 있다.

- ~~Jaeger client~~ / OpenTelemetry Distro (SDK)
    - Jaeger Client는 분산 추적을 위한 OpenTracing API의 언어별 구현체
    - 지금은 OpenTelemetry SDK를 사용
- Jaeger Agent
    - 사용자 데이터그램 프로토콜 (UDP)을 통해 전송된 스팬을 수신하는 네트워크 데몬으로, 계측된 애플리케이션과 동일한 호스트에 배치됨
- Jaeger Collector
    - 프로세싱을 위해 Span을 수신하여 대기열에 배치
- Storage Backends
    - Trace를 저장할 수 있는 데이터 저장소
- Jaeger Query
    - Query 서비스는 저장소에서 데이터를 가져와 UI에 필요한 API를 제공한다
- Jaeger UI

### 2.1 Jaeger Architecture

![Architecture](architecture-v1.png)


#### 2.1.1 Jaeger Architecture w/ Kafka - Intermediate Buffer

- Ingester
    - Collector와 DB 간의 Intermediate buffer로 Kafka를 사용할 수 있다
    - Ingester는 Kafka에서 데이터를 읽고 다른 스토리지에 쓰는 역할을 한다


![Architecture](architecture-v2.png)



#### 2.1.2 Instrumentation

Span을 생성하는 방법은 2가지가 있다

- Auto Instrumentation
    - 이미 OpenTelemetry 커뮤니티에서 여러 어플리케이션(ex. Redis, MongoD)를 위한 library를 만들어서 registry 사이트에서 제공하고 있음
    - https://opentelemetry.io/registry/
- Manual Instrumentation
    - 오픈소스로 제공되지 않는 경우에는 어플리케이션에 직접 수동으로 Span을 생성해서 개발을 해야 함

#### 2.1.3 Sampling

모든 tracing 정보를 raw하게 다 저장하지 않고 백엔드에 저장되는 trace 수를 줄이기 위해 sampling을 사용한다.

- Head-based sampling
    - jaeger-client 맨 앞단에서 sampling rule이 결정되는 방식
- Tail-based sampling
    - collector 단에서 sampling을 하는 거라 tail-based라고 칭함
    - Adaptive sampling (v1.27이후) 도 지원해서 시스템으로 들어오는 트랙픽과 trace의 수을 가지고 sampling이 자동으로 조절이 가능함

## 3.Running Jaeger Docker on Local Machine

### 3.1 Hot R.O.D - Rides on Demand Sample 실행하기

HotROD는 Jaeger github에서 제공하는 "ride on demand" 데모 어플리케이션이고 OpenTracing API를 사용한 버전이다. Standalone으로 실행되고 여러 마이크로 서비스가 별도 port로 실행하여 간단한 MSA 형식으로 동작하게 되어 있다. 이 예제에서는 별도 Instrumentation을 사용하지 않고 직접 Span을 생성하는 방식으로 되어 있다.

#### Jaeger 실행하기

빠른 실행을 위해 Jaeger의 모든 컨포넌트가 포함되어 있는 올인원 도커 이미지로 실행한다.

> 운영 환경에서는 올인원 도커 이미지로 실행하고 만약 컨테이너가 죽게 되면 단일 장애 원천 (single source of failure)이 되고 결국 운영 서비스에 큰 영향을 주게 된다. 운영 환경의 경우에 개별 컨포넌트로 배포하는 걸 추천한다.

```bash
$ docker run -d -p6831:6831/udp -p16686:16686 jaegertracing/all-in-one:latest
```

컨테이너가 실행된 후 Jaeger UI에 접속하려면 이 주소로 http://localhost:16686 접속한다.

![Jaeger Web](image-20220717103342529.png)

#### Hot R.O.D 샘플 프로그램 실행하기

HotROD 샘플 코드는 golang으로 작성되어 있어서 미리 go toolchain 설치가 필요한다.

Github에서 소스를 다운로드 받아 실행한다.

```bash
$ git clone https://github.com/jaegertracing/jaeger
$ cd jaeger/examples/hotrod
$ go run ./main.go all
```

all 옵션을 주면  HotROD의 모든 서비스를 한번에 실행할 수 있고 구동 후에는 http://127.0.0.1:8080로 접속한다.

![Hot R.O.D Sample WebApp](image-20220717103943745.png)

### 3.2 Play around with Jaeger

HotROD에서 버튼을 클릭하여 라이드 요청하면, Jaeger에서 API에 대한 trace를 확인할 수 있다.

#### System Architecture > DAG

- 이 화면에서는 컨포넌트를 전체 구성 요소를 한눈에 확인할 수 있다

![System Architecture DAG](image-20220717104614304.png)

에러가 발생한 경우 어느 서비스 구간에서 발생했는지 로그로 찾기는 쉽지 않다.

![Console Log](image-20220717104917246.png)



#### Jaeger Tracing의 장점

- 어느 구간에서 실패가 발생했는지 쉽게 찾을 수 있다
- 여러 컨포넌트에서 어느 구간에서 bottleneck이 있는지도 쉽게 확인할 수 있다

![Jaeger Trace](image-20220717115919867.png)

![Jaeger Trace](image-20220717115937277.png)

## 3.2 OpenTelemetry를 사용한 샘플 코드 - MongoDB, Gin instrumentation 사용

HotROD 어플리케이션은 OpenTracing SDK를 사용 + Manual Instrumentation 방식으로 구현된 버전이다. 최신 OpenTelemetry 표준화인 SDK로 구현한 버전도 같이 확인해보자.

웹 어플리케이션 개발시 다양한 DB나 웹 프레임워크를 사용하게 되는데, 이것에 대한 instrumentation도 오픈소스로 개발되어 있어 쉽게 어플리케이션에 적용이 가능하다.

Aspecto 블로그에 예제로 작성된 Todo 웹 서비스를 보면, MongoDB와 Gin 웹 프레입워크를 사용한다. Span을 직접 생성하지 않고 DB나 프레임워크에 잘 설정만 해주면 된다.

- MongoDB에 적용

```go
func connectMongo() {
  opts := options.Client()
  //Mongo OpenTelemetry instrumentation
  opts.Monitor = otelmongo.NewMonitor() // 이렇게 하면 끝
  opts.ApplyURI("mongodb://localhost:27017")
  client, _ = mongo.Connect(context.Background(), opts)
...생략...
}
```

- Gin 웹 프레임워크에 적용

```go
r := gin.Default()
  //Gin OpenTelemetry instrumentation
r.Use(otelgin.Middleware("todo-service")) //이렇게 하면 끝
```



### 3.3 Reference

- https://medium.com/opentracing/take-opentracing-for-a-hotrod-ride-f6e3141f7941
- https://www.aspecto.io/blog/opentelemetry-go-getting-started/

## 4.Conclusion

> *Frank의 내면의 소리: 문제 있을 때 이제 Kibana 로그는 그만 보고 싶다. 한번에 빠르게 파악하기 위해서는 팀내에 APM/distributed trace system 도입이 시급하지 않을 까*

Jaeger를 도입하는 건 결국 운영 관리 비용이 들기 때문에 되도록이면 사내 APM/Distributed trace system을 사용하는게 베스트일 것이다. 우리 사내에서는 이미 Pinpoint를 제공하고 있어서 이걸로 사용하는게 좋을 듯하다.

> [1784](https://www.navercorp.com/naver/1784) 사옥에서 이미 서비스 운용 중인데, 인프라적으로나 개발적으로 할일도 많고 일손이 많이 부족합니다. 로봇 플랫폼 개발에 관심있는 분들은 많이 지원 부탁드려요.

이번에 처음 알게 되었지만, Pinpoint도 CNCF의 프로젝트로 포함되어 있었다.

- https://landscape.cncf.io/?selected=pinpoint

## 5.Terminology

- Observability (관찰 가능성?)
    - Observability란 개념을 처음 도입한 건 엔지니어 [Rudolf E. Kálmán](https://en.wikipedia.org/wiki/Rudolf_E._K%C3%A1lm%C3%A1n) 임
    - **"오직 시스템의 외부 출력만을 이용해서 시스템의 현재 상태를 이해할 수 있는 능력"**
    - Observability의 3대 요소 : logs, metrics, traces
- Tag
    - 태그는Trace data를 query, filter하기 위해 사용자가 정의하는 Key:value 값이다
    - ex. http.method=GET
    - http.status.code=200
- Telemetry data
    - 원격 측정 데이터로 metrics, log, traces 3가지가 있다


## 6.Reference

- https://www.aspecto.io/blog/jaeger-tracing-the-ultimate-guide/
- https://www.slideshare.net/OracleDeveloperkr/opentracing-jaeger
- https://www.aspecto.io/blog/logging-vs-tracing-why-logs-arent-enough-to-debug-your-microservices/
- https://www.jaegertracing.io/docs/1.36/
- https://www.redhat.com/ko/topics/microservices/what-is-jaeger
- https://twofootdog.tistory.com/67
- https://opentracing.io/docs/
- https://access.redhat.com/documentation/ko-kr/openshift_container_platform/4.9/html/distributed_tracing/_jaeger-architecture
- https://litaro.tistory.com/entry/Jaeger-with-Go
- https://www.elastic.co/kr/blog/distributed-tracing-opentracing-and-elastic-apm
- https://speakerdeck.com/simonz130/distributed-tracing-and-monitoring-with-opentelemetry?slide=26
- https://docs.logz.io/user-guide/distributed-tracing/what-is-tracing
- https://opentelemetry.uptrace.dev/guide/distributed-tracing.html#what-is-tracing
