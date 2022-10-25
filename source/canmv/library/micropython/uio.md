uio – 输入/输出流
====================

该模块实现了相应 CPython 模块的子集，如下所述。有关更多信息，请参阅原始 CPython 文档：[io](https://docs.python.org/3.5/library/io.html#module-io)


该模块包含其他类型的流（类文件）对象和辅助函数。


## 函数

### `open`

```python
io.open(name, mode='r', **kwargs)
```

打开一个文件。内置 `open()` 函数是此函数的别名。

## 类

### `class io.FileIO(...)`

这是以二进制模式打开的文件类型，例如使用`open(name, "rb")`。你不应该直接实例化这个类。

### `class io.TextIOWrapper(...)`

这是以文本模式打开的文件类型，例如使用`open(name, "rt")`。你不应该直接实例化这个类。

### `class io.StringIO([string])`

### `class io.BytesIO([string])`

用于输入/输出的内存中类似文件的对象。 

`StringIO` 用于文本模式 `I/O`（类似于使用“t”修饰符打开的普通文件）。 

`BytesIO` 用于二进制模式 `I/O`（类似于使用“b”修饰符打开的普通文件）。

类文件对象的初始内容可以用字符串参数指定（对于 `StringIO` 应该是普通字符串，对于 `BytesIO` 应该是字节对象）。

所有常见的文件方法，如 `read()`、`write()`、`seek()`、`flush()`、`close()` 都可用于这些对象，此外还有以下方法：

#### `getvalue()`

获取保存数据的底层缓冲区的当前内容。

### `class io.StringIO(alloc_size)`

### `class io.BytesIO(alloc_size)`

创建一个空的 `StringIO/BytesIO` 对象，预分配最多可容纳 `alloc_size` 个字节。

这意味着写入该数量的字节不会导致缓冲区的重新分配，因此不会遇到内存不足的情况或导致内存碎片。

这些构造函数是 `MicroPython` 扩展，建议仅在特殊情况和系统级库中使用，而不是用于最终用户应用程序。
