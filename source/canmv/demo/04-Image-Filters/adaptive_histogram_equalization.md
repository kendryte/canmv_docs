Adaptive Histogram Equalization - 直方图均衡
==================================================

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

    # A clip_limit of < 0 gives you normal adaptive histogram equalization
    # which may result in huge amounts of contrast noise...

    # A clip_limit of 1 does nothing. For best results go slightly higher
    # than 1 like below. The higher you go the closer you get back to
    # standard adaptive histogram equalization with huge contrast swings.

    img = sensor.snapshot().histeq(adaptive=True, clip_limit=3)

    print(clock.fps())

```

具体接口定义请参考 [histeq](../../library/canmv/image.md#histeq)
