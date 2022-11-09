Demo LCD - LCD 例程
================================

```python

import lcd, time

lcd.init()                      # 初始化LCD显示屏
#lcd.direction(lcd.XY_RLDU)

#lcd.init(type=2, invert=True) # cube ips
#lcd.init(width=320, height=240, invert=True, freq=20000000)

lcd.clear(lcd.RED)              # 将屏幕清空，使用红色填充

# 旋转屏幕并写字符串
lcd.rotation(0)
lcd.draw_string(30, 30, "hello canmv", lcd.WHITE, lcd.RED)
time.sleep(1)
lcd.rotation(1)
lcd.draw_string(60, 60, "hello canmv", lcd.WHITE, lcd.RED)
time.sleep(1)
lcd.rotation(2)
lcd.draw_string(120, 60, "hello canmv", lcd.WHITE, lcd.RED)
time.sleep(1)
lcd.rotation(3)
lcd.draw_string(120, 120, "hello canmv", lcd.WHITE, lcd.RED)
time.sleep(1)

```

具体接口定义请参考 [lcd](../../library/canmv/lcd.md)
