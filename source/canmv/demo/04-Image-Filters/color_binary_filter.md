Color Binary Filter - 二值化滤波
================================

```python
# 颜色二值化滤波例子
#
# 这个脚本展示了二值图像滤波。
# 您可以传递二进制任意的阈值来分割图像。

import sensor, image, time

sensor.reset()
sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.RGB565)
sensor.skip_frames(time = 2000)
clock = time.clock()

#设置颜色阈值，如果是rgb图像，六个数字分别为(minL, maxL, minA, maxA, minB, maxB)；
#如果是灰度图，则只需设置（min, max）两个数字即可。
red_threshold = (0,100,   0,127,   0,127) # L A B
green_threshold = (0,100,   -128,0,   0,127) # L A B
blue_threshold = (0,100,   -128,127,   -128,0) # L A B

#使用工具 - >机器视觉 - >阈值编辑器选择更好的阈值。
while(True):

    #测试红色阈值
    for i in range(100):
        clock.tick()
        img = sensor.snapshot()
        img.binary([red_threshold])
        print(clock.fps())

    #测试绿色阈值
    for i in range(100):
        clock.tick()
        img = sensor.snapshot()
        img.binary([green_threshold])
        print(clock.fps())

    #测试蓝色阈值
    for i in range(100):
        clock.tick()
        img = sensor.snapshot()
        img.binary([blue_threshold])
        print(clock.fps())

    #测试不是红色阈值
    for i in range(100):
        clock.tick()
        img = sensor.snapshot()
        img.binary([red_threshold], invert = 1)
        print(clock.fps())

    #测试不是绿色阈值
    for i in range(100):
        clock.tick()
        img = sensor.snapshot()
        img.binary([green_threshold], invert = 1)
        print(clock.fps())

    #测试不是蓝色阈值
    for i in range(100):
        clock.tick()
        img = sensor.snapshot()
        img.binary([blue_threshold], invert = 1)
        print(clock.fps())

```

具体接口定义请参考 [binary](../../library/canmv/image.md#binary)
