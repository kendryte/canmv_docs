Thread - 多线程
================================

```python
# doc refer to: http://docs.micropython.org/en/latest/library/_thread.html?highlight=_thread#module-_thread

import _thread
import time

def func(name):
    while 1:
        print("hello {}".format(name))
        time.sleep(1)

_thread.start_new_thread(func,("1",))
_thread.start_new_thread(func,("2",))

while 1:
    pass
```

具体接口定义请参考 [_thread](../../library/micropython/_thread.md)
