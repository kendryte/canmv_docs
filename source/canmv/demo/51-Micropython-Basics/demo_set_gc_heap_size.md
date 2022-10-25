Set_gc_heap_size - 设置gc heap 大小
================================

```python
import machine
import maix

# gc 大小1MiB
gc_mem_size = 1024*1024

# 判断当前gc heap是否为1MiB，如果不是则更新配置
print('config micropython gc stack 1M (1024KB) if not')
if maix.utils.gc_heap_size() != gc_mem_size:
    maix.utils.gc_heap_size(gc_mem_size)
    print('updates take effect when you reboot the system. ')
    machine.reset()

print('Current: ', maix.utils.gc_heap_size())


```
