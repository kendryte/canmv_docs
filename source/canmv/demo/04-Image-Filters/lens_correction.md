Lens Correction - 畸变校正
================================

```python
# 畸变校正
#
# 这个例程展示了如何使用畸变矫正方法来修复图像失真问题。在二维码/条形码/矩形码检测时需要使用此方法。
# 增加下面的strength直到直线在视图中。
# zoom是在对图像进行缩放的数值。默认值为1。

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

while(True):
    clock.tick()

    img = sensor.snapshot().lens_corr(strength = 1.8, zoom = 1.0)

    print(clock.fps())

```

具体接口定义请参考 [lens_corr](../../library/canmv/image.md#lens_corr)
