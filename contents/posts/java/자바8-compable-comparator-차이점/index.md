---
title: "자바 Comparable과 Comparator의 차이점"
description: "자바 Comparable과 Comparator의 차이점"
date: 2020-04-15
update: 2020-04-15
tags:
  - java
  - java8,
  - comparator
  - comparing
  - sort
  - 자바
  - 자바8
  - 정렬
---

자바에서 객체 정렬 시 사용되는 Comparator와 Comparable 인터페이스 간의 차이점을 알아보겠습니다.

예제로 작성한 코드는 github [java-compare](https://github.com/kenshin579/tutorials-java/tree/master/java-compare) 모듈을 참고해주세요.

## Comparable vs. Comparator

두 인터페이스 모두 컬렉션을 정렬할 때 정렬 규칙을 설정하는 데 사용되는데, 차이점은 아래와 같습니다.

- Comparable
    - 정렬할 대상 객체에 Comparable 인터페이스를 implements해서 compareTo() 메서드를 구현해야 한다
    - compareTo() 메서드는 this와 o 객체의 차이점에 따라서 int 값을 반환하는 메서드이고 이 반환 값에 따라서 정렬이 이루어진다
        - 1 : this > o , this가 o보다 큰 경우
        - -1 : this < o this가 o보다 작은 경우
        - 0 : this == o, 두 객체 같은 경우

```java
public interface Comparable<T> {
  public int compareTo(T o);
}
```

- Comparator

    - 정렬할 대상 객체를 직접 수정할 수 없는 경우에 Comparator 인터페이스를 사용해서 정렬할 수 있다
        - compare() 메서드는 o1, to2 객체의 차이점에 따라서 int값을 반환하는 메서드이고 이 반환 값에 따라서 정렬이 이루어진다
            - 1 : o1 > o2 첫번째 객체가 큰 경우
            - -1 : o1 < o2 첫번째 객체가 작은 경우
            - 0 :  o1 == o2 두 객체가 같은 경우

```java
public interface Comparator<T> {
	int compare(T o1, T o2);
}
```

## 1. 정렬할 대상 객체

Comparable의 경우에는 객체 자체에 Comparable 인터페이스를 구현해야 해서 Comparator와 구분하기 위해서 각각 다른 객체로 생성했습니다.

### 1.1 Comparable

```java
@Getter
@Setter
@AllArgsConstructor
public class ComparablePlayer implements Comparable<ComparablePlayer> {
	private String name;
	private int score;

	@Override
	public int compareTo(ComparablePlayer o) {
		return o.getScore() - this.getScore();
	}
}

```


### 1.2 Comparator

```java
@Getter
@Setter
@AllArgsConstructor
public class ComparatorPlayer {
	private String name;
	private int score;

	public static int compareByScoreThenName(ComparatorPlayer lhs, ComparatorPlayer rhs) {
		if (lhs.getScore() == rhs.getScore()) {
			return lhs.getName().compareTo(rhs.getName());
		} else {
			return lhs.getScore() - rhs.getScore();
		}
	}
}

```

## 2. 객채 정렬하기

### 2.1 Collections.sort()로 정렬하기

Collections의 sort() 메서드는 2가지 메서드를 제공합니다. Comparable 객체의 List를 정렬할 수 있는 메서드와 Comparator 객체를 인자로 넘겨서 정렬할 수 있는 메서드를 제공합니다.

```java
public static <T extends Comparable<? super T>> void sort(List<T> list);
public static <T> void sort(List<T> list, Comparator<? super T> c);
```

Comparable 객체의 리스트를 정렬하고 isSorted() 메서드로 정렬이 되었는지 확인할 수 있습니다.

```java
@Test
public void comparable_test() {
  Collections.sort(comparablePlayers);
  assertThat(comparablePlayers).isSorted();
}
```

정렬 규칙을 Comparator로 넘겨서도 List를 정렬할 수 있습니다.

```java
@Test
public void comparator_lambda_Test() {
		Comparator<ComparatorPlayer> comparator = (a, b) -> b.getScore() - a.getScore();

		Collections.sort(comparatorPlayers, comparator);

		assertThat(comparatorPlayers).isSortedAccordingTo(comparator);
}
```


### 2.2 Stream의 sorted()로 정렬하기

Stream에서는 sorted() 메서드를 사용해서 정렬할 수 있습니다. sorted() 메서드는 comparator 인터페이스를 구현한 객체를 인자로 받습니다.

```java
Stream<T> sorted(Comparator<? super T> comparator);
```



List를 stream으로 변환해서 sorted() 메서드를 사용해서 정렬한 예제입니다.

```java
@Test
public void stream_comparable_sort() {
		List<ComparablePlayer> sortedPlayers = comparablePlayers.stream()
				.sorted((a, b) -> b.getScore() - a.getScore())
				.collect(Collectors.toList());

		assertThat(sortedPlayers).isSorted();
}
```


정렬 시 객체의 여러 값을 기준으로도 정렬을 할 수 있습니다. Score가 같은 경우 발생 시에는 name 기준으로 정렬하는 예제입니다.

```java
public static int compareByScoreThenName(ComparatorPlayer lhs, ComparatorPlayer rhs) {
		if (lhs.getScore() == rhs.getScore()) {
			return lhs.getName().compareTo(rhs.getName());
		} else {
			return lhs.getScore() - rhs.getScore();
		}
}
```

ComparatorPlayer 객체에 compareByScoreThenName() 메서드가 있어서 method reference로 더 간결하게 작성할 수도 있습니다.

```java
@Test
public void sort_by_score_then_name() {
		List<ComparatorPlayer> sortedPlayers = comparatorPlayers.stream()
				//.sorted((a, b) -> ComparatorPlayer.compareByNameThenScore(a, b))
				.sorted(ComparatorPlayer::compareByScoreThenName)
				.collect(Collectors.toList());

assertThat(sortedPlayers).isSortedAccordingTo(ComparatorPlayer::compareByScoreThenName);
}
```



### 2.3 자바8 Comparators

자바8에서는 comparing() 팩토리 메서드가 추가되어 Comparator를 쉽게 정의하도록 도와줍니다. Comparator.comparing() 메서드는 항목을 비교하는데 사용할 객체의 필드 메서드를 인자로 넘겨주면 일치하는 Comparator 인스턴스를 반환해줍니다. 즉, 비교할 필드 메서드만 제공하면 알아서 Comparator 구현체를 반환해주는 것입니다.

```java
public static <T, U extends Comparable<? super U>> Comparator<T> comparing(
            Function<? super T, ? extends U> keyExtractor)
{
  Objects.requireNonNull(keyExtractor);
  return (Comparator<T> & Serializable)
    (c1, c2) -> keyExtractor.apply(c1).compareTo(keyExtractor.apply(c2));
}
```


sort_by_score_then_name 예제에서 score와 name 두 값을 비교해서 정렬한 것처럼 comparing() 메서드와 thenComparing() 메서드를 사용하면 동일하게 정렬할 수 있습니다. 더 코드가 간결해졌습니다.

```java
@Test
public void thenComparing_test() {
		List<ComparatorPlayer> sortedPlayers = comparatorPlayers.stream()
				.sorted(Comparator.comparing(ComparatorPlayer::getScore)
						.thenComparing(ComparatorPlayer::getName))
				.collect(Collectors.toList());

		assertThat(sortedPlayers).isSortedAccordingTo(ComparatorPlayer::compareByScoreThenName);
}
```


## 참고

* https://www.baeldung.com/java-8-sort-lambda
* https://www.daleseo.com/java-comparable-comparator/
* https://www.baeldung.com/java-comparator-comparable
* https://gmlwjd9405.github.io/2018/09/06/java-comparable-and-comparator.html
* https://www.leveluplunch.com/java/tutorials/007-sort-arraylist-stream-of-objects-in-java8/
* [https://velog.io/@agugu95/Java-%EA%B0%9D%EC%B2%B4-%EC%A0%95%EB%A0%AC%EA%B3%BC-%EB%B9%84%EA%B5%90](https://velog.io/@agugu95/Java-객체-정렬과-비교)
