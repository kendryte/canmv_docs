Mem Free - 查看剩余内存信息
================================

```python
import gc

print(gc.mem_free() / 1024) # stack mem

import maix

print(maix.utils.heap_free() / 1024) # heap mem

```
