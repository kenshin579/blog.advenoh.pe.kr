---
title: "Python으로 API 호출에 Rate Limiting 적용하기: aiolimiter와 aiometer 사용법"
description: "Python으로 API 호출에 Rate Limiting 적용하기: aiolimiter와 aiometer 사용법"
date: 2025-04-05
update: 2025-04-05
tags:
  - rate limit
  - aiolimiter
  - rate limiting
  - aiometer
  - python
  - 파이썬
---

## 1. 개요

Rate limiting은 API 호출이나 서버 요청을 특정 시간 단위 내에서 제한하는 기법이다. 이는 서버 과부하를 방지하고, 과도한 요청으로 인한 장애를 예방하기 위해 사용된다. 예를 들어, 특정 API에서는 "1초당 20건"과 같은 방식으로 호출 횟수를 제한하기도 한다. 이러한 상황에서 Python으로 개발할 때, 효율적으로 rate limit을 적용할 수 있는 방법에 대해 알아보자.

> 개인적으로 [korea-investment-stock](https://pypi.org/project/korea-investment-stock/) API를 사용하고 있고 한국투자 API 는 1초당 20건 호출 제약이 있어서 이 부분을 해결하기 위해 스터디를 하게 되었다.

## 2. `aiolimiter` 사용방법

### 2.1 `aiolimiter`란?

`aiolimiter`는 비동기 프로그래밍을 지원하는 rate limiter 라이브러리이다. 이는 `asyncio`와 함께 사용되어, 비동기적으로 여러 작업을 처리하는 동안에도 요청 수를 제어할 수 있게 도와준다. `aiolimiter`는 특히 서버나 API 호출을 비동기적으로 처리할 때 유용하다.

#### 사용 예제

다음은 `aiolimiter`를 사용하여 API 호출에 rate limit을 적용하는 예제이다.

```python
class AiolimiterTest(TestCase):
    @classmethod
    def setUpClass(cls):
        max_concurrent = 20
        cls.limiter = AsyncLimiter(max_concurrent, time_period=1)  # 20 calls per second

    def test_run_concurrently(self):
        stock_list = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"] * 4 * 5
        # stock_list = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
        start_time = time.time()

        stock_data = asyncio.run(self.fetch_stocks(stock_list))
        elapsed_time = time.time() - start_time

        print(f"elapsed_time: {elapsed_time}, size: {len(stock_list)}, stock_data: {stock_data}")

    async def fetch_stock_current_price(self, stock_code):
        async with self.limiter:
            url = "<http://httpbin.org/get>"

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{start_time}:{stock_code}: calling stock price")

                    data = await response.json()

                    wait_time = random.uniform(1, 2)  # 1~2초 랜덤 딜레이

                    await asyncio.sleep(wait_time)
                    print(f"{start_time}:{stock_code} Stock price fetched")
                    return data

    async def fetch_stocks(self, stock_list):
        # create a list of tasks
        tasks = [self.fetch_stock_current_price(code) for code in stock_list]

        # run the tasks concurrently
        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)
```

이 코드에서는 `AsyncLimiter`를 사용하여 1초당 20번만 요청을 보낼 수 있도록 설정했다. `limiter`를 사용하여 비동기적으로 API를 호출할 때, 제한된 요청 횟수 내에서 안전하게 데이터를 받아올 수 있다.

## 3. `aiometer` 사용방법

### 3.1 `aiometer`란?

`aiometer`는 `aiolimiter`와 비슷하지만, 여러 개의 rate limiter를 한 번에 관리할 수 있는 기능을 제공한다. 여러 API를 동시에 호출하거나 여러 가지 다른 제약을 두어야 할 때 유용하다.

#### 사용 예제

`aiometer`를 사용하여 비동기 요청에 rate limit을 적용한 예시이다.

```python
class AiometerTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.max_at_once = 5  # 주어진 시간에 동시에 실행되는 작업의 최대 수를 제한하는 데 사용
        cls.max_per_second = 20  # 초당 생성되는 작업 수를 제한

    def test_run_concurrently(self):
        stock_list = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"] * 4 * 5
        # stock_list = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
        start_time = time.time()

        stock_data = asyncio.run(self.fetch_stocks(stock_list))
        elapsed_time = time.time() - start_time

        print(f"elapsed_time: {elapsed_time}, size: {len(stock_list)}, stock_data: {stock_data}")

    async def fetch_stock_current_price(self, stock_code):
        url = "<http://httpbin.org/get>"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{start_time}:{stock_code}: calling stock price")

                data = await response.json()

                wait_time = random.uniform(1, 2)  # 1~2초 랜덤 딜레이

                await asyncio.sleep(wait_time)
                print(f"{start_time}:{stock_code} Stock price fetched")
                return data

    async def fetch_stocks(self, stock_list):
        # create a list of tasks
        tasks = [functools.partial(self.fetch_stock_current_price, code) for code in stock_list]

        # run the tasks concurrently
        results = await aiometer.run_all(tasks, max_per_second=self.max_per_second, max_at_once=self.max_at_once)

        for result in results:
            print(result)
```

`aiometer.run_all(tasks, 20, 5)`은 1초에 최대 20번의 호출만을 허용하도록 설정했고 추가로 동시 실행 개수는 5개로 제한을 두었다.

## 4. 마무리

두 라이브러리 모두 비동기 처리가 가능한 환경에서 매우 유용하게 사용될 수 있다. `aiometer`의 경우 동시에 실행할 수 있는 작업의 최대 수를 제한할 수 있어 과도한 I/O를 방지할 수 있다는 장점이 있다.

| 기능                              | `aiometer`  | `aiolimiter`                 |
| --------------------------------- | ----------- | ---------------------------- |
| 속도 제한 (Rate Limit)            | ✅ 지원      | ✅ 지원                       |
| 동시 실행 개수 제한 (Concurrency) | ✅ 지원      | ❌ 지원 안 함                 |
| 복잡도                            | 비교적 간단 | 직접 `async with`로 제어해야 |

## 5. 참고

- [파이썬 Async API Call 에 Rate Limit 적용하기](https://devocean.sk.com/blog/techBoardDetail.do?ID=166023&boardType=techBlog)
