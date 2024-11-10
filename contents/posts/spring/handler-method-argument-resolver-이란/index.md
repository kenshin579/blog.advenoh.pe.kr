---
title: "Custom Handler Method ArgumentResolver 만들어보기"
description: "Custom Handler Method ArgumentResolver 만들어보기"
date: 2020-07-20
update: 2020-07-20
tags:
  - java
  - spring
  - spring boot
  - ArgumentResolver
  - 자바
  - 스프링
  - 스프링부트
  - 리졸버
---

## 1.HandlerMethodArgumentResolver란?

### 1.1 들어가면

`HandlerMethodArgumentResolver`에 대해서 알아보자. 아래와 같이 컨트롤러 메서드에 여러 인자 값(ex. `@PathVariable`)을 추가하여 자주 작업을 한다. 이런 인자는 `HandlerMethodArgumentHandler`에 의해서 처리가 된다.

필요에 따라서 컨트롤러 메서드에 여러 인자 값을 추가하는데 이런 인자는 `HandlerMethodArgumentHandler`에 의해서 처리가 된다.

```java
@GetMapping
public ResponseEntity<?> getStudentList(
  @PathVariable(value = "version") Integer version,
  @RequestParam(value = "listSize", defaultValue = "10") Integer listSize) {
  ...생략...
}
```

`HandlerMethodArgumentHandler`는 어노테이션이나 타입에 따라서 실제 값을 컨트롤러에 넘겨주는 역할을 한다. 스프링에서도 기본적으로 여러 Argument Resolver가 구현되어 있다.

- `PathVariableMethodArgumentResolver`
    - `@PathVariable` 어노테이션으로 선언된 인자를 처리하는 Argument Resolver이다
- `RequestParamMethodArgumentResolver`
    - `@RequestParam` 어노테이션으로 선언된 인자의 실제 값을 지정해 준다
- RequestHeaderMapMethodArgumentResolver
    - `@RequestHeader` 어노테이션으로 선언된 인자의 실제 값을 지정해 준다

`HandlerMethodArgumentHandler`을 사용하게 되면 중복 코드를 줄이고 공통 기능으로 빼서 사용할 수 있는 장점이 있다. 이제 Custom `HandlerMethodArgumentResolver`를 직접 구현해보도록 하자.


## 2. Custom Argument Resolver 만들기

### 2.1 Argument Resolver 컨트롤러에 사용예제

컨트롤러 메서드에서 `@ClientIp` 어노테이션이 추가된 인자를 넘겨주면 Client Ip 주소를 얻어 올 수 있는 Resolver를 만들어보자.

```java
@RestController
public class IpController {
    @GetMapping("/test")
    public String getIpAddress(@ClientIp String clientIp) {
        return String.format("ip address : %s", clientIp);
    }
}

```

### 2.2 Argument Resolver 생성하기

Argument Resolver 인터페이스에는 2가지 메서드가 존재하고 `supportsParameter()`가 참인 경우에 `resolveArgument()` 메서드를 실행한다.

```java
public interface HandlerMethodArgumentResolver {

	boolean supportsParameter(MethodParameter parameter);

	@Nullable
	Object resolveArgument(MethodParameter parameter, @Nullable ModelAndViewContainer mavContainer,
			NativeWebRequest webRequest, @Nullable WebDataBinderFactory binderFactory) throws Exception;

}

```

| 메서드              | 설명                                                       |
| ------------------- | ---------------------------------------------------------- |
| `supportsParameter` | 현재 parameter를 resolver가 지원할지 true/false로 반환한다 |
| `resolveArgument`   | 실제 바인딩할 객체를 반환한다                              |



```java
@Slf4j
@Component
public class ClientIpArgumentResolver implements HandlerMethodArgumentResolver {
    @Override
    public boolean supportsParameter(MethodParameter methodParameter) {
        return methodParameter.hasParameterAnnotation(ClientIp.class);
    }

    @Override
    public Object resolveArgument(MethodParameter methodParameter, ModelAndViewContainer modelAndViewContainer, NativeWebRequest nativeWebRequest, WebDataBinderFactory webDataBinderFactory) throws Exception {
        HttpServletRequest request = (HttpServletRequest) nativeWebRequest.getNativeRequest();

        String clientIp = request.getHeader("X-Forwarded-For");
        if (StringUtils.isEmpty(clientIp) || "unknown".equalsIgnoreCase(clientIp)) {
            clientIp = request.getRemoteAddr();
        }
        log.debug("[debug] clientIp : {}", clientIp);
        return clientIp;
    }
}
```

- `supportsParameter()` 메서드에서는 인자 값에 ClientIp 어노테이션이 포함되어 있는 지 확인한다
- `resolveArgument()` 메서드에서는 실제 client Ip 주소를 request에서 얻어 오는 로직이 있다

### 2.3 Argument Resolver 등록하기

이제 앞에서 생성한 Resolver를 `addArgumentResolvers()` 메서드에서 추가해주면 된다.

```java
@RequiredArgsConstructor
@Configuration
public class WebConfig implements WebMvcConfigurer {
    private final ClientIpArgumentResolver clientIpArgumentResolver;

    @Override
    public void addArgumentResolvers(List<HandlerMethodArgumentResolver> argumentResolvers) {
        argumentResolvers.add(clientIpArgumentResolver);
    }
}
```

### 2.4 Controller 실행하기

Unit Test로 확인해보자. 컨트롤러에서 Client Ip 주소를 잘 반환해주고 있다.

