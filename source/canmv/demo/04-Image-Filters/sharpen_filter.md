Sharpen Filter - 图像锐化
================================

```python
# 图像锐化例程：
#
# 这个例子演示了如何使用morph变换来锐化图像

import sensor, image, time

sensor.reset()                          # 复位并初始化摄像头
sensor.set_pixformat(sensor.GRAYSCALE)  # 设置摄像头输出格式为 GRAYSCALE（也可以是RGB565）
sensor.set_framesize(sensor.QQVGA)      # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)         # 跳过2000帧
clock = time.clock()                    # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像

    # 在图像的每个像素上运行核
    img.laplacian(1, sharpen=True)

    print(clock.fps()) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。
```

具体接口定义请参考 [laplacian](../../library/canmv/image.md#laplacian)
