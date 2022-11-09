maix.utils
===============

## 类 `maix.utils`

### 函数

#### `gc_heap_size`

```python
maix.utils.gc_heap_size([size])
```

获取或者设置 GC 堆大小，如果报内存不够时可以考虑设置大一点

##### 参数

无 或者 传入新的 GC 堆大小.
* 如果没有参数就只是获取堆大小；
* 如果有参数则设置堆大小，然后会自动重启

##### 返回值

GC 堆大小

#### `flash_read`

```python
maix.utils.flash_read(flash_offset, size)
```

从内部 flash 读取 size 指定大小(字节数) 数据

##### 参数

flash_offset: flash 地址偏移

flash_offset: flash 地址偏移

#### `heap_free`

```python
maix.utils.heap_free()
```

获取当前剩余的内存空间（非gc管理部分）

