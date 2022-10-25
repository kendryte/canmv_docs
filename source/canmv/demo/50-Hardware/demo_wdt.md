Demo WDT - 看门狗例程
================================

```python
import time
from machine import WDT

# 不带回调的看门狗

# 初始化看门狗0
wdt0 = WDT(id=0, timeout=3000)
print('into', wdt0)
time.sleep(2)
print(time.ticks_ms())
# 1.test wdt feed
wdt0.feed()
time.sleep(2)
print(time.ticks_ms())
# 2.test wdt stop
wdt0.stop()
print('stop', wdt0)
# 3.wait wdt work
#while True:
    #print('idle', time.ticks_ms())
    #time.sleep(1)
```

```python
import time
from machine import WDT

# 看门狗回调
def on_wdt(self):
    print(self.context(), self)
    #self.feed()
    ## release WDT
    #self.stop()

# 带回调的看门狗

# 初始化看门狗1
wdt1 = WDT(id=1, timeout=4000, callback=on_wdt, context={})
print('into', wdt1)
time.sleep(2)
print(time.ticks_ms())
# 1.test wdt feed
wdt1.feed()
time.sleep(2)
print(time.ticks_ms())
# 2.test wdt stop
wdt1.stop()
print('stop', wdt1)
# 3.wait wdt work
#while True:
    #print('idle', time.ticks_ms())
    #time.sleep(1)
```

```python
import time
from machine import WDT
# 看门狗回调
def on_wdt(self):
    print(self.context(), self)
    #self.feed()
    ## release WDT
    #self.stop()

# 带回调的看门狗

# 初始化看门狗0&1
wdt0 = WDT(id=0, timeout=3000, callback=on_wdt, context=[])
wdt1 = WDT(id=1, timeout=4000, callback=on_wdt, context={})
## 3.wait wdt work
while True:
    #wdt0.feed()
    print('idle', time.ticks_ms())
    time.sleep(1)
```

具体接口定义请参考 [WDT](../../library/micropython/spec/machine.WDT.md)
