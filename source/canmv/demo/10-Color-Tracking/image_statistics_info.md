Image Statistics Info - 图像统计信息
==========================================

```python
# 图像统计信息示例
#
# 该脚本计算图像的统计信息并将其打印出来。

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE) # or RGB565.
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # 颜色跟踪必须关闭自动增益
sensor.set_auto_whitebal(False) # 颜色跟踪必须关闭白平衡
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    print(img.get_statistics())
    print(clock.fps())

# 你也可以给传递get_statistics（）一个“roi =”来获得该区域的统计信息。
# get_statistics（）允许您快速确定图像中任何区域的颜色通道信息。

```

具体接口定义请参考 [get_statistics](../../library/canmv/image.md#get_statistics)
