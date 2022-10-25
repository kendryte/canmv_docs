Grayscale Binary Filter - 灰度二值化滤波
==========================================

```python
# 灰度二值化例程
#
# 这个脚本展示了二值图像滤波。
# 这个脚本是很原始的测试，但是对于如何使用二值化还是很有用的。

import sensor, image, time

sensor.reset()
sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.skip_frames(time = 2000)
clock = time.clock()

low_threshold = (0, 50)
high_threshold = (205, 255)

while(True):

    # 测试低阈值
    for i in range(100):
        clock.tick()
        img = sensor.snapshot()
        img.binary([low_threshold])
        print(clock.fps())
        #image.binary(thresholds, invert=False)此函数将在thresholds内的
        #图像部分的全部像素变为1白，将在阈值外的部分全部像素变为0黑。invert将图像
        #的0 1（黑 白）进行反转，默认为false不反转。

    # 测试高阈值
    for i in range(100):
        clock.tick()
        img = sensor.snapshot()
        img.binary([high_threshold])
        print(clock.fps())

     #测试不是低阈值
    for i in range(100):
        clock.tick()
        img = sensor.snapshot()
        img.binary([low_threshold], invert = 1)
        print(clock.fps())

    #测试不是高阈值
    for i in range(100):
        clock.tick()
        img = sensor.snapshot()
        img.binary([high_threshold], invert = 1)
        print(clock.fps())

```

具体接口定义请参考 [binary](../../library/canmv/image.md#binary)
