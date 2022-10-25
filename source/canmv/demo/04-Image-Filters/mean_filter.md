Mean Filter - 均值滤波
================================

```python
# 均值滤波例程
#
# 这个例子展示了均值滤波。均值滤波是NxN邻域的标准均值滤波。
# 均值滤波通过模糊所有内容来消除图像中的噪点。
# 但是，这是最快的内核过滤器操作

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QQVGA)  # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像

    # The only argument is the kernel size. N coresponds to a ((N*2)+1)^2
    # kernel size. E.g. 1 == 3x3 kernel, 2 == 5x5 kernel, etc. Note: You
    # shouldn't ever need to use a value bigger than 2.
    # 唯一的参数是内核大小。N对a ((N*2)+1)^2的核大小有响应。
    # 例如:1 == 3x3内核，2 == 5x5内核，等等。
    # 注意:不应该使用大于2的值。
    img.mean(1)

    print(clock.fps()) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。
```

具体接口定义请参考 [mean](../../library/canmv/image.md#mean)
