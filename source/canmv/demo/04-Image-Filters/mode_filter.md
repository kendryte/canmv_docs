Mode Filter - 众数滤波
================================

```python
# 众数滤波例程
#
# 这个例子显示众数过滤。 众数滤波是一种高度非线性的操作，它用每个像素周围像素的NxN邻# 域的众数取代每个像素。
# 避免在RGB565图像上使用众数过滤器。 它会在图像边缘造成伪影.

import sensor, image, time

sensor.reset()                          # 复位并初始化摄像头
sensor.set_pixformat(sensor.GRAYSCALE)  # 设置摄像头输出格式为 GRAYSCALE（也可以是RGB565）
sensor.set_framesize(sensor.QQVGA)      # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)         # 跳过2000帧
clock = time.clock()                    # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像

    # Size是内核的大小。取1 (3x3 内核)、2 (5x5 内核)。
    img.mode(1)

    print(clock.fps()) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。
```

具体接口定义请参考 [mode](../../library/canmv/image.md#mode)