```java
@Test
void getIpAddress() throws Exception {
  this.mockMvc.perform(get("/test"))
  .andDo(print())
  .andExpect(status().isOk())
  .andExpect(jsonPath("$", is("ip address : 127.0.0.1")));
}
```

## 3. Argument Resolver 동작 방식

Custom Argument Resolver를 구현해보았다. 이제 스프링안에 내부적으로 어떻게 Argument Resolver가 호출되는지 알아보자. Argument Resolver 동작 구조를 쉽게 보여주는 이미지([Carrey's 기술 블로그](https://jaehun2841.github.io/2018/08/10/2018-08-10-spring-argument-resolver/#spring-argument-resolver)에서 참고)이다.

![Dispatch-Seq](https://jaehun2841.github.io/2018/08/10/2018-08-10-spring-argument-resolver/Dispatch-Seq.jpg)

Request 처리시 Argument Resolver가 실행되는 순서는 크게 보면 아래와 같다. 실제 실행시 debug해서 확인하면 더 쉽게 이해할 수 있다.

1. Client에서 Request 요청을 보낸다
2. 요청은 Dispatcher Serlvet에서 처리가 된다
3. 요청에 대한 HandlerMapping 처리
    1. (스프링 구동시) `RequestMappingHandlerAdapter`에서 필요한 Argument resolver를 등록한다 ([#1.2.1](https://blog.advenoh.pe.kr/handler-method-argument-resolver-이란/#121-스프링-기본--Custom-Argument-Resolver은-어디서-등록이-되나))
    2. (요청시) `RequestMappingHandlerAdapter.invokeHandlerMethod()`에서 Argument resolver를 실행한다 ([#1.2.2](https://blog.advenoh.pe.kr/handler-method-argument-resolver-이란/#122-supportsParameter는-어디에서-호출되나))
        1. `DispatcherServlet.doDispatch()` -> `RequestMappingHandlerAdapter.handleInternal()` -> `invokeHandlerMethod()`
4. 컨트롤러 메서드 실행

#### 1.2.1 스프링 기본 + Custom Argument Resolver은 어디서 등록이 되나?

`RequestMappingHandlerAdapter` 객체가 초기화(ex. 스프링 시작시) 될 때 `afterPropertiesSet()`에서 `getDefaultArgumentResolvers()` 메서드를 호출하여 기본 스프링과 Custom resolver를 등록한다.

```java
private List<HandlerMethodArgumentResolver> getDefaultArgumentResolvers() {
		List<HandlerMethodArgumentResolver> resolvers = new ArrayList<>(30);
		...생략...
      
		resolvers.add(new PathVariableMethodArgumentResolver());
		resolvers.add(new RequestPartMethodArgumentResolver(getMessageConverters(), this.requestResponseBodyAdvice));
		resolvers.add(new RequestHeaderMethodArgumentResolver(getBeanFactory()));

    ...생략...
		// Custom arguments
		if (getCustomArgumentResolvers() != null) {
			resolvers.addAll(getCustomArgumentResolvers());
		}
}
```

#### 1.2.2 supportsParameter는 어디에서 호출되나?

`HandlerMethodArgumentResolverComposite.getArgumentResolver()` 메서드에서 `supportsPameter()` 실행해서 true를 반환하면 해당 Argument Resolver를 반환한다.

```java
private HandlerMethodArgumentResolver getArgumentResolver(MethodParameter parameter) {
		HandlerMethodArgumentResolver result = this.argumentResolverCache.get(parameter);
		if (result == null) {
			for (HandlerMethodArgumentResolver resolver : this.argumentResolvers) {
				if (resolver.supportsParameter(parameter)) { //true이면 resolveArgument를 결과로 반환함
					result = resolver;
					this.argumentResolverCache.put(parameter, result);
					break;
				}
			}
		}
		return result;
}
```

`getArgumentResolver()` 메서드는 아래 여러 메서드에 의해서 호출된다.

- `DispatcherServlet.doDispatch()` -> ...생략... -> `invokeHandlerMethod()` -> ...생략... -> `InvocableHandlerMethod.getMethodArgumentValues()` -> `getArgumentResolver()` 순으로 실행되는 것을 확인할 수 있다.


![](image-20200912154932896.png)

## 4. 마무리

`HandlerMethodArgumentResolver`는 컨트롤러 메서드에서 인자 값에 대한 처리를 위해 사용된다. 이미 스프링에서 공통기능으로 많이 제공하고 있지만, 사용자용 메서드도 쉽게 작성하여 중복 로직을 많이 줄일 수 있어 용의하게 사용된다.

관련 소스는 [github](https://github.com/kenshin579/tutorials-java/tree/master/springboot-handler-method-argument-resolver)에 올려두어서 참고하시면 됩니다.

## 5. 참고

- https://webcoding-start.tistory.com/59
- https://velog.io/@riechu3228/HandlerMethodArgumentResolver
- http://wonwoo.ml/index.php/post/1092
- https://sun-22.tistory.com/76
- https://www.mscharhag.com/spring/json-schema-validation-handlermethodargumentresolver
- https://jaehun2841.github.io/2018/08/10/2018-08-10-spring-argument-resolver/
- [https://jekalmin.tistory.com/entry/%EC%BB%A4%EC%8A%A4%ED%85%80-ArgumentResolver-%EB%93%B1%EB%A1%9D%ED%95%98%EA%B8%B0](https://jekalmin.tistory.com/entry/커스텀-ArgumentResolver-등록하기)
- https://a1010100z.tistory.com/127
