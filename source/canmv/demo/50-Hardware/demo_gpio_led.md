Demo GPIO LED - GPIO 点灯例程
================================

```python
import time
from maix import GPIO
from fpioa_manager import fm
from board import board_info

# for 01studio
# fm.register(12, fm.fpioa.GPIO0, force=True)
# fm.register(13, fm.fpioa.GPIOHS0, force=True)
# fm.register(14, fm.fpioa.GPIO2, force=True)

# CanMV 开发板引脚配置
fm.register(23, fm.fpioa.GPIO0, force=True)
fm.register(24, fm.fpioa.GPIOHS0, force=True)
fm.register(25, fm.fpioa.GPIO2, force=True)
fm.register(board_info.BOOT_KEY, fm.fpioa.GPIO3, force=True)

# 配置引脚为输出
led_r = GPIO(GPIO.GPIO0, GPIO.OUT)
led_g = GPIO(GPIO.GPIOHS0, GPIO.OUT)
led_b = GPIO(GPIO.GPIO2, GPIO.OUT)
key_input = GPIO(GPIO.GPIO3, GPIO.IN)

status = 0
for i in range(0, 20):
    led_r.value(status)
    time.sleep_ms(300)
    led_g.value(status)
    time.sleep_ms(300)
    led_b.value(status)
    time.sleep_ms(300)
    status = 0 if (status == 1) else 1
    time.sleep_ms(300)
    print("LED RGB(%d,%d,%d)" % (led_r.value(), led_g.value(), led_b.value()))
    time.sleep_ms(100)
    print("key_input:", key_input.value())

fm.unregister(23)
fm.unregister(24)
fm.unregister(25)
fm.unregister(board_info.BOOT_KEY)

```

具体接口定义请参考 [GPIO](../../library/canmv/maix/maix.GPIO.md)
