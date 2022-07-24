---
title: 'Mongo Script Collection 모음'
tags : [mongo, script, mongodb]
social_image: /media/cover/cover-mongo.jpeg
date: 2022-07-24
---



```javascript
db.inventory.insertMany([
    {item: "journal", qty: 25, tags: ["blank", "red"], size: {h: 14, w: 21, uom: "cm"}},
    {item: "mat", qty: 85, tags: ["gray"], size: {h: 27.9, w: 35.5, uom: "cm"}},
    {item: "mousepad", qty: 25, tags: ["gel", "blue"], size: {h: 19, w: 22.85, uom: "cm"}}
])
```



# 1.Key Name

```javascript
db.inventory.updateMany({}, {$rename: {"item": "item_id"}}, false, true)
```



# 2. 업데이트 value based on key 

```javascript
db.inventory.updateMany(
    {"item_id": {$eq: "journal"}},
    {
        $set: {"item_id": "uuid 입력이 필요함"}
    }
)
```



# 참고

- https://blog.kevinchisholm.com/javascript/mongodb/getting-started-with-mongo-shell-scripting-basic-crud-operations/

  

  
