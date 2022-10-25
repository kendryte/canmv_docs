math – 数学函数
====================

该模块实现了相应CPython模块的子集，如下所述。有关更多信息，请参阅原始CPython文档：[math](https://docs.python.org/3.5/library/math.html#module-math).

`math`模块提供了一些处理浮点数的基本数学函数。


### 函数

#### `acos`

```python
math.acos(x)
```

返回`x`的反余弦值。

#### `acosh`

```python
math.acosh(x)
```

返回`x`的反双曲余弦值。

#### `asin`

```python
math.asin(x)
```

返回`x`的反正弦。

#### `asinh`

```python
math.asinh(x)
```

返回`x`的反双曲正弦值。

#### `atan`

```python
math.atan(x)
```

返回`x`的反正切。

#### `atan2`

```python
math.atan2(y, x)
```

返回`y` /`x`的反正切的主值。

#### `atanh`

```python
math.atanh(x)
```

返回`x`的反双曲正切。

#### `ceil`

```python
math.ceil(x)
```

返回一个整数，“x”向正无穷大四舍五入。

#### `copysign`

```python
math.copysign(x, y)
```

以`y`的符号返回`x`。

#### `cos`

```python
math.cos(x)
```

返回`x`的余弦。


#### `cosh`

```python
math.cosh(x)
```

返回`x`的双曲余弦值

#### `degrees`

```python
math.degrees(x)
```

返回弧度`x`转换为度数。

#### `erf`

```python
math.erf(x)
```

返回`x`的错误函数。

#### `erfc`

```python
math.erfc(x)
```

返回`x`的互补误差函数。

#### `exp`

```python
math.exp(x)
```

返回`x`的指数。

#### `expm1`

```python
math.expm1(x)
```

返回`exp（x） -  1`。

#### `fabs`

```python
math.fabs(x)
```

返回`x`的绝对值。

#### `floor`

```python
math.floor(x)
```

返回一个整数，“x”向负无穷大舍入。

#### `fmod`

```python
math.fmod(x, y)
```

返回`x` /`y`的余数。

#### `frexp`

```python
math.frexp(x)
```

将浮点数分解为尾数和指数。返回的值是元组`（m，e）`，使得`x == m * 2 ** e`完全正确。如果`x == 0`则函数返回`（0.0,0）`，否则关系`0.5 <= abs（m）<1`成立。

#### `gamma`

```python
math.gamma(x)
```

返回`x`的伽玛函数。

#### `isfinite`

```python
math.isfinite(x)
```

如果`x`是有限的，则返回True。

#### `isinf`

```python
math.isinf(x)
```

如果`x`是无限的，则返回True。

#### `isnan`

```python
math.isnan(x)
```

如果`x`不是数字，则返回True

#### `ldexp`

```python
math.ldexp(x, exp)
```

返回`x *（2 ** exp）`。

#### `lgamma`

```python
math.lgamma(x)
```

返回`x`的伽玛函数的自然对数。

#### `log`

```python
math.log(x)
```

返回`x`的自然对数。

#### `log10`

```python
math.log10(x)
```

返回`x`的以10为底的对数。

#### `log2`

```python
math.log2(x)
```

返回`x`的base-2对数。

#### `modf`

```python
math.modf(x)
```

返回两个浮点数的元组，是“x”的分数和整数部分。两个返回值都与`x`具有相同的符号。

#### `pow`

```python
math.pow(x, y)
```

将`x`返回到'y`的幂。

#### `radians`

```python
math.radians(x)
```

返回度数`x`转换为弧度。

#### `sin`

```python
math.sin(x)
```

返回`x`的正弦值。

#### `sinh`

```python
math.sinh(x)
```

返回`x`的双曲正弦值。

#### `sqrt`

```python
math.sqrt(x)
```

返回`x`的平方根。

#### `tan`

```python
math.tan(x)
```

返回`x`的正切值。

#### `tanh`

```python
math.tanh(x)
```

返回`x`的双曲正切。

#### `trunc`

```python
math.trunc(x)
```


返回一个整数，“x”向0舍入。

### Constants

#### `math.e`

自然对数的基础

#### `math.pi`

圆周长与直径的比值

