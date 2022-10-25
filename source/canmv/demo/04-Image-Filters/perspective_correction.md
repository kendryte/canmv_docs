Perspective Correction - 透视校正
================================

```python
# 透视校正
#
# 这个例子展示了如何使用rotation_corr()来纠正透视图的失真，
# 然后在3D空间中向右旋转新的校正后的图像来处理移动。

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

# 图像将被扭曲，使以下几点成为新的:
#
#   (0,   0)
#   (w-1, 0)
#   (w-1, h-1)
#   (0,   h-1)
#
# 试着把下面的点设置到一个四边形的角上(按时钟顺序)。
# 您可以通过单击和拖动帧缓冲区并记录histogram小部件中显示的值来获得图像上的点。

w = sensor.width()
h = sensor.height()

TARGET_POINTS = [(0,   0),   # (x, y) CHANGE ME!
                 (w-1, 0),   # (x, y) CHANGE ME!
                 (w-1, h-1), # (x, y) CHANGE ME!
                 (0,   h-1)] # (x, y) CHANGE ME!

while(True):
    clock.tick()

    img = sensor.snapshot().rotation_corr(corners = TARGET_POINTS)

    print(clock.fps())

```

具体接口定义请参考 [rotation_corr](../../library/canmv/image.md#rotation_corr)
