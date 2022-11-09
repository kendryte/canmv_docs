urandom – 随机数生成
===========================

该模块实现了一个伪随机数生成器 (PRNG)。

该模块实现了相应 CPython 模块的子集，如下所述。有关更多信息，请参阅原始 CPython 文档：[random](https://docs.python.org/3.5/library/random.html#module-random)

## 整数随机数生成函数

### `getrandbits`

```python
random.getrandbits(n)
```

返回具有 n 个随机位 (0 <= n <= 32) 的整数。


### `randint`

```python
random.randint(a, b)
```

返回 [a, b] 范围内的随机整数。

### `randrange`

```python
1. random.randrange(stop)
2. random.randrange(start, stop)
3. random.randrange(start, stop[, step])
```

* 1. 返回从 [0, stop) 范围内返回一个随机整数。

* 2. 返回范围 [start, stop) 中的随机整数。

* 3. 以 step 的步进从范围 [start, stop) 中返回一个随机整数。例如，调用 randrange(1, 10, 2) 将返回介于 1 和 9 之间的奇数。

## 浮点随机数生成函数


### `random`

```python
random.random()
```

返回 [0.0, 1.0) 范围内的随机浮点数。

### `uniform`

```python
random.uniform(a, b)
```

返回一个随机浮点数 N，使得 a <= N <= b 表示 a <= b，b <= N <= a 表示 b < a。


## 其他函数

### `seed`

```python
random.seed(n)
```

用种子 n 初始化随机数生成器，种子 n 应该是一个整数。

### `choice`

```python
random.choice(sequence)
```

从序列（元组、列表或任何支持下标操作的对象）中随机选择并返回一项。
