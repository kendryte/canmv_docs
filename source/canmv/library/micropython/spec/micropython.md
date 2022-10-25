micropython - 读取和控制Micropython内部功能
===============================================

## 函数

### `const`

```python
micropython.const(expr)
```

用于声明表达式为常量，以便编译器对其进行优化。这个函数的使用应该如下：

```python
from micropython import const

CONST_X = const(123)
CONST_Y = const(2 * CONST_X + 1)
```

以这种方式声明的常量仍然可以从声明它们的模块外部作为全局变量访问。

另一方面，如果常量以下划线开头，则它是隐藏的，它不能作为全局变量使用，并且不会占用执行期间的任何内存。

这个 const 函数直接被 MicroPython 解析器识别，并作为 micropython 模块的一部分提供，主要是为了编写在 CPython 和 MicroPython 下运行的脚本，遵循上述模式。

### `opt_level`

```python
micropython.opt_level([level])
```

如果`level`没有给定参数，则返回当前的`otp_level`，否则在后续编译中使用给定的的优化级别。

* 断言：在`level`为`0`时会编译到字节码中，如果`level`大于等于`1`，则不会编译进字节码。
* 内置的`_debug__`变量： 在`level`为`0`时为`True`,`level`为`1`时为`False`。
* 代码行数：`level`为`0`、`1`、`2`时，代码行数会编译进字节码，`level`为`3`时，不会被编译进字节码中。

### `alloc_emergency_exception_buf`

```python
micropython.alloc_emergency_exception_buf(size)
```

为紧急异常缓冲区分配 size 字节的 RAM（推荐大小为100Bytes）。

缓冲区用于在正常 RAM 分配失败的情况下（例如在中断处理程序中）创建异常，因此在这些情况下提供有用的回溯信息。

推荐将其放在主脚本的开头（例如 boot.py 或 main.py）调用，然后紧急异常缓冲区将对其后面的所有代码都可用。


### `mem_info`

```python
micropython.mem_info([verbose])
```

打印有关当前使用的内存的信息。如果给出详细参数，则打印额外信息。

打印的信息取决于实现，但目前包括使用的堆栈和堆的数量。

在详细模式下，它会打印出整个堆，指示哪些块被使用，哪些块是空闲的。


### `mem_total`

```python
micropython.mem_total()
```

### `mem_current`

```python
micropython.mem_current()
```

### `mem_peak`

```python
micropython.mem_peak()
```

### `qstr_info`

```python
micropython.qstr_info([verbose])
```

打印有关当前`qstr_info`。如果给出详细参数，则打印额外信息。

打印的信息取决于实现，但目前包括内部字符串的数量和它们使用的 RAM 量。

在详细模式下，它会打印出所有 RAM 内部字符串的名称。


### `stack_use`

```python
micropython.stack_use()
```

返回一个整数，表示当前正在使用的堆栈数量。

它的绝对值并不是特别有用，而是应该用来计算不同点的堆栈使用差异。

### `heap_lock`

```python
micropython.heap_lock()
```

### `heap_unlock`

```python
micropython.heap_unlock()
```

### `heap_locked`

```python
micropython.heap_locked()
```

锁定或解锁堆。锁定时不会发生内存分配，如果尝试进行任何堆分配，将引发 `MemoryError`。如果堆当前被锁定，`heap_locked()` 返回`True`。


这些函数可以嵌套，即`heap_lock()`可以连续调用多次，锁的深度会增加，然后`heap_unlock()`必须调用相同的次数才能使堆再次可用。

`heap_unlock()` 和 `heap_locked()` 都以非负整数返回当前锁定深度（前者解锁后），0 表示堆未锁定。

如果 `REPL` 在堆锁定的情况下变为活动状态，那么它将被强制解锁。


### `kbd_intr`

```python
micropython.kbd_intr(chr)
```

设置将引发 `KeyboardInterrupt` 异常的字符。

默认情况下，在脚本执行期间设置为 `3`，对应于 `Ctrl-C`。将 `-1` 传递给此函数将禁用 `Ctrl-C` 捕获，传递 `3` 将恢复它。

此功能可用于防止在通常用于 `REPL` 的传入字符流上捕获 `Ctrl-C`，以防该流用于其他目的。

### `schedule`

```python
micropython.schedule(func, arg)
```
