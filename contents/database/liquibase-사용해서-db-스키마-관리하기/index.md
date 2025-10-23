---
title: "Liquibase 사용해서 DB 스키마 관리하기"
description: "Liquibase 사용해서 DB 스키마 관리하기"
date: 2024-09-20
update: 2024-09-20
tags:
  - Liquibase
  - Flyaway
  - rollback
  - migration
  - 롤백
  - 마이그레이션
  - SQL
  - MySQL
  - changelog
  - changeset
  - tag
  - docker
  - 도커
  - context
  - label
---

## 1. 개요

> 같이 일하는 동료분께서 현재 개발중인 프로젝트에 적용해주셔서 스터디 차원에서 정리해본다

`Liquibase`는 데이터베이스 변경을 추적하고 관리할 수 있도록 도와주는 오픈 소스 도구이다. 이 도구는 데이터베이스 스키마 변경을 기록하고, 이를 애플리케이션 배포와 연계하여 일관성을 유지하는 데 사용된다. `Liquibase`는 여러 팀이 협력해 일관된 방식으로 데이터베이스를 관리하는 데 유리하며, 코드 버전 관리를 하듯 데이터베이스의 상태를 관리할 수 있는 강력한 기능을 제공한다.

특히 `Liquibase`는 데이터베이스 마이그레이션 툴로서, 다양한 방식으로 데이터베이스 변경 사항을 기록하고 롤백할 수 있게 해준다. `Liquibase`의 기본 동작 원리는 변경 사항을 정의한 파일(`Changelog`)과 이를 실행할 환경(DB) 간의 동기화를 유지하는 것이다.

### 1.1 주요기능

- 자동 마이그레이션
  - `Liquibase`는 변경 사항을 자동으로 적용하며, 데이터베이스 상태를 자동으로 업데이트한다
- 롤백 기능
  - 잘못된 변경 사항을 되돌리기 위한 롤백 기능을 제공한다 - 유료 버전에서만 가능
  - 무료 버전은 사용자가 직접 롤백 스크립트를 작성해줘야 한다. 우리에게 챗GPT가 있어서 괜찮을 듯하다
- 다양한 형식 지원
  - `XML`, `SQL`, `YAML`, `JSON` 등 다양한 포맷으로 데이터베이스 변경 사항을 관리할 수 있다
- 데이터베이스 무관성
  - `Liquibase`는 다양한 데이터베이스 시스템(`MySQL`, `PostgreSQL`, `Oracle`, `SQL Server` 등)을 지원하여 여러 데이터베이스에 동일한 변경 사항을 적용할 수 있다
- 데이터베이스 변경 이력 추적
  - `Liquibase`는 언제, 누가, 어떤 변경을 적용했는 지 추적할 수 있다

### 1.2 기본 개념

`Liquibase`는 데이터베이스 변경 관리를 위한 핵심 개념으로 다음의 요소들을 사용한다.

#### 1.2.1 용어

1. `Changelog`
   - 여러 개의 `changeset`을 모아 놓은 파일로 데이터베이스의 스키마 변경 내역을 관리하는 `XML`, `YAML`, `JSON` 또는 `SQL` 파일이다
   - 데이터베이스 변경 내역을 기록하고, 각 `changeset`이 언제 적용되었는지 추적한다
2. `Changeset`
   - 데이터베이스에 적용할 특정 변경 사항(단위 작업)을 기술한 블록이다
   - 데이터베이스에 적용할 하나의 변경 작업을 설명하고, 각 `changeset`에는 고유의 ID, author, 그리고 해당 변경 사항이 들어있다
   - ex. 테이블 추가, 컬럼 수정, 인덱스 추가 등
3. `Changetype`
   - 각 `changeset` 내에서 실행할 구체적인 데이터베이스 변경 작업의 유형이다
   - 데이터베이스의 스키마나 데이터에 적용할 변경 사항의 유형을 정의한다
   - ex. `createTable`, `addColumn`, `dropColumn`, `insert` 등

#### 1.2.2 기본 동작 원리

`Liquibase`를 사용해서 SQL를 관리하는 기본 동작은 다음과 같다.

1. `Changelog`, `Changeset` 파일을 작성하기
   - 데이터베이스 스키마 변경 내용을 기록한 `Changelog` 파일을 작성한다. 이 파일에는 데이터베이스에 반영할 `Changeset`이 포함된다
