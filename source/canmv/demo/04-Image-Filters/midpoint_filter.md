Midpoint Filter - 中点滤波
================================

```python
# 中点滤波例程
#
# 这个例子显示了中点过滤。中点滤波用NxN邻域的最小和最大像素值的平均值代替每个像
# 素。

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QQVGA)  # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像

    # size 是内核的大小。取1 (3x3 内核)、2 (5x5 内核)或更高值。

    # bias 控制图像混合的最小/最大程度。0只适用于最小滤波，1仅用于最大滤波。您可以
    # 通过对图像进行最小/最大化过滤。
    img.midpoint(1, bias=0.5)

    print(clock.fps()) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。
```

具体接口定义请参考 [midpoint](../../library/canmv/image.md#midpoint)
