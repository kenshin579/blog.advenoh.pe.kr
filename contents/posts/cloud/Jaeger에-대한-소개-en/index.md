---
title: "Introducing Jaeger"
description: "Introducing Jaeger"
date: 2023-03-07
update: 2023-03-07
tags:
  - jaeger
  - trace
  - tracing
  - pinpoint
  - telemetry
---


## 1.What is Jaeger?

### 1.1 Distributed Tracing?

In a distributed environment such as Microservices, it is not easy to identify the problems right away just going through the logs. In particular, most problems in microservices are often communication issues between multiple services (e.g., incorrect requests, latency), and it's not easy to quickly find the root cause of the problem in this environment.

> What is the Distributed Tracing?
>
> - *‘call-stacks’ for distributed services.*
> - Distributed tracing is the process of tracing and observing service requests that flow through a distributed system.


![Distributed Tracing](distributed-tracing.png)


#### Basic Idea for Implementing Distributed Tracing

- Establish execution time and additional information for each executed component
- Store the collected information in DB
- Using the information stored in the DB, recombine the relationships between components and display them as a visualization tool.

### 1.2 Jaeger?

Jaeger is an open source Distributed Tracing System created by Uber in 2015. Jaeger was designed from the ground up to support the OpenTracing standard, which is a vendor-neutral tracing data modeling standard.

#### 1.2.1 Tracing Specification

- OpenTracing
    - Currently deprecated as a CNCF project
    - Provides a vendor-neutral standardized API for developers to send telemetry data (metrics, logs, traces) to observability backend servers
    - Developers must implement their own libraries to comply with the OpenTracing API standard
- OpenCensus
    - Google's open-source community project
    - OpenCensus provides a set of language-specific libraries for developers to instrument their applications and send telemetry data to the backend
- OpenTelemetry (OTel)
    - It is a merged two projects, OpenTracing and OpenCensus
    - Adopted as a CNCF Incubation project in 2019
    - Project maturity is still at the Incubating level
    - A vendor-neutral open-source observability framework for instrumenting, generating, collecting, and exporting remote measurement data, such as trace, metric, and log data


#### Reference

- https://opencensus.io/
- https://opentracing.io/
- https://opentelemetry.io/docs/concepts/what-is-opentelemetry/



#### 1.2.2 History

- Dapper (Google): Foundation of all tracers

- Topics related to tracing have been emerging since the 1990s.
    - Google's paper, [Dapper, a Large-Scale Distributed Systems Tracing Infrastructure](https://research.google/pubs/pub36356/), published in 2010, has become the mainstream foundation of tracing.

- Zipkin and OpenZipkin (Twitter)

    - The first open-source tracing system
    - Released by Twitter in 2012

- Jaeger (Uber)

    - Developed by Uber in 2015 and release in 2017 as an open-source project
    - Adopted as a CNCF Incubation project in September 2017
    - Jaeger was approved as a Graduated project in 2019

