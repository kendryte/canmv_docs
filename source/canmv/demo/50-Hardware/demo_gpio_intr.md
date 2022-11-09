Demo GPIO Int - GPIO 中断
================================

```python
from board import board_info

from fpioa_manager import fm

# 将IO16配置为GPIOHS0
fm.register(board_info.BOOT_KEY, fm.fpioa.GPIOHS0, force=True)

from maix import GPIO

def test_irq(pin_num):
    print("key", pin_num)

# 配置GPIOHS0为输入
key=GPIO(GPIO.GPIOHS0, GPIO.IN, GPIO.PULL_NONE)
# 配置GPIOHS0上下边沿中断
key.irq(test_irq, GPIO.IRQ_BOTH, GPIO.WAKEUP_NOT_SUPPORT, 7)

import time
for i in range(20):
    #print('key.value(): ', key.value())
    time.sleep_ms(500)

key.disirq()
fm.unregister(board_info.BOOT_KEY)
```

具体接口定义请参考 [GPIO](../../library/canmv/maix/maix.GPIO.md)
