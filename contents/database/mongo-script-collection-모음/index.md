---
title: "Mongo Script Collection 모음"
description: "Mongo Script Collection 모음"
date: 2023-02-25
update: 2023-02-25
tags:
  - mongo
  - script
  - mongodb
  - 몽고
  - 스크립트
---

개발 시 mongoDB를 주 데이터베이스로 사용하면 데이터 마이그레이션을 자주 하게 되는데, MYSQL보다는 덜 익숙한 면도 있어서 종종 하게 되는 migration을 매번 구글링하게 되어 정리 차원에서 블로그에 적어둔다.

실습 전에 간단하게 inventory collection에 데이터를 입력한다.

```javascript
db.inventory.insertMany([
    {item: "journal", qty: 25, tags: ["blank", "red"], size: {h: 14, w: 21, uom: "cm"}},
    {item: "mat", qty: 85, tags: ["gray"], size: {h: 27.9, w: 35.5, uom: "cm"}},
    {item: "mousepad", qty: 25, tags: ["gel", "blue"], size: {h: 19, w: 22.85, uom: "cm"}}
])
```

## 1.item의 key 이름을 변경

inventory list의 item의 key 이름은 `$rename` operator를 사용한다. 아래 예제에서는 `item` -> `item_id`로 이름을 변경한다.

```javascript
db.inventory.updateMany({}, {$rename: {"item": "item_id"}}, false, true)
```


## 2. 매칭이 item의 특정 값을 업데이트

SQL에서 where와 같이 `$eq` operator로 특정 값이 매칭되는 item을 선택해서 값을 `$se`t operator로 변경한다.

```javascript
db.inventory.updateMany(
    {"item_id": {$eq: "journal"}},
    {
        $set: {"item_id": "11111"}
    }
)
```

## 참고

- https://blog.kevinchisholm.com/javascript/mongodb/getting-started-with-mongo-shell-scripting-basic-crud-operations/

- https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne

  

  