2. Liquibase CLI로 DB에 적용하기
   - `liquibase update` 명령을 사용해 작성된 `Changeset`을 데이터베이스에 적용한다. `Liquibase`는 먼저 데이터베이스의 `DATABASECHANGELOG` 테이블을 확인하여 이미 적용된 Changeset을 파악하고, 새로운 Changeset만을 실행한다
   - `Changeset`이 성공적으로 실행되면, `Liquibase`는 그 기록을 `DATABASECHANGELOG` 테이블에 저장한다. 이를 통해 이미 적용된 `Changeset`을 다시 실행하지 않도록 방지한다
3. Rollback의 경우
   - 잘못된 변경 사항을 되돌릴 때는 `rollback` 명령을 사용하여 데이터베이스를 특정 시점의 상태로 복구할 수 있다

![](image-20240920182800486.png)

## 2. Liquibase CLI 설치

### 2.1 CLI 설치

> 설치는 맥 기준으로 설명한다

Homebrew를 사용하여 `Liquibase`를 간편하게 설치한다.

```bash
> brew install liquibase
```

### 2.2 실습을 위해 MySQL 도커 실행

실습을 위해 MySQL 도커를 실행하고 데이터베이스를 생성한다.

```bash
> cd cloud/docker/mysql
make mysql-create
```

DB 서버에 로그인을 해서 아래 데이터베이스를 생성한다.

```sql
> create database liquibase_quickstart;
```

# 3. Liquibase 기본 사용 방법

`Liquibase`를 사용하려면 아래 단계로 진행하면 된다.

- liquibase.properties 파일을 생성해서 DB 접속 정보를 입력한다
- `Changelog`  파일을 생성한다
- Liquibase CLI 명령어로 DB에 `Changelog`를 적용한다

### 3.1 프로젝트 생성하기

#### 3.1.1 (옵션) init project 명령어 생성하기

`init project` 명령어는 `Liquibase`의 샘플 파일을 생성해 주는데, 유료 버전에서 사용할 수 있는 파일도 있고 그래서 굳이 이 명령어를 사용할 필요는 없다. 어떤 명령어인지 스터디 차원에서 추가한다.

```bash
mkdir quickstart
❯ cd quickstart
> liquibase init project
...생략...
Setup new liquibase.properties, flowfile, and sample changelog? Enter (Y)es with defaults, yes with (C)ustomization, or (N)o. [Y]: 
c
Enter a relative path to desired project directory [./]: 

Enter name for sample changelog file to be created or (s)kip [example-changelog]: 

Enter your preferred changelog format (options: sql, xml, json, yml, yaml) [sql]: 

Enter name for defaults file to be created or (s)kip [liquibase.properties]: 

Enter the JDBC url without username or password to be used (What is a JDBC url? <url>) [jdbc:h2:tcp://localhost:9090/mem:dev]: 
jdbc:mysql://localhost:3306/liquibase_quickstart
Enter username to connect to JDBC url [dbuser]: 
root
Enter password to connect to JDBC url [letmein]: 
go-mysql
Setting up new Liquibase project in '/Users/user/GolandProjects/tutorials-go/liquibase/quickstart/.'...

Created example changelog file '/Users/user/GolandProjects/tutorials-go/liquibase/quickstart/example-changelog.sql'
Created example defaults file '/Users/user/GolandProjects/tutorials-go/liquibase/quickstart/liquibase.properties'
Created example flow file '/Users/user/GolandProjects/tutorials-go/liquibase/quickstart/liquibase.advanced.flowfile.yaml'
Created example flow file '/Users/user/GolandProjects/tutorials-go/liquibase/quickstart/liquibase.flowvariables.yaml'
Created example flow file '/Users/user/GolandProjects/tutorials-go/liquibase/quickstart/liquibase.endstage.flow'
Created example flow file '/Users/user/GolandProjects/tutorials-go/liquibase/quickstart/liquibase.flowfile.yaml'
Created example checks package '/Users/user/GolandProjects/tutorials-go/liquibase/quickstart/liquibase.checks-package.yaml'

To use the new project files make sure your database is active and accessible and run "liquibase update".
For more details, visit the Getting Started Guide at <https://docs.liquibase.com/start/home.html>
Liquibase command 'init project' was executed successfully.
```

#### 3.1.2 수동으로 생성하기

