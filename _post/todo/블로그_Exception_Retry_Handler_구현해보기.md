# 블로그 : Exception Retry Handler 구현해보기
* 들어가며
* 개발 환경
* 사용법
* 참고

**코멘트**
-

1. 들어가며

외부 REST API를 사용할 때 네트워크가 불안하여 원하는 결과를 얻기 위해 종종 몇번 시도를 해야 할때가 있습니다. 지금 하는 프로젝트에서도 사용해야 해서 간단하게 정리를 해보았습니다.

2. 개발 환경

* OS : Mac OS
* IDE: Intellij
* Java : JDK 1.8
* Source code : [github](https://github.com/kenshin579/tutorials-java-examples/tree/master/retry-exception-handler)
* Software management tool : Maven

3. Exception Retry Handler 구현해보기

대부분 네트워크로

여러 시도하는 코드가 필요하여 간단한 예제로 IP:PORT로 Socket을 생성하는 코드로 작성을 했습니다.

Socket으로 IP:PORT로 연결을 시도ㅎ=

네트워크로

public class SocketClient {
private Socket clientSocket;
private PrintWriter out;
private BufferedReader in;
public void startConnection(String ip, int port) throws IOException {
clientSocket = new Socket(ip, port);
out = new PrintWriter(clientSocket.getOutputStream(), true);
in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
}
}

public SocketClient startConnection(String ip, int port) {
SocketClient client = new SocketClient();
try {
client.startConnection(ip, port);
} catch (IOException e) {
log.error("error", e);
}
return client;
}

3.1 간단한 구현

public SocketClient getConnectionWithRetry(String ip, int port) {
SocketClient client = new SocketClient();
int numRetries = 3;
while (true) {
try {
client.startConnection(ip, port);
} catch (IOException e) {
log.info("retry connection...", e);
numRetries--;
if (numRetries < 0) {
log.warn("Retry limit exceeded");
break;
}
try {
TimeUnit.SECONDS.sleep(3);
} catch (InterruptedException e1) {
log.error("sleep error", e1);
}
}
}
return client;
}

3.2 Oracle

```
Frank Thought
역시 구글링이 답인가 보네요. 역시 다른 분들은 너무 1차적으로만 생각을 했었는데, 재사용 가능하도록 구현을 한번 더 생각해보는 것도 좋을 것 같다는 생각이 들었습니다.
```

3.3 다른 Library 구현체 알아보기

역시 많은 분들이 라이브러리 형식으로 제공하고 있었습니다. 그만큼 자주 발생 이슈이며 유용하기 때문에 라이브러리를 제공하는 것 같습니다.

* FailSafe
* RetryCatch

너무 큰 프로젝트는 제 한도에서 시간이 많이 걸릴 것으로 판단되어 하나면 분석해보도록 하겠습니다.

실제 라이브러리 형식으로 어떻게 구현을 했는지 보면 좋을 것 같다.

4. 참고

* Exception Retry
	* [https://stackoverflow.com/questions/13239972/how-do-you-implement-a-re-try-catch](https://stackoverflow.com/questions/13239972/how-do-you-implement-a-re-try-catch)
	* [https://docs.oracle.com/en/cloud/paas/app-container-cloud/cache/handle-connection-exceptions-retries.html](https://docs.oracle.com/en/cloud/paas/app-container-cloud/cache/handle-connection-exceptions-retries.html)
	* [https://crunchify.com/how-to-retry-operation-n-number-of-times-in-java/](https://crunchify.com/how-to-retry-operation-n-number-of-times-in-java/)
	* [https://myadventuresincoding.wordpress.com/2014/07/30/java-creating-a-simple-retry-command-with-function-passing-in-java-8/](https://myadventuresincoding.wordpress.com/2014/07/30/java-creating-a-simple-retry-command-with-function-passing-in-java-8/)
* Library
	* [https://github.com/bnsd55/RetryCatch](https://github.com/bnsd55/RetryCatch)
	* [https://github.com/jhalterman/failsafe](https://github.com/jhalterman/failsafe)

#tistory #blog #스터디중