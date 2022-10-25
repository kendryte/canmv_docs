Json - Json解析
================================

```python
import ujson

# Json 数据
json_str = '''{
    "name": "kendryte",
    "babies": [
        {
            "name": "canmv",
            "birthday": 220913,
            "sex": "unstable"
        }
    ]
}'''

# 解析Json并生成一个对象
obj = ujson.loads(json_str)
print(obj["name"])
print(obj["babies"])


```
