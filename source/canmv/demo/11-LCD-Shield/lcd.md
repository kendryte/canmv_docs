lcd - 显示屏
================================

```python
# LCD 可以显示帧缓存中的图像

import sensor, image, lcd

lcd.init()                              # 初始化LCD显示屏

sensor.reset()                          # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565)     # 设置摄像头输出格式为 RGB565
sensor.set_framesize(sensor.QVGA)       # 设置摄像头输出大小为 QVGA (320x240)

while(True):
    lcd.display(sensor.snapshot())      # 拍照并显示图像到LCD上
```

具体接口定义请参考 [lcd](../../library/canmv/lcd.md)