`Liquibase` 프로젝트의 디렉토리 구조는 아래와 같이 구성할 수 있다. `Liquibase` 프로젝트 구성에 대한 내용은 [Design Your LIquibase Project](https://docs.liquibase.com/start/design-liquibase-project.html)를 참고해 주세요.

```bash
❯ tree .
.
├── db
│   └── changelog
│       ├── 1_init.sql
│       └── changelog.yaml
├── liquibase.properties
```

### 3.2 Liquibase 설정하기

`Liquibase`를 사용하기 위해서는 데이터베이스와 연결할 수 있도록 설정 파일을 작성해야 한다. `liquibase.properties` 파일을 생성하고 아래와 같이 설정한다.

```bash
changeLogFile=changelog.yaml
liquibase.command.url=jdbc:mysql://localhost:3306/liquibase_quickstart
liquibase.command.username=root
liquibase.command.password=password
classpath=lib/mysql-connector-j-8.0.33.jar
```

> mysql connector jar 파일은 [[mysql.com](http://mysql.com)](http://mysql.comhttps://downloads.mysql.com/archives/c-j/) 사이트에서 다운로드할 수 있다

## 3.3 SQL Changelog 생성하기

`Liquibase`에서는 Changelog 파일을 작성하여 데이터베이스의 변경 사항을 기록한다. `Changelog`의 형식은 각기 다른 데이터베이스에서 구애받지 않기 위해 `SQL`, `XML`, `JSON`, `YAML`로 구성할 수 있다. 여기서는 `Changelog`는 `yaml`로 작성하고 `Changeset`은 개발자에게 익숙한 SQL 구문으로 작성한다.

```yaml
databaseChangeLog:
  - include:
      file: db/changelog/1_init.sql
--liquibase formatted sql

--changeset your.name:1 labels:example-label context:example-context
--comment: example comment
create table person
(
    id       int primary key auto_increment not null,
    name     varchar(50)                    not null,
    address1 varchar(50),
    address2 varchar(50),
    city     varchar(30)
);
--rollback DROP TABLE person;
```

이 `Changeset`은 formatted SQL 방식을 따르고 있으며, 아래와 같은 세부 사항들을 포함하고 있다.

- `--liquibase formatted sql`
  - 이 주석은 파일이 Liquibase의 formatted SQL 파일임을 명시한다. 모든 Liquibase formatted SQL 파일은 이 주석으로 시작해야 한다
  
- `--changeset your.name:1 labels:example-label context:example-context`
  - `your.name`는 Changeset 작성자의 이름이고 `1`은 Changeset의 고유 ID이다. 프로젝트 내에서 동일한 작성자 이름과 ID의 조합이 유일해야 한다
  - `labels`: 특정 레이블을 사용하여 Changeset을 필터링할 수 있다 ex. `example-label`이라는 레이블을 사용하면 나중에 특정 레이블이 붙은 Changeset만 실행할 수 있다
  - `context`: Changeset이 실행되는 특정 컨텍스트를 정의한다 여기서는 `example-context`로 정의되었으며, 해당 컨텍스트에서만 Changeset이 실행된다
  
- `--comment: example comment`
  - Changeset에 대한 설명을 추가할 수 있는 주석이다. 이 예시에서는 단순한 설명인 `example comment`가 포함되어 있다
  
- `--rollback DROP TABLE person;`
  - 이 주석은 Changeset을 롤백할 때 실행할 SQL 구문을 정의한다

참고

- [Example Changelogs: SQL Format](https://docs.liquibase.com/concepts/changelogs/sql-format.html)

### 3.4 Changelog를 DB에 적용하기

작성한 `Changelog`를 DB에 적용하려면, `Liquibase` 명령어를 실행하면 된다. 이때 도커를 사용하거나, `Liquibase` 명령어를 직접 실행할 수 있다.

#### 3.4.1 Liquibase 명령어로 실행하기

```sql
❯ liquibase --defaultsFile=liquibase.properties update
...생략...
Running Changeset: db/changelog/1_init.sql::1::your.name

UPDATE SUMMARY
Run:                          1
Previously run:               0
Filtered out:                 0
-------------------------------
Total change sets:            1

Liquibase: Update has been successful. Rows affected: 1
Liquibase command 'update' was executed successfully.
```

`update` 명령어를 실행하면 설정 파일에서 지정된 `Changelog` 파일을 참조하여 아직 적용되지 않은 변경 사항인(`Changeset`)을 데이터베이스에 적용한다. 처음 실행하게 되면 Liquibase 관련 테이블도 같이 생성된 것을 확인할 수 있다.

![](image-20240920182833879.png)

#### 3.4.2 Liquibase 명령어 도커로 실행하기

도커로 실행하면 별도의 설치 과정 없이 손쉽게 `Liquibase`를 실행할 수 있지만, 몇 가지 주의 사항이 필요하다.

- 도커 환경에서 `Liquibase`를 실행하려면 MySQL과 `Liquibase` 컨테이너가 서로 통신할 수 있도록 설정해야한다

```yaml
# 도커 네트워크 생성하기
> docker network create mysql-network

# mysql 컨테이너를 생성한 네트워크에 연결한다
> docker network connect mysql-network go-mysql
```

위 과정을 통해 MySQL 컨테이너(`go-mysql`)와 `Liquibase` 컨테이너가 같은 네트워크에서 통신할 수 있게 된다.

- [liquibase.properties](http://liquibase.properties) 파일에서 MySQL 주소를 설정이 필요하다

도커 컨테이너 내에서 `localhost`는 각 컨테이너 자신을 의미한다. 따라서 MySQL이 실행 중인 컨테이너에 접근하려면 MySQL 컨테이너의 이름을 주소로 지정해 줘야 한다. ex. `go-mysql`

```yaml
liquibase.command.url=jdbc:mysql://go-mysql:3306/liquibase_quickstart
```

아래 명령어로 Liquibase를 도커로 실행하면 된다.

```bash
> docker run --rm --network mysql-network \\
  -v $(pwd):/liquibase/changelog \\
  -e INSTALL_MYSQL=true \\
  liquibase/liquibase \\
  --log-level=info \\
  --defaultsFile=/liquibase/changelog/liquibase.docker.properties update
```

- `--rm`: 컨테이너 실행 후 자동으로 삭제한다
- `--network mysql-network`: 앞에서 생성한 `mysql-network` 네트워크를 사용하여 MySQL과 Liquibase가 통신할 수 있도록 설정한다
- `-v $(pwd):/liquibase/changelog`: 현재 디렉토리(`$(pwd)`)를 도커 컨테이너 내의 `/liquibase/changelog` 경로에 마운트한다
- `-e INSTALL_MYSQL=true`: MySQL JDBC 드라이버를 컨테이너 내에 설치한다
- `--defaultsFile`: Liquibase 설정 파일(`liquibase.docker.properties`)을 지정한다
- `update`: 변경사항을 데이터베이스에 적용하는 Liquibase 명령어이다

## 4. Liquibase 명령어

`Liquibase`는 아래처럼 다양한 명령어를 제공한다. 자주 사용할 것 같은 명령어 위주로 정리한다. 더 자세한 내용은 Liquibase Commands를 참고해 주세요.

### 4.1 Update 명령어

`Liquibase`의 `update` 명령어는 변경 사항을 데이터베이스에 적용하는 기본 명령이다. 하지만 다양한 상황에 맞춰 `update` 명령어에는 몇 가지 유용한 변형이 있다.

- `update-sql` : 실제로 데이터베이스에 변경을 적용하지 않고, 변경 사항을 SQL 파일로 출력한다. 이 명령어를 통해 변경 사항을 미리 검토하거나 수동으로 적용할 수 있다

```bash
> liquibase --defaultsFile=liquibase.properties update-sql
...생략...
--  Lock Database
UPDATE liquibase_quickstart.DATABASECHANGELOGLOCK SET `LOCKED` = 1, LOCKEDBY = 'MacBook-Pro-1647.local (172.30.1.5)', LOCKGRANTED = NOW() WHERE ID = 1 AND `LOCKED` = 0;

--  *********************************************************************
--  Update Database Script
--  *********************************************************************
--  Change Log: db/changelog/changelog.yaml
--  Ran at: 24. 9. 20. 오후 2:54
--  Against: root@172.17.0.1@jdbc:mysql://localhost:3306/liquibase_quickstart
--  Liquibase version: 4.29.1
--  *********************************************************************

--  Changeset db/changelog/2_insert.sql::2::your.name
INSERT INTO liquibase_quickstart.person (id, name, address1, address2, city) VALUES (1, 'John Doe', '123 Main St', 'Apt 1', 'Beverly Hills');

INSERT INTO liquibase_quickstart.DATABASECHANGELOG (ID, AUTHOR, FILENAME, DATEEXECUTED, ORDEREXECUTED, MD5SUM, `DESCRIPTION`, COMMENTS, EXECTYPE, CONTEXTS, LABELS, LIQUIBASE, DEPLOYMENT_ID) VALUES ('2', 'your.name', 'db/changelog/2_insert.sql', NOW(), 2, '9:ac8dc4edceb0733373ac291b4a1bf9be', 'sql', '', 'EXECUTED', NULL, NULL, '4.29.1', '6811656895');

--  Release Database Lock
UPDATE liquibase_quickstart.DATABASECHANGELOGLOCK SET `LOCKED` = 0, LOCKEDBY = NULL, LOCKGRANTED = NULL WHERE ID = 1;

Liquibase command 'update-sql' was executed successfully.
```

- `update-count-sql`: 특정 개수의 `Changeset`을 SQL 파일로 출력하여 데이터베이스에 직접 적용하지 않고 검토할 수 있다

```bash
> liquibase --defaultsFile=liquibase.properties update-count-sql 2
```

- `update-count` : `Changelog` 파일에서 지정된 개수만큼의 변경사항(`Changeset`)을 데이터베이스에 적용한다. 이 명령어는 부분적으로 변경을 적용할 때 유용하다

```bash
> liquibase --defaultsFile=liquibase.properties update-count 2
```

### 4.2 Rollback 명령어

`Liquibase`의 `rollback` 명령어는 데이터베이스의 변경 사항을 이전 상태로 되돌릴 수 있는 기능을 제공한다. 특정 조건에 맞춰 다양한 방식으로 롤백을 수행할 수 있다.

- `rollback` : 특정 조건(태그, 날짜 등)까지의 모든 `Changeset`을 롤백한다. 이를 통해 데이터베이스를 지정된 이전 상태로 복원할 수 있다

```bash
> liquibase --defaultsFile=liquibase.properties rollback --tag v1.0
```

- `rollback-sql` : 실제 롤백을 수행하지 않고, 롤백에 필요한 SQL 스크립트를 출력해줘서 미리 변경 사항을 검토할 수 있어 자주 사용하게 된다


```bash
> liquibase --defaultsFile=liquibase.properties rollback-sql v1.0
...생략...
--  Lock Database
UPDATE liquibase_quickstart.DATABASECHANGELOGLOCK SET `LOCKED` = 1, LOCKEDBY = 'MacBook-Pro-1647.local (172.30.1.5)', LOCKGRANTED = NOW() WHERE ID = 1 AND `LOCKED` = 0;

--  *********************************************************************
--  Rollback to 'v1.0' Script
--  *********************************************************************
--  Change Log: db/changelog/changelog.yaml
--  Ran at: 24. 9. 20. 오후 6:07
--  Against: root@172.17.0.1@jdbc:mysql://localhost:3306/liquibase_quickstart
--  Liquibase version: 4.29.1
--  *********************************************************************

--  Rolling Back ChangeSet: db/changelog/3_update.sql::3::your.name
ALTER TABLE liquibase_quickstart.person DROP COLUMN zip;

DELETE FROM liquibase_quickstart.DATABASECHANGELOG WHERE ID = '3' AND AUTHOR = 'your.name' AND FILENAME = 'db/changelog/3_update.sql';

--  Rolling Back ChangeSet: db/changelog/2_insert.sql::2::your.name
DELETE FROM liquibase_quickstart.person WHERE id = 1;

DELETE FROM liquibase_quickstart.DATABASECHANGELOG WHERE ID = '2' AND AUTHOR = 'your.name' AND FILENAME = 'db/changelog/2_insert.sql';

--  Release Database Lock
UPDATE liquibase_quickstart.DATABASECHANGELOGLOCK SET `LOCKED` = 0, LOCKEDBY = NULL, LOCKGRANTED = NULL WHERE ID = 1;

Liquibase command 'rollback-sql' was executed successfully.
```

- `rollbackCount` : 지정한 개수의 `Changeset`을 롤백한다

```bash
> liquibase --defaultsFile=liquibase.properties rollbackCount 1
...생략...
Rolling Back Changeset: db/changelog/3_update.sql::3::your.name
Liquibase command 'rollbackCount' was executed successfully.
```

### 4.3 Database Inspection 명령어

데이터베이스의 현재 상태를 확인하거나 비교할 때 사용하는 명령어이다.

- `diff` : 실제 서버의 DB 상태와 적용하려는 `Changelog`를 비교할 때 사용하면 좋다. 실제로 서버에 새로운 `Changelog`를 반영하기 전에 서버와 차이가 있는지 미리 확인하는 게 좋다

```bash
# 테스트를 위해 임의로 liquibase_quickstart_ref.person 테이블에 새로운 열을 추가한다
sql> alter table person
    add address3 varchar(30) null comment 'test' after address2;

# 두 데이터베이스와 비교
> liquibase --defaultsFile=liquibase.properties \\
	--referenceUrl=jdbc:mysql://localhost:3306/liquibase_quickstart_ref \\
	--referenceUsername=root \\
	--referencePassword=password \\
	diff
...생략...
	Diff Results:
Reference Database: root@172.17.0.1 @ jdbc:mysql://localhost:3306/liquibase_quickstart_ref (Default Schema: liquibase_quickstart_ref)
Comparison Database: root@172.17.0.1 @ jdbc:mysql://localhost:3306/liquibase_quickstart (Default Schema: liquibase_quickstart)
Compared Schemas: liquibase_quickstart_ref -> liquibase_quickstart
Product Name: EQUAL
Product Version: EQUAL
Missing Catalog(s): NONE
Unexpected Catalog(s): NONE
Changed Catalog(s): NONE
Missing Column(s): 
     liquibase_quickstart_ref.person.address3
Unexpected Column(s): NONE
Changed Column(s): 
     liquibase_quickstart_ref.person.city
          order changed from '6' to '5'
Missing Foreign Key(s): NONE
Unexpected Foreign Key(s): NONE
Changed Foreign Key(s): NONE
Missing Index(s): NONE
Unexpected Index(s): NONE
Changed Index(s): NONE
Missing Primary Key(s): NONE
Unexpected Primary Key(s): NONE
Changed Primary Key(s): NONE
Missing Table(s): NONE
Unexpected Table(s): NONE
Changed Table(s): NONE
Missing Unique Constraint(s): NONE
Unexpected Unique Constraint(s): NONE
Changed Unique Constraint(s): NONE
Missing View(s): NONE
Unexpected View(s): NONE
Changed View(s): NONE
Liquibase command 'diff' was executed successfully.
```

- `diff-changelog` : 두 데이터베이스 간의 차이점에 대한 `Changelog` 파일을 생성한다

```bash
> liquibase --defaultsFile=liquibase.properties \\
	--changeLogFile=changelog.mysql.sql \\
	--referenceUrl=jdbc:mysql://localhost:3306/liquibase_quickstart_ref \\
	--referenceUsername=root \\
	--referencePassword=password \\
	diff-changelog
...생략...
BEST PRACTICE: The changelog generated by diffChangeLog/generateChangeLog should be inspected for correctness and completeness before being deployed. Some database objects and their dependencies cannot be represented automatically, and they may need to be manually updated before being deployed.
Liquibase command 'diff-changelog' was executed successfully.
```

`Liquibase`가 생성한 `changelog.mysql.sql` 파일을 확인하면 아래와 같이 잘 생성해준다.

```bash
...생략...
-- liquibase formatted sql

-- changeset user:1726817103402-1
ALTER TABLE person
    ADD address3 VARCHAR(30) NULL COMMENT 'test';
```

### 4.4 Change Tracking 명령어

`Liquibase`의 Change Tracking 명령어는 데이터베이스에 적용된 변경 사항을 추적하고, 현재 상태를 확인하거나 변경 사항 기록을 생성하는 데 사용된다.

- `history` : 이 명령어로 어떤 변경이 언제 적용되었는지 추적할 수 있다

```bash
> liquibase --defaultsFile=liquibase.properties history
...생략...
Liquibase History for jdbc:mysql://localhost:3306/liquibase_quickstart

+---------------+--------------------+-------------------------+------------------+--------------+------+
| Deployment ID | Update Date        | Changelog Path          | Changeset Author | Changeset ID | Tag  |
+---------------+--------------------+-------------------------+------------------+--------------+------+
| 6731865868    | 24. 9. 19. 오전 7:44 | db/changelog/1_init.sql | your.name        | 1            | v1.0 |
+---------------+--------------------+-------------------------+------------------+--------------+------+

Liquibase command 'history' was executed successfully.
```

- `status` : 데이터베이스에 적용되지 않은 `Changeset`이 있는지 확인할 수 있다

```bash
> liquibase --defaultsFile=liquibase.properties status
...생략...
2 changesets have not been applied to root@172.17.0.1@jdbc:mysql://localhost:3306/liquibase_quickstart
     db/changelog/2_insert.sql::2::your.name
     db/changelog/3_update.sql::3::your.name
Liquibase command 'status' was executed successfully.
```

- `generate-changelog` : 현재 데이터베이스의 스키마 상태를 기반으로 새로운 `Changelog` 파일을 생성해준다. 처음 `Liquibase`로 전환을 할때 사용하면 좋다
  - 생성하는 포맷의 결정은 파일 이름으로 결정이 된다. yaml로 생성하고 싶으면 `--changeLogFile=changelog.yaml` 로 변경해서 실행하면 된다

```bash
> liquibase --defaultsFile=liquibase.properties \\
	--changeLogFile=changelog.mysql.sql \\
	generate-changelog

BEST PRACTICE: The changelog generated by diffChangeLog/generateChangeLog should be inspected for correctness and completeness before being deployed. Some database objects and their dependencies cannot be represented automatically, and they may need to be manually updated before being deployed.

BEST PRACTICE: When generating formatted SQL changelogs, always check if the 'splitStatements' attribute
works for your environment. See <https://docs.liquibase.com/commands/inspection/generate-changelog.html> for more information. 

Generated changelog written to changelog.mysql.sql
Liquibase command 'generate-changelog' was executed successfully.
```

### 4.5 Utility 명령어

`Liquibase`는 데이터베이스 상태를 관리하고 변경 사항을 추적할 수 있는 유틸리티 명령어를 제공한다.

- `tag` : 현재 데이터베이스 상태에 태그를 지정하여 나중에 해당 시점으로 롤백할 수 있다. 특정 배포나 중요한 변경 시점에 태그를 설정한다

```bash
> liquibase --defaultsFile=liquibase.properties tag v1.0
```

- `validate` :  `changelog` 파일의 구조나 구문 오류를 확인하여 변경 사항을 적용하기 전에 문제가 있는지 검증한다. 유효성 검사를 통해 잘못된 `Changeset`이 적용되는 것을 방지할 수 있다

```bash
> liquibase --defaultsFile=liquibase.properties validate
...생략...
No validation errors found.
Liquibase command 'validate' was executed successfully.
```

- `changelog-sync` : changelog 파일과 Liquibase의 테이블 상태를 수동으로 동기화 하기 위해 사용된다. 이미 적용된 `Changeset`을 데이터베이스에 기록하지만, 실제로 `Changelog`의 변경사항을 적용하지 않는다

```bash
> liquibase --defaultsFile=liquibase.properties changelog-sync
```

- `changelog-sync-sql` : `changelog-sync` 명령어와 동일한 기능을 수행하지만, 실제 동기화 작업을 실행하지 않고 그에 해당하는 SQL 문을 출력한다. 이를 통해 SQL을 미리 검토하거나 수동으로 실행할 수 있다

```bash
> liquibase --defaultsFile=liquibase.properties changelog-sync-sql
...생략...
--  Lock Database
UPDATE liquibase_quickstart.DATABASECHANGELOGLOCK SET `LOCKED` = 1, LOCKEDBY = 'MacBook-Pro-1647.local (172.30.1.5)', LOCKGRANTED = NOW() WHERE ID = 1 AND `LOCKED` = 0;

--  *********************************************************************
--  SQL to add all changesets to database history table
--  *********************************************************************
--  Change Log: db/changelog/changelog.yaml
--  Ran at: 24. 9. 20. 오후 4:17
--  Against: root@172.17.0.1@jdbc:mysql://localhost:3306/liquibase_quickstart
--  Liquibase version: 4.29.1
--  *********************************************************************

INSERT INTO liquibase_quickstart.DATABASECHANGELOG (ID, AUTHOR, FILENAME, DATEEXECUTED, ORDEREXECUTED, MD5SUM, `DESCRIPTION`, COMMENTS, EXECTYPE, CONTEXTS, LABELS, LIQUIBASE, DEPLOYMENT_ID) VALUES ('2', 'your.name', 'db/changelog/2_insert.sql', NOW(), 2, '9:ac8dc4edceb0733373ac291b4a1bf9be', 'sql', '', 'EXECUTED', NULL, NULL, '4.29.1', '6816665001');

INSERT INTO liquibase_quickstart.DATABASECHANGELOG (ID, AUTHOR, FILENAME, DATEEXECUTED, ORDEREXECUTED, MD5SUM, `DESCRIPTION`, COMMENTS, EXECTYPE, CONTEXTS, LABELS, LIQUIBASE, DEPLOYMENT_ID) VALUES ('3', 'your.name', 'db/changelog/3_update.sql', NOW(), 3, '9:5ce7a1f50046b2f71d0696d52d6e7c1c', 'sql', '', 'EXECUTED', NULL, NULL, '4.29.1', '6816665001');

--  Release Database Lock
UPDATE liquibase_quickstart.DATABASECHANGELOGLOCK SET `LOCKED` = 0, LOCKEDBY = NULL, LOCKGRANTED = NULL WHERE ID = 1;

Liquibase command 'changelog-sync-sql' was executed successfully.
```

## 5. FAQ

#### 1. `context` vs `label`의 차이점은?

`Context`와 `Label`은 `Liquibase`에서 특정 `Changeset`을 적용할 환경이나 조건을 정의하는 기능이지만, 용도가 약간 다르다.

- `Context` :  `Changeset`을 특정 환경(개발, 테스트, 프로덕션 등)에 맞춰 적용할 때 사용된다. ex. `--contexts=dev`로 지정하면 해당 `Changeset`이 dev 환경에서만 실행된다

```sql
--changeset author:1 context:dev
CREATE TABLE example_dev (id INT PRIMARY KEY);
# dev 환경 context로 정의된 부분만 실행이 된다
> liquibase --defaultsFile=liquibase.properties --contexts=dev update
```

- `Label` : `Changeset`을 태그처럼 구분하여 특정 조건에 맞춰 실행할 때 사용된다. 여러 개의 `Changeset`을 논리적으로 그룹화하여 "이 변경사항은 A 기능에 관련된 것"처럼 추적하거나 선택적으로 실행할 수 있다. `--labels=pre` 로 특정 레이블을 가진 `Changeset`만 실행할 수 있다.
- SQL 전후처리가 필요한 경우에는 `Label`을 사용할 수 있다

```sql
--changeset author:1 labels:pre
CREATE TABLE example_feature (id INT PRIMARY KEY);
```

> 정리하면 `Context`는 주로 배포 환경에 맞춘 `Changeset` 실행을 제어하는 반면, `Label`은 논리적 그룹화나 추적 목적으로 사용된다

#### 2. rollback 단위는 어떻게 되는 건가?

- changeset 안에 여러 rollback 명령어가 있지만, rollback 실행은 changeset 단위로 실행이 되어서 아래 rollback 명령어 전체가 실행된다고 보면 된다

```sql
--liquibase formatted sql
--changeset your.name:4
create table employee
(
    id       int primary key auto_increment not null,
    name     varchar(50) not null,
    address1 varchar(50),
    address2 varchar(50),
    city     varchar(30)
);

INSERT INTO liquibase_quickstart.employee (id, name, address1, address2, city)
VALUES (1, 'John Doe', '123 Main St', 'Apt 1', 'Beverly Hills');

INSERT INTO liquibase_quickstart.employee (id, name, address1, address2, city)
VALUES (2, 'John Doe2', '123 Main St', 'Apt 1', 'Beverly Hills');

ALTER TABLE liquibase_quickstart.employee ADD COLUMN email VARCHAR(50);

UPDATE liquibase_quickstart.employee SET email = 'user1@naver.com' WHERE id = 1;
UPDATE liquibase_quickstart.employee SET email = 'user2@naver.com' WHERE id = 2;


--comment rollback 실행하면 아래 전체가 한번에 실행이 된다. rollback 하는 단위는 changeset 단위로 되는 듯하다
--rollback UPDATE liquibase_quickstart.employee SET email = NULL WHERE id = 2;
--rollback UPDATE liquibase_quickstart.employee SET email = NULL WHERE id = 1;
--rollback ALTER TABLE liquibase_quickstart.employee DROP COLUMN email;
--rollback DELETE FROM liquibase_quickstart.employee WHERE id = 2;
--rollback DELETE FROM liquibase_quickstart.employee WHERE id = 1;
--rollback DROP TABLE employee;

```







## 6. 마무리

`Liquibase`는 다양한 환경에서 안전하고 효율적으로 데이터베이스 변경을 관리할 수 있는 강력한 도구이다. `Context`와 `Label`을 사용해 환경별 맞춤 실행을 제어하고, `rollback`을 통해 실수나 변경사항을 쉽게 되돌릴 수 있다. 또한, Docker를 통해 쉽게 설정 및 실행할 수 있어 개발자에게 편리한 옵션을 제공한다.

실제 환경에 적용할 때는 주로 아래와 같은 명령어를 주로 사용해서 적용하게 된다.

- `validate`: `Changelog`의 유효성을 검사하여 오류를 사전에 방지한다
- `diff`: 두 데이터베이스 간의 스키마 차이를 비교해볼 수 있다
- `update`: 변경사항을 데이터베이스에 적용한다
- `rollback` : rollback 스크립트가 동작하는지 확인하기 위해 롤백도 실행해보는 걸 추천한다. 미리 잘 못 작성된 스크립트도 확인할 수 있어서 꼭 rollback도 테스트해야 한다

`Liquibase` 를 통해서 SQL schema도 코드와 같이 리뷰도 가능하고 환경 별로 직접 DB에 수동으로 SQL을 실행하는 경우로 인해서 DB 스키마가 조금씩 달라지고 관리가 안 되는 이슈들이 있었는데, `Liquibase` 활용하여 DB 관리가 간편해져서 좋다.

## 7. 참고

- [Liquibase Documentation](https://docs.liquibase.com/home.html)
- [Liquibase에 대해 자세히 알아보기: DB 스키마 버전 관리의 핵심 도구](https://velog.io/@gun_123/Liquibase에-대해-자세히-알아보기-DB-스키마-버전-관리의-핵심-도구)
- [데이터 베이스 형상관리(Migration)툴 비교 Flyway vs Liquibase](https://velog.io/@kjy0302014/데이터-베이스-형상관리Migration툴-비교)
