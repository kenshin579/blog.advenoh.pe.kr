---
title: "Mongodb Collection Cloning하는 방법"
description: "Mongodb Collection Cloning하는 방법"
date: 2022-07-16
update: 2022-07-16
tags:
  - mongo, mongodb, clone, collection, script, 몽고
---

종종 기존의 데이터를 수정하지 않고 테스트를 위해서 기존 collection을 clone을 해서 테스트해보고 싶을 때가 있다. MongoDB 스크립트로 쉽게 clone 하는 방법에 대해서 알아보자

clone 테스트를 위해서 inventory를 생성해서 샘플 데이터를 생성한다.

```javascript
db.inventory.insertMany([
    {item: "journal", qty: 25, tags: ["blank", "red"], size: {h: 14, w: 21, uom: "cm"}},
    {item: "mat", qty: 85, tags: ["gray"], size: {h: 27.9, w: 35.5, uom: "cm"}},
    {item: "mousepad", qty: 25, tags: ["gel", "blue"], size: {h: 19, w: 22.85, uom: "cm"}}
])
```

## 1.db.collection.find().forEach()

`find().forEach()` 는 collection의 데이터를 하나씩 `forEach`로 돌면서 다른 inventory2로 삽입하는 방식이다. 하나씩 처리하기 때문에 느리다는 단점이 있다.

```javascript
db.inventory.find().forEach(
    function(docs){
        db.inventory2.insert(docs);
    })
```

## 2.db.collection.aggregate()

`aggregate`의 `$out operator`를 사용하면 조금 더 빠르게 clone이 가능하다.

### Syntax

```javascript
{ $out: { db: "<output-db>", coll: "<output-collection>" } }
```


```javascript
db.inventory.aggregate([{ $match: {} }, { $out: "inventory3" }])

```

## 참고

- https://www.mongodbmanager.com/clone-mongodb-collection
- https://www.mongodb.com/docs/manual/reference/operator/aggregation/out/
- https://github.com/kenshin579/tutorials-go/blob/master/go-mongo/script/clone_collection.js

  
