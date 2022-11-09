Demo TouchScreen - 触摸屏例程
================================

```python
import touchscreen as ts
from machine import I2C
import lcd, image
from board import board_info
from fpioa_manager import fm
from maix import GPIO

# 配置BOOT_KEY 为清空按钮
fm.register(board_info.BOOT_KEY, fm.fpioa.GPIO1, force=True)
btn_clear = GPIO(GPIO.GPIO1, GPIO.IN)

lcd.init()                                              # 初始化屏幕显示
i2c = I2C(I2C.I2C0, freq=400000, scl=30, sda=31)        # 配置I2C0
ts.init(i2c)                                            # 触摸屏挂在I2C0下
#ts.calibrate()                                         # 触摸屏校准
lcd.clear()                                             # 将屏幕清空
img = image.Image()
status_last = ts.STATUS_IDLE
x_last = 0
y_last = 0
draw = False

# 读取触摸点数据，并在屏幕上绘制对应的点，记录触摸轨迹
while True:
    (status,x,y) = ts.read()
    print(status, x, y)
    if draw:
        img.draw_line((x_last, y_last, x, y))
    if status_last!=status:
        if (status==ts.STATUS_PRESS or status == ts.STATUS_MOVE):
            draw = True
        else:
            draw = False
        status_last = status
    lcd.display(img)
    x_last = x
    y_last = y
    if btn_clear.value() == 0:
        img.clear()



```
