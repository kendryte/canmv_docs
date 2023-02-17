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

#### `free_kpu_buffers`

```python
info = maix.utils.free_kpu_buffers()
```

释放所有`KPU`申请的内存，使用的时候，请注意是否会影响到正常的模型使用，建议在模型之前，或者在程序结束运行的时候使用

> 固件版本在[V1.0.5](https://github.com/kendryte/canmv/releases/tag/v1.0.5)之的可使用本函数

##### 参数

* 无

##### 返回值

* `info`：包含释放内存信息的`dict`
    - `count`: 释放的`buffer`数量
    - `size`: 释放内存总大小
