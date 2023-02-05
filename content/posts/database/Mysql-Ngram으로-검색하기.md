---
title: 'Ngram으로 검색기능 구현하기'
tags : [mysql, ngram, search, parser, token, DB, database, full-text, 검색]
social_image: /media/cover/cover-mysql.jpeg
date: 2023-02-26
---

# 목차

- Full-Text 기능을 사용하려면?
  - 기본설정 (create table, index, sql query match)
  - Ngram parser
    - ngram parser란? (한국어, 일본, 중국어를 지원)
    - 설정하는 방법
    - ngram이란?
      - token_size

- search mode
  - naturla langauge 
  - boolean mode
- custom stopword을 사용하는 설정
  - a stop word
  	- inverted index 만들때, 검색 키워드에서 포함되지 않는다
    - custom list 만들어 사용하기
- 용어
  - inverted index
  - forwated index


# MySqlDB Full-Text Search 기능

MySQL은 FULLTEXT 검색 기능을 제공합니다. FULLTEXT 검색은 텍스트 기반 데이터를 검색하는데 사용되며, 일반적인 LIKE절과는 달리 더 빠르고 정확한 검색을 제공합니다.

FULLTEXT 인덱스를 사용하면 빠른 검색 결과를 제공할 수 있습니다. 이 인덱스는 MySQL의 일반 인덱스와 달리 MyISAM 엔진에서만 사용할 수 있습니다.

FULLTEXT 검색은 단어 단위로 수행되며, 특수문자나 공백으로 분리된 단어를 사용합니다. 검색어는 일반적으로 불용어(stopword)를 제외한 단어로 구성됩니다.

FULLTEXT 검색은 일반적으로 전체 텍스트를 대상으로 수행됩니다. 하지만, MySQL은 BOOLEAN 검색을 지원하여 AND, OR, NOT 연산자를 사용하여 검색 범위를 제한할 수 있습니다.

FULLTEXT 검색은 대용량의 텍스트 데이터를 검색할 때 매우 유용합니다. 예를 들어, 전자 상거래 웹사이트에서 제품 설명을 검색하는 것과 같은 경우에 사용됩니다.

- MongoDB도 지원하지만, (stemming, fuzzy matching인 지원하지 않아서 직접 구현을 하기도 함)
  - 링크 추가하기
- 직접 구현하려면 다양한 부분을 고려해서해서 간단한 검색은 mysqlDB에서 제공하는 기능을 사용하는게 좋을 듯하다
- 검색에 대한 기능에 고도화 기능이 더 필요한 다시 구현을 다르게... 
- https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html
- 

# Full-Text 사용방법

MySQL에서 full-text을 어떻게 사용하는지 알아보자



## 1.기본 Full

FULLTEXT 검색 기능을 사용하려면 다음과 같은 단계를 따릅니다.

1. FULLTEXT 검색을 수행할 테이블에 MyISAM 스토리지 엔진을 사용합니다. (MyISAM은 FULLTEXT 인덱스를 지원합니다.)
2. 검색 대상이 되는 열에 FULLTEXT 인덱스를 생성합니다.
3. MATCH AGAINST 연산자를 사용하여 FULLTEXT 검색을 수행합니다.

예를 들어, 다음과 같은 샘플 테이블이 있다고 가정해 봅시다.

```mysql
CREATE TABLE products (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  price DECIMAL(10,2)
) ENGINE=MyISAM;

```



이 테이블에 FULLTEXT 인덱스를 생성하려면 다음과 같은 SQL 문을 실행합니다.

```
ALTER TABLE products ADD FULLTEXT (name, description);

```

이제 FULLTEXT 검색을 수행할 수 있습니다. 다음은 `MATCH AGAINST` 연산자를 사용한 FULLTEXT 검색의 예입니다.

```
SELECT * FROM products WHERE MATCH(name, description) AGAINST('apple');

```

이 예제는 `products` 테이블에서 `name` 열과 `description` 열에서 'apple'을 검색합니다. `MATCH AGAINST` 연산자는 FULLTEXT 인덱스에서 검색어를 찾아 일치하는 레코드를 반환합니다.

## 2. Ngram Parser

ngram은 MySQL에서 FULLTEXT 검색의 일종으로, 단어의 일부분이 일치하는 경우도 검색 결과로 반환할 수 있습니다. 예를 들어, 'apple'을 검색할 때 'appl'이나 'ple'과 같은 부분 문자열도 검색 결과로 반환할 수 있습니다.

- Feature
  - 한국어, 중국어, 일본어 지원
  - 

## 2.1 필요한 table, index



```mysql
CREATE TABLE articles
(
    id    INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title VARCHAR(200),
    FULLTEXT INDEX ngram_idx (title) WITH PARSER ngram
) ENGINE = InnoDB
  CHARACTER SET utf8mb4;
```



ngram을 사용하려면 FULLTEXT 검색과 같은 단계를 따릅니다.

1. FULLTEXT 검색을 수행할 테이블에 MyISAM 스토리지 엔진을 사용합니다. (MyISAM은 FULLTEXT 인덱스를 지원합니다.)
2. 검색 대상이 되는 열에 FULLTEXT 인덱스를 생성합니다.
3. ngram 파라미터를 추가하여 FULLTEXT 인덱스를 설정합니다.

예를 들어, 다음과 같은 샘플 테이블이 있다고 가정해 봅시다.

## 2.2 Search mode

### 2.3.1 Natural Language

### 2.3.2 Boolean 

### 2.3.3 Wildcard



## 2.2.사용자정의 Stopwords 목록 설정하기



# 용어

### 1.inverted index
- mapping이 word -> document로 할 수 있는 index
	- ex. book 뒤에 있는 index

### 2.forward index
- mapping document-> word로 mapping 할 수 있는 index
	- ex. content of contents in book, dns lookup

참고

- https://www.codingninjas.com/codestudio/library/difference-between-inverted-index-and-forward-index
- https://www.geeksforgeeks.org/difference-inverted-index-forward-index/

# 참고

- https://gongzza.github.io/database/mysql-fulltext-search/
- https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html
- https://www.mysqltutorial.org/mysql-ngram-full-text-parser/
- https://gywn.net/2017/04/mysql_57-ngram-ft-se/
- https://chat.openai.com/chat
