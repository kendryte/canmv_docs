onewire
============

单总线即只有单根信号线，该线即传输数据也传输时钟，并且数据传输也为双向，节约 IO 口。

# 类 `modules.onewire` 

## 构造函数

```python
onewire(gpio_num)
```

### 参数

* `gpio_num`：GPIO号。

### 返回值

* onewire 对象

## 函数 

### `reset`

```python
reset()
```

重置

#### 返回值

* bool 类型，是否成功。

### `readbit`

```python
readbit()
```

读取一位数据

#### 返回值

* int 类型，读取到的数据。

### `readbyte`

```python
readbyte()
```

读取一个字节

#### 返回值

* int 类型，读取到的数据。

### `readbuffer`

```python
readbuffer(n)
```

读取指定长度的字节数

#### 参数

* `n`：int 类型，需要读取的字节数

#### 返回值

* bytearray 类型，读取到的字节数组

### `writebit`

```python
writebit(bit)
```

写入一个位

#### 参数

* `bit`：int 类型，需要写入的位数据

### `writebyte`

```python
writebyte(byte)
```

#### 参数

* `byte`：int 类型，需要写入的字节数据

### `writebuffer` 

```python
writebuffer(buf)
```

#### 参数

* `buf`：bytearray 类型，需要写入的数据

### `select`

```python
select(rom_in)
```

让主机指定某一个从机。

#### 参数

* `rom_in`：bytearray 类型，表示将指定从机的8byte的ROM数据。

### `search`

```python
search(diff_in)
```

使用 F0H 标准搜索

#### 参数

* `diff_in`：int 类型，第一次搜索优先选择的路径

#### 返回值

* `list`：元素为(depth,roms)的列表，`depth` 为搜索深度,int 类型，`rom` 为器件 ROM 码，list 类型。

### `skip`

```python
skip()
```

跳过 ROM，适用于单节点

### `depower`

```python
depower()
```

重新使能IO

### `crc8`

```python
crc8(data_in)
```

计算8位循环冗余校验码

#### 参数

* `data_in`：需要校验的数据

#### 返回值

* 返回校验码