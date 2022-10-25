Mode Adaptive Threshold Filter - 众数自适应阈值滤波
===========================================================

```python
# 众数自适应阈值滤波示例。

# 此示例显示了使用自适应阈值处理的众数滤波。 当mode(threshold=True) 时，
# mode()方法通过比较像素周围的像素的众数减去偏移量来自适应阈值图像。

import sensor, image, time

sensor.reset()                          # 复位并初始化摄像头
sensor.set_pixformat(sensor.GRAYSCALE)  # 设置摄像头输出格式为 GRAYSCALE（也可以是RGB565）
sensor.set_framesize(sensor.QQVGA)      # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)         # 跳过2000帧
clock = time.clock()                    # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像

    # 众数过滤器的参数是内核大小，对于1x1,3x3或5x5内核，它可以分别为0,1或2。
    img.mode(1, threshold=True, offset=5, invert=True)

    print(clock.fps()) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。
```

具体接口定义请参考 [mode](../../library/canmv/image.md#mode)
