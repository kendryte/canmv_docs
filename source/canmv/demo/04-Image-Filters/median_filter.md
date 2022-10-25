Median Filter - 中值滤波
================================

```python
# 中值滤波
#
# 这个例子展示了中值滤波。中值滤波用其NxN邻域的中位数替换每个像素。中值滤波对于在保
# 留边缘的同时去除图像中的噪声是很好的。

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QQVGA)  # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像

    # Size是内核的大小。取1 (3x3 内核)、2 (5x5 内核)或更高值。

    # percentile控制内核中所使用值的百分位数。默认情况下，每个像素都使用相邻的第五
    # 十个百分位数（中心）替换。使用最小滤波时，您可将此值设置为0，使用下四分位数滤
    # 波时设置为0.25，使用上四分位数滤波时设置为0.75，使用最大滤波时设置为1。
    img.median(1, percentile=0.5)

    print(clock.fps()) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。
```

具体接口定义请参考 [median](../../library/canmv/image.md#median)
