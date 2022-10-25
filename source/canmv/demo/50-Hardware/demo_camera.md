Demo Camera - 摄像头
================================

```python
import sensor, lcd

try:
    sensor.reset()                          # 初始化屏幕显示
except Exception as e:
    raise Exception("sensor reset fail, please check hardware connection, or hardware damaged! err: {}".format(e))
sensor.set_pixformat(sensor.RGB565)         # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)           # 设置摄像头输出大小为 QVGA (320x240)
sensor.run(1)
sensor.skip_frames()                        # 等待图像质量稳定
lcd.init(freq=15000000)                     # 初始化屏幕显示，指定驱动频率

while(True):
    lcd.display(sensor.snapshot())          # 拍照，获取一张图像并在LCD上显示
```
