Image Histogram Info - 图像直方图信息
===========================================

```python
# 图像直方图信息示例
#
# 该脚本计算图像的直方图并将其打印出来。

import sensor, image, time

sensor.reset()
#设置图像色彩格式，有RGB565色彩图和GRAYSCALE灰度图两种
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # 颜色跟踪必须关闭自动增益
sensor.set_auto_whitebal(False) # 颜色跟踪必须关闭白平衡
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    # 获取图像的灰度直方图为8个bin。
    # Bins默认为256，可能在2到256之间。
    print(img.get_histogram(bins=8))
    print(clock.fps())

# 你也可以通过传递一个“roi =”给get_histogram（）来得到该区域的直方图。
# get_histogram（）允许您快速确定图像中任何区域的颜色通道信息。

```

具体接口定义请参考 [get_histogram](../../library/canmv/image.md#get_histogram)
