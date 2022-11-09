Demo CPU - CPU 频率设置
================================

```python
from maix import freq

cpu_freq, kpu_freq = freq.get() # 获取当前频率设置
print(cpu_freq, kpu_freq)       # 打印频率

freq.set(cpu = 400, pll1=400, kpu_div = 1) # 设置频率
```
