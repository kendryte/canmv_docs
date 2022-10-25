Selective Search
================================

```python
# 选择性查找例程

import sensor, image, time
from random import randint

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
sensor.set_auto_gain(False)
# sensor.set_auto_exposure(False, exposure_us=10000)
clock = time.clock()                # 创建一个clock对象，用来计算帧率


while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像
    rois = img.selective_search(threshold = 200, size = 20, a1=0.5, a2=1.0, a3=1.0)
    for r in rois:
        img.draw_rectangle(r, color=(255, 0, 0))
        #img.draw_rectangle(r, color=(randint(100, 255), randint(100, 255), randint(100, 255)))
    print(clock.fps())

```
