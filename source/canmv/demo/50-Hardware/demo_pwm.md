Demo PWM - PWM 例程
================================

```python
from machine import Timer,PWM
import time
from fpioa_manager import fm

# 配置定时器0通道0为PWM模式
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
# 配置PWM
ch = PWM(tim, freq=500000, duty=50, pin=25)
duty=0
dir = True
# 呼吸灯
while True:
    if dir:
        duty += 10
    else:
        duty -= 10
    if duty>100:
        duty = 100
        dir = False
    elif duty<0:
        duty = 0
        dir = True
    time.sleep(0.05)
    ch.duty(duty)
```

具体接口定义请参考 [PWM](../../library/micropython/spec/machine.PWM.md)
