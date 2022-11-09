Histogram Equalization - 直方图均衡
==========================================

```python
# 直方图均衡例子
#
# 此示例展示了如何使用直方图均衡来改善图像中的对比度。 

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

while(True):
    clock.tick()

    img = sensor.snapshot().histeq()

    print(clock.fps())

```

具体接口定义请参考 [histeq](../../library/canmv/image.md#histeq)
