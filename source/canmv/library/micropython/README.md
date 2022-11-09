`Micropython Library`
=============================

* 小提示:
```
可以在终端输入 help('modules') 来查看固件中内置的模块
```

<br>
<br>

# `Python` 标准库和`Micropython`标准微库

以下是`Micropython`兼容`Python`实现的微型库，在`import`的时候，一般需要在模块名称签加上`u`。

* [array](./array.md) – arrays of numeric data
* [binascii](./ubinascii.md) – binary/ASCII conversions
* [builtins](./builtins.md) – builtin functions and exceptions
* [cmath](./cmath.md) – mathematical functions for complex numbers
* [collections](./ucollections.md) – collection and container types
* [errno](./uerrno.md) – system error codes
* [gc](./gc.md) – control the garbage collector
* [hashlib](./uhashlib.md) – hashing algorithms
* [heapq](./uheapq.md) – heap queue algorithm
* [utimeq](./utimeq.md) –
* [io](./uio.md) – input/output streams
* [json](./ujson.md) – JSON encoding and decoding
* [math](./math.md) – mathematical functions
* [os](./uos.md) – basic “operating system” services
* [random](./urandom.md) – generate random numbers
* [re](./ure.md) – simple regular expressions
* [socket](./usocket.md) – socket module
* [struct](./ustruct.md) – pack and unpack primitive data types
* [sys](./sys.md) – system specific functions
* [time](./utime.md) – time related functions
* [zlib](./uzlib.md) – zlib decompression
* [_thread](./_thread.md) – multithreading support

# `MicroPython` 特有库

以下库中提供了特定于 MicroPython 实现的功能。

* [cryptolib](./spec/ucryptolib.md) – cryptographic ciphers
* [machine](./spec/machine.md) — functions related to the hardware
* [micropython](./spec/micropython.md) – access and control MicroPython internals
* [uctypes](./spec/uctypes.md) – access binary data in a structured way
