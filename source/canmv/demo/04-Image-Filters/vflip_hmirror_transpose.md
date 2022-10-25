Vertical Flip - Horizontal Mirror - Transpose
========================================================

```python
# 垂直翻转 - 水平镜像 - 转置图像
#
# 此示例显示如何垂直翻转，水平镜像或转置图像。
#
# vflip=False, hmirror=False, transpose=False -> 0 degree rotation
# vflip=True,  hmirror=False, transpose=True  -> 90 degree rotation
# vflip=True,  hmirror=True,  transpose=False -> 180 degree rotation
# vflip=False, hmirror=True,  transpose=True  -> 270 degree rotation

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

mills = time.ticks_ms()
counter = 0

while(True):
    clock.tick()

    img = sensor.snapshot().replace(vflip=(counter//2)%2,
                                    hmirror=(counter//4)%2,
                                    transpose=(counter//8)%2)

    if (time.ticks_ms() > (mills + 1000)):
        mills = time.ticks_ms()
        counter += 1

    print(clock.fps())

```