- StackDriver Trace -> [Cloud Trace](https://cloud.google.com/trace?hl=ko) (Google)

- [X-Ray](https://aws.amazon.com/ko/xray/) (AWS)

![Trace History](image-20220718232202127.png)



#### 1.2.3 Feature

- Jaeger backend is designed with High Scalability in mind

- collectors can be auto-scaled

- Support OpenTracing and OpenTelemetry
    - Designed to support OpenTracing standards from the beginning
    - Since v1.35, Jaeger backend can receive trace data from OpenTelemetry SDK
- Modern Web UI is developed using React
- Cloud Native Deployment
    - Jaeger backend is distributed as a docker image
- Support backwards compatibility with Zipkin
- Support two types of services graphs
    - System Architecture, Deep Dependency Graph
- Provide adaptive sampling
- Support Multiple Storage Backends
    - ex. Memory (default), Cassandra, Elasticsearch
- Service Performance Monitoring (SPM)

#### 1.2.4 Tracing Terms

##### Span

- In distributed tracing, span represents the unit of work performed in a distributed system, typically corresponding to a single operation such as an HTTP request or call to a database.
- A span has the following information:
    - Span Name (Operation Name)
    - Start/Finish Timestamp
    - Span Tags, Logs (key:value)
    - Span Context: Tracing information that allows each span to be distinguished in a trace as it is propagated from one service to another (e.g. span id, Trace id)

##### Trace

- A trace represents the data and execution path across a system
- It is composed of one or more spans, with multiple spans coming together to form a complete trace

##### Instrumentation

- Several libraries are provided as open source for different applications (e.g. databases)
- Instrumentation libraries are used to create spans


![OpenTracing](OpenTracing1.png)

## 2. Jaeger Tracing Architecture

Jaeger consists of multiple components to collect, store, and display tracing data.

- ~~Jaeger client~~ / OpenTelemetry Distro (SDK)
    - Jaeger client is a language-specific implementation of the OpenTracing API for distributed tracing
    - Currently using the OpenTelemetry SDK
- Jaeger Agent
    - A network daemon that receives spans sent via the UDP and is deployed on the same host as the instrumented application
- Jaeger Collector
    - Receives spans for processing and places them in a queue
- Storage Backends
    - Data storage for traces
- Jaeger Query
    - Query service that retrieves data from storage and provides the necessary APIs for the UI

### 2.1 Jaeger Architecture

![Jaeger Architecture](architecture-v1.png)


#### 2.1.1 Jaeger Architecture with Kafka - Intermediate Buffer

- Ingester
    - Kafka can be used as an intermediate buffer between collector and database
    - Ingester is responsible for reading data from Kafka and writing to other storage


![Jaeger Architecture](architecture-v2.png)

#### 2.1.2 Instrumentation

There are two ways to create spans:

- Auto Instrumentation
    - The OpenTelemetry community has created libraries for various applications (e.g., Redis, MongoDB) and provides them on the registry site
    - https://opentelemetry.io/registry/
- Manual Instrumentation
    - If it is not provided as open source, spans must be manually created in the application development

#### 2.1.3 Sampling

Sampling is used to reduce the number of traces stored in the backend by not storing all tracing information raw.

- Head-based sampling
    - The sampling rule is determined at the front end of the jaeger-client
- Tail-based sampling
    - Sampling is done at the collector, so it is called tail-based sampling
    - Adaptive sampling (supported since v1.27) is also available, which allows automatic adjustment of sampling based on traffic and the number of traces entering the system

## 3.Running Jaeger Docker on Local Machine

### 3.1 Hot R.O.D - Running Rides on Demand Sample

HotROD is a "ride on demand" demo application available on Jaeger's github and uses the OpenTracing API. It runs standalone and has multiple microservices running on separate ports to work in a simple MSA format. In this example, we are creating the spans directly without using any instrumentation.

#### Running Jaeger

To get up and running quickly, run it as an all-in-one Docker image that includes all of Jaeger's components.

> You should not use all-in-one Docker image in a production environment. If a container dies, it can be a single source of failure, which can have a significant impact on production services. For production environments, we recommend deploy as individual components.



```bash
$ docker run -d -p6831:6831/udp -p16686:16686 jaegertracing/all-in-one:latest
```



To access the Jaeger UI after the container is running, open up a browser and enter this address, http://localhost:16686.

![Jaeger Web ](image-20220717103342529.png)

#### Run Hot R.O.D Sample Program

The HotROD sample code is written in golang, so you'll need to install the go toolchain beforehand. Download and run the program from Github.

```bash
$ git clone https://github.com/jaegertracing/jaeger
$ cd jaeger/examples/hotrod
$ go run ./main.go all
```

If you enter all above commands, you can run all the services of HotROD at once. You can access the web site at http://127.0.0.1:8080.

![Hot R.O.D WebApp](image-20220717103943745.png)

### 3.2 Play around with Jaeger

When you click the button on the HotROD to request a ride, you'll see a trace of the API in Jaeger.

#### System Architecture > DAG

- This screen gives you a entire view of all your components

![System Architecture DAG](image-20220717104614304.png)

If an error occurs, it's not easy to find in the logs which service it occured.

![Console Log](image-20220717104917246.png)



#### The Benefits of Jaeger Tracing

- Easier to find where failures occured
- Be able to see where the bottlenecks occur across multiple components

![Jaeger Tracing](image-20220717115919867.png)

![Jaeger Tracing](image-20220717115937277.png)

### 3.2 Sample code for using OpenTelemetry for MongoDB and Gin instrumentation

The HotROD application is implemented using the OpenTracing SDK and manual instrumentation. You can also see the version implemented with the latest OpenTelemetry SDK.

When developing web applications, various DBs or web frameworks are used, and the instrumentation for them is also developed as open source, so it can be easily applied to the application.

The example Todo web service on the Aspecto blog uses MongoDB and the Gin web framework. You don't need to create a span by yourself, just configure it in your DB or framework.

- Applying to the MongoDB

```go
func connectMongo() {
  opts := options.Client()
  //Mongo OpenTelemetry instrumentation
  opts.Monitor = otelmongo.NewMonitor() // this is all you have to do. 
  opts.ApplyURI("mongodb://localhost:27017")
  client, _ = mongo.Connect(context.Background(), opts)
...skip...
}
```

- Applying to the Gin web framework

```go
r := gin.Default()
  //Gin OpenTelemetry instrumentation
r.Use(otelgin.Middleware("todo-service")) // this is all you have to do. 
```

### 3.3 Reference

- https://medium.com/opentracing/take-opentracing-for-a-hotrod-ride-f6e3141f7941
- https://www.aspecto.io/blog/opentelemetry-go-getting-started/

## 4.Conclusion

In this post, I briefly introduced Jaeger, but there are other open source tracing projects such as Pinpoint. The Pinpoint is also a part of CNCF project as well.

- https://landscape.cncf.io/?selected=pinpoint

> If you are interested in developing a robot service and platform, you are welcome to apply for our Platform Enginering team. If you want to know what we are doing, take a look at the [YouTube channel](https://www.youtube.com/@NAVERLABS).
>

## 5.Terminology

- Observability
    - Engineer [Rudolf E. Kálmán](https://en.wikipedia.org/wiki/Rudolf_E._K%C3%A1lm%C3%A1n) first introduced the concept of observability
    - *"The ability to understand the current state of a system using only the system's external output"*
    - The three pillars of observability: logs, metrics, and traces
- Tag
    - A tag is a key:value, value defined by the user to query and filter trace data
    - ex. http.method=GET
    - http.status.code=200
- Telemetry data
    - There are three types of telemetry data: metrics, log, and traces

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
