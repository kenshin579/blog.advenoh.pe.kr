# 블로그 : Spring / Spring Boot Annotation 모음
[https://springframework.guru/spring-framework-annotations/](https://springframework.guru/spring-framework-annotations/)
@SpringBootApplication
public class Application {
@Autowired <— bookingSerivce bean을 이 변수에 assign시킴
BookingService bookingService;

@Bean <— 단지 스프링에게 이걸 Bean으로 등록하겠다는 의미.
BookingService bookingService() {
return new BookingService();
}

public static void main(String[] args) {
ApplicationContext ctx = SpringApplication.run(Application.class, args);
BookingService bookingService = ctx.getBean(BookingService.class);
bookingService.book("Alice", "Bob", "Carol");
}
}
- [ ] @Bean과 @Autowired의 차이점
ㅁ. [http://www.baeldung.com/spring-autowire](http://www.baeldung.com/spring-autowire)
ㅁ. [https://stackoverflow.com/questions/34172888/difference-between-bean-and-autowired](https://stackoverflow.com/questions/34172888/difference-between-bean-and-autowired)
ㅁ. [https://github.com/kenu/springstudy2013/blob/master/0325/5.javaCodeConfig.md](https://github.com/kenu/springstudy2013/blob/master/0325/5.javaCodeConfig.md)

public class HelloWorldServiceClient {

This annotation tells the Spring container where to perform dependency injection
@Autowired <— 타입을 이용해서 자동으로 의존관계를 맺어줌 #1, #2. helloWorld property에 HelloWorldService 타입의 빈 객체를 전달한
private HelloWorldService helloWorld;
}

@Configuration to tell the container that beans are defined in AppRunner
@Configuration <— 이 어노테이션은 container에기 빈이 정의되어 있다고 알려줌 (XML로 정의하는 것대신 자바코드로 알려줌)
public class AppRunner {

what objects should be registered as beans.
*@Bean 빈 객체로 등록되어 있음 #1*
public HelloWorldService createHelloWorldService() {
return new HelloWorldServiceImpl();
}

*@Bean #2*
public HelloWorldServiceClient createClient() {
return new HelloWorldServiceClient();
}
}
::@:: Autowired <— JournalRepository 타입의 repo 변수를 자동으로 연결해서 index메서드가 갖다 쓸수 있게 함
JournalRepository repo;

- [ ] 타입을 이용해서 의존 관계를 자동으로 설정하며 사용함.
- [ ] 설정위치: 생성자, 필드, 메서드의 세곳에 적용가능
- [ ] [http://tbang.tistory.com/87](http://tbang.tistory.com/87)

@Bean <— 스프링이 제어권을 가지고 직접 관리하는 객체 (인스터스등등)
- [ ] Spring IoC container란
ㅁ. 빈(객체)을 생성하고 관리해주는 객체
- [ ] [http://www.logicbig.com/tutorials/spring-framework/spring-core/quick-start/](http://www.logicbig.com/tutorials/spring-framework/spring-core/quick-start/)
- [ ] 참고, [http://www.logicbig.com/tutorials/spring-framework/spring-core/java-config/](http://www.logicbig.com/tutorials/spring-framework/spring-core/java-config/)
- [ ] [http://ooz.co.kr/178](http://ooz.co.kr/178)
- [ ] [http://sailboat-d.tistory.com/33](http://sailboat-d.tistory.com/33)

@Configuration
Public class SpringConfig {
@Bean <— 의존할 빈 객체에 대한 메서드를 호출하는 것으로 의존관계를 설정할 수 있음
Public Viewer viewer() {
MonitorViewer viewer = new MonitorView();
viewer.setDisplayStrategy( **displayStrategy** ());
Return viewer;
}

**@Bean**
public DisplayStrategy **displayStrategy** () {
return new DefaultDisplayStrategy();
}
@Configuration
@ComponentScan(basePackages=“UserDaoJdc.package.name”) <— 이 어노테이션은 XML에 일일이 빈등록을 하지 않고, 각 빈 클래스에 @Component를 통해 자동 빈등록을 함
@Autowired UserDao userDao;

@Bean
Public UserService userService() {
UserServiceImpl service = new UserServiceImp();
service.setUserDao(this.userDao);
return service;
}
- [ ] @Controller, @Repository, @Service (@Component 어노테이션를 포함함)도 빈 등록 대상이 됨

@Component <— 이 어노테이션이 붙은 클래스는 빈 스캐너를 통해 자동으로 빈으로 등록됨
public class UserDaoJdc implements UserDao {

- [ ] 참고
ㅁ. [https://m.blog.naver.com/PostView.nhn?blogId=writer0713&logNo=220695884239&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F](https://m.blog.naver.com/PostView.nhn?blogId=writer0713&amp;logNo=220695884239&amp;proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)
ㅁ. [http://egloos.zum.com/pelican7/v/2578951](http://egloos.zum.com/pelican7/v/2578951)
ㅁ. [http://yellowh.tistory.com/109](http://yellowh.tistory.com/109)
ㅁ. [http://thswave.github.io/spring/2015/02/02/spring-mvc-annotaion.html](http://thswave.github.io/spring/2015/02/02/spring-mvc-annotaion.html)
ㅁ. [http://smallgiant.tistory.com/11](http://smallgiant.tistory.com/11)
@Configuration
@ConditionalOnWebApplication <— 웹 애플리케이션 때만 구성 내용을 반영함 (spring-boot-starter-web 폼이 없으면 그냥 넘어감)
@ConditionalOnClass(JournalRepository.class) <— 해당 클래스가 있을 경우에만 반영함
@EnableConfigurationProperties(JournalProperties.class) <— JournalProperties 클래스를 커스텀 프로퍼티처럼 쓰겠다는 뜻. 이 클래스의 프로퍼티는 @Autowired, @Value로 얼마든지 접근할 수 있음
@ConditionalOnProperty(prefix = "journal", name = {"context-path", "banner"}, matchIfMissing = true) <— journal.contextpath, journal.banner property가 따로 정의되어 있지 않을 경우에만 구성 내용을 반영함
public class JournalAutoConfiguration extends RepositoryRestMvcConfiguration {
private final String API_PATH = "/api";
private final String BANNER = "_META-INF_banner/journal.txt";
…
}
@ConfigurationProperties(location=“classpath:mail.properties)
public class MailConfigurationp
- [ ] @ConfigurationProperties은 **spring boot 1.5에 추가됨**. 환경설정 파일(ex. application.properties)에서 값을 추출해 주입해줌. 
- [ ] [http://wonwoo.ml/index.php/post/1599](http://wonwoo.ml/index.php/post/1599)
- [ ] [http://jdm.kr/blog/230](http://jdm.kr/blog/230)
- [ ] [http://blog.codeleak.pl/2014/09/using-configurationproperties-in-spring.html](http://blog.codeleak.pl/2014/09/using-configurationproperties-in-spring.html)

@ConfigurationProperties(prefix = "myapp”) <— 커스텀 properties를 추가할 수 있음.
public static class MyAppProperties {
private String name;
private String description;
private String serverIp;

public String getName() {
return name;
}

public void setName(String name) {
this.name = name;
}

public String getDescription() {
return description;
}
..
}
application.properties :
**myapp.server** -ip=192.168.34.56
**myapp.name** =My Config App
**myapp.description** =This is an example

[http://javacan.tistory.com/entry/springboot-configuration-properties-class](http://javacan.tistory.com/entry/springboot-configuration-properties-class)

[https://medium.com/@logan.81k/spring-boot-configurationproperties-a73638b4d5ae](https://medium.com/@logan.81k/spring-boot-configurationproperties-a73638b4d5ae)
[https://www.boraji.com/spring-boot-configurationproperties-example](https://www.boraji.com/spring-boot-configurationproperties-example)
@Controller <— 웹요청을 처리하는 컨트롤러로 사용함
public class CollaborationActionController {

@RequestMapping(value = "_editAction.do_ **{documentId}**", method = RequestMethod.POST) <— 응답을 수행할 HTTP 요청을 명시할 수 있다.
@ResponseStatus(HttpStatus.OK) <— response code를 사용자가 지정함
public Callable<Object> editAction(@PathVariable("documentId") final String documentId, <— URL 템플릿 변수에 접근할 때 사용
@RequestParam("serial") final String serial, <— HTTP 파라미터와 매핑

@RunWith(SpringJUnit4ClassRunner.class)
::@ContextConfiguration:: (classes = LettuceRedisConfig.class) <- 테스트 클래스에 대해 ApplicationContext를 어떻게 로딩하고 어떻게 설정하는지 결정하는 클래스수준의 메타에디터를 정의
public class SpringDataLettuceTest {
@Autowired
StringRedisTemplate stringRedisTemplate; <—
ㅁ. [https://blog.outsider.ne.kr/859](https://blog.outsider.ne.kr/859)
ㅁ. [http://noritersand.tistory.com/156](http://noritersand.tistory.com/156)

@Configuration
@ConditionalOnClass({JedisCluster.class}) <— 해당 class가 있는지 검사를 하는 조건 어노테이션
@EnableConfigurationProperties( **RedisProperties.class** ) <— property 클래스를 지정해준다. 
public class JedisClusterConfig {
@Autowired
private **RedisProperties** redisProperties;
- [ ] spring boot에서 사용가능 한 것 같음
- [ ] [http://kingbbode.tistory.com/40](http://kingbbode.tistory.com/40)
@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@Configuration
@EnableAutoConfiguration <— 이 어노테이션은 부트설정에 따라서 필요한 설정에 따라 필요한 모든 빈을 자동으로 로드해준다
@ComponentScan
public @interface **SpringBootApplication** {
Class<?>[] exclude() default {};

String[] excludeName() default {};
…
- [ ] 참고, [http://devidea.tistory.com/entry/spring-spring-boot-configuration-%EC%9D%B4%ED%95%B4](http://devidea.tistory.com/entry/spring-spring-boot-configuration-%EC%9D%B4%ED%95%B4)
@Configuration
@EnableGlobalAuthentication <— 이 어노테이션을 붙인 클래스는 AuthenticationManagerBuilder의 전역 인스턴스를 구성하며 앱에 있는 모든 빈에 보안을 적용함
public class InMemorySecurityConfiguration {
@Autowired <— configureGlobal은 AuthenticationManagerBuilder를 자동 연결하는 메서드임
public void configureGlobal( **AuthenticationManagerBuilder** auth) throws Exception {
auth.inMemoryAuthentication().withUser("user").password("password").roles("USER")
.and().withUser("admin").password("password").roles("USER", "ADMIN");
}
}
- [ ] AuthenticationManagerBuilder는 개발자가 UserDetailService와 인증 공급자를 추가해서 인증 로직을 쉽게 구현할 수 있게 도와줌
@Configuration
@EnableAuthorizationServer <— OAuth2 인증 서버를 구성함. 인증 끝점(_oauth_authorize)은 개발자가 직접 보안을 걸어야 함. 
토큰끝점(_oauth_token)은 사용자 credential(여기선 DB에서 조회한 username과 password)에 따라 HTTP 기본 인증 방식으로 보안이 자동 적용됨
@EnableResourceServer **<— 리소스 서버를 구성함. 알맞은 OAuth2 토큰을 보낸 요청만 통과시키는 스프링 시큐리티 필터를 켬**
public class ResourceOAuthSecurityConfiguration extends **ResourceServerConfigurerAdapter** {

@Override
public void configure(HttpSecurity http) throws Exception {
http.authorizeRequests()
.antMatchers("/").permitAll()
.antMatchers("_api_").authenticated();
}

}
@EnableScheduling <— 이걸 붙이면 ScheduleAnnotationBeanPostProcessor 클래스가 필요하다하는 거임.
또 @Scheduled를 붙인 메서드는 전부 TaskScheduler 인터페이스 구현체가 실행되도록 등록함
@SpringBootApplication
public class SpringBootRabbitmqApplication {

@Scheduled(fixedDelay = 500L) <— 0.5초마다 큐에 메시지를 전송함
public void sendMessages() {
producer.sendTo(queue, "안녕하세요, 여러분! 지금 시각은 " + new Date());
}
@Entity <— JPA에서 제공하는 어노테이션으로 클래스의 선언부분에 부여해야 함
@Entity를 부여하는 것으로 영속화(Persistence)의 대상이 됨.
애플리케이션이 실행이 될 때 엔티티 자동검색을 통하여 이 어노테이션이 선언 된 클래스들은 엔티티 빈으로 등록합니다.
- [ ] 참고, [http://chan180.tistory.com/168](http://chan180.tistory.com/168)

public class Journal {

@Id <— Primary Key 필드로 명시함
::@GeneratedValue(strategy = GenerationType.AUTO):: <— 데이터베이스에 의해 자동으로 생성된 값이라는 의미. 프로그램 상에서 조작된 데이터가 아닌, 실제 DB에 데이터가 저장될때 생성되는 값임. 
private Long id;
private String title;
private Date created;
private String summary;

@Transient <— JPA 엔진은 값을 저장하지 않고 무시함
private SimpleDateFormat format = new SimpleDateFormat("MM_dd_yyyy”);

@JmsListener(destination = "${myqueue}”)  <— 이 함수가 consumer listener 역할을 하게 됨
public String simplerConsumer(String message) {
log.info("간단한 소비기> " + message);
return message + "와 스프링 메시징을 시작!";
}

@Value("${myqueue}")
String queue;

@Bean
CommandLineRunner start(JmsTemplate template) {
return args -> {
log.info("전송> ... queue: {}", queue);
template.convertAndSend(queue, "스프링 부트”); <— 여기서 send하면 Listener로 등록된 함수가 호출되게 됨
};
}
@PropertySource(name = "myProperties", value = "values.properties”) <— properties 파일에 등록된 value값에 접근할 수 있음
public class ValuesApp {
@Value("${value.from.file}”) <— 변수에 mapping해줌
private String valueFromFile;
- [ ] Spring boot에서는 @PropertiesSource 사용을 권장하지 않음, [http://kingbbode.tistory.com/39](http://kingbbode.tistory.com/39)
- [ ] 참고, [https://www.mkyong.com/spring/spring-propertysources-example/](https://www.mkyong.com/spring/spring-propertysources-example/)
public interface JournalRepository extends JpaRepository<Journal, Long> {
List<Journal> findByCreatedAfter(Date date); <— 이렇게 만들어주면 알라서 query를 생성해줌

@Query("select j from Journal j where j.title like %?1%”) <— custom query를 실행하고 싶다면
List<Journal> findByCustomQuery(String word);
}

@RestController <— 스프링 부트에서 웹 컨트롤러 클래스로 지정.
@Controller에 위에 설명한 @ResponseBody를 추가한 효과를 가진다.
DispatcherServlet이 갖고 갈 웹 컨트롤러 클래스임을 표시함
class WebApp

@RequestMapping <— HTTP 요청을 처리하는 메서드로 인식
public class greeting() {
@RequestMapping(value=“/journal”, produce = {MediaType.APPLICATION_JSON_UTF8_VALUE}) <— produce JSON형태로 return해줌
public @ResponseBody LIst<Journal> getJournal()
- [ ] [https://blog.outsider.ne.kr/902](https://blog.outsider.ne.kr/902)
@ExceptionHandler(DataFormatException.class)
@ResponseStatus(value = HttpStatus.NOT_FOUND, reason = “error code!”) <— 원래의 response code를 사용자가 지정한 NOT_FOUND 코드로 바꿔서 출력한다. (404)
public void handleDataFormatException(DataFormatException ex,
HttpServletResponse response) {

logger.info("Handlng DataFormatException - Catching: " + ex.getClass().getSimpleName());
}

@Service <— 이 어노테이션은 클래스를 스프링 컨테이너가 빈으로 인식 가능한 스테레오타입으로 표시 (이 빈을 @Autowired로 자동 연결할 수 있게 됨)
public class JournalService {
@JmsListener(destination = "${myqueue}")
@SendTo("${myotherqueue}”) <— 해당 목적지에 message를 보냄
public String simplerConsumer(String message) {
log.info("간단한 소비기> " + message);
return message + "와 스프링 메시징을 시작!";
}

@JmsListener(destination = "${myotherqueue}")
public void anotherSimplerConsumer(String message) {
log.info("다른 간단한 소비기> " + message);
}
@SpringBootApplication <— @Configuration, @EnableAutoConfiguration, @ComponentScan 애너테이션이 뭉쳐진 애너테이션
public class SimpleWebApp
- [ ] 자동 구성을 유발하는 어노테이션임.
@Entity
@Table(name = "entry”) **<— entry라는 table을 생성함**
public class JournalEntry {

@JsonSerialize(using = JsonDateSerializer.class) <— 커스텀 클래스로 데이터를 직렬화함. 날짜를 특정형식으로 나타낼때 필요한 어노테이션.
public Date getCreated() {
return created;
}

@JsonIgnore <— 이 클래스를 JSON 문자열로 나타낼때 대상에서 제외하라는 뜻
public String getCreatedAsShort() {
return format.format(created);
}
@Transactional <— REST 호출에 트랜잭션을 걸어 API동시 호출시 데이터 정합성 문제가 없도록 보호함
@RepositoryRestResource(collectionResourceRel = "entry", path = "journal”) <— 경로를 journal로 바꿈, 리소스는 복수형대신 entry로 수정함
public interface JournalRepository extends JpaRepository<JournalEntry, Long> {
[http://localhost:8080/api/journal/search](http://localhost:8080/api/journal/search) 로 원하는 데이터를 검색할 수 있음
List<JournalEntry> findByCreatedAfter(@Param("after”) <— 인자로 안에서 URL의 쿼리 파라미터명을 넣음. _search_findByCreatedAfter?after=2016-02-1
@DateTimeFormat(iso = ISO.DATE) Date date);

}

- - - -

@Bean(destoryMethod = “close”) <— 객체가 close되는 시점은 어떻게 되나? 객체를 close()하면 호출되는 건가?
- [ ] 참고, [https://stackoverflow.com/questions/44756872/spring-core-default-bean-destroy-method](https://stackoverflow.com/questions/44756872/spring-core-default-bean-destroy-method)

@Resouce
ㅁ. 어플리케이션에서 필요로 하는 자원을 자동 연결 (의존하는 빈 객체 전달) 할때 사용
ㅁ. @Autowired와 같은 기능 (차이점: @Autowired - by type, @Resource - by name)
ㅁ. 설정위치 : 프로퍼티, setter 메서드
ㅁ.
ㅁ. [http://blog.daum.net/feelsogreat/42](http://blog.daum.net/feelsogreat/42)

#tistory #blog #스터디중