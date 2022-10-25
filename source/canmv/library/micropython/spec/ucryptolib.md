ucryptolib – 加密算法
==========================

`ucryptolib` 模块提供`aes`加密功能。

## 类 `aes`


### `aes`

#### 构造函数

```python
aes((key, mode[, IV]))
```

初始化密码对象，适用于加密/解密。

> 注意：初始化后，密码对象只能用于加密或解密。不支持在 encrypt() 之后运行 decrypt() 操作，反之亦然。

* `key`: 加密或解密使用的密钥，`bytes`类型。
* `mode `: 
    * `cryptolib.MODE_ECB`: Electronic Code Book (ECB) 模式。
    * `cryptolib.MODE_CBC`: Cipher Block Chaining (CBC) 模式。
    * `cryptolib.MODE_GCM`: Galois/Counter Mode (GCM) 模式。
* `IV`: `CBC` 模式的初始化向量。

#### 函数

##### `encrypt`

```python
encrypt(in_buf[, out_buf])
```

加密 `in_buf`。

如果没有给出 `out_buf`，则结果作为新分配的字节对象返回。

否则，将结果写入可变缓冲区 `out_buf`。 `in_buf` 和 `out_buf` 也可以引用同一个可变缓冲区，在这种情况下，数据被就地加密。

##### `decrypt`

```python
decrypt(in_buf[, out_buf])
```

解密方法，类似 `encrypt()`。
