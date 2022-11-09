array – 数组
================

该模块实现了相应 CPython 模块的子集，如下所述。有关更多信息，请参阅原始 CPython 文档：数组。
支持的格式代码：`b`, `B`, `h`, `H`, `i`, `I`, `l`, `L`, `q`, `Q`, `f`, `d`（后两种取决于浮点支持）。

## 类 `array`

### 构造函数

#### `array.array`

```python
array.array(typecode [, iterable])
```

使用给定类型的元素创建数组。数组的初始内容由 `iterable` 给出。如果未提供，则创建一个空数组。

### 函数

#### `append`

```python
arr.append(val)
```

将新元素 val 附加到数组的末尾，使其增长。

#### `extend`

```python
arr.extend(iterable)
```

将迭代中包含的新元素附加到数组的末尾，使其增长。
