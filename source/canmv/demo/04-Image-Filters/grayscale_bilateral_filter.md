Grayscale Bilteral Filter - 灰度双边滤波
========================================

```python
# 双边滤波例程
# 此示例显示了在灰度图像上使用双边滤波。

import sensor, image, time

sensor.reset()                          # 复位并初始化摄像头
sensor.set_pixformat(sensor.GRAYSCALE)  # 设置摄像头输出格式为 GRAYSCALE（也可以是RGB565）
sensor.set_framesize(sensor.QQVGA)      # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)         # 跳过2000帧
clock = time.clock()                    # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像

    # color_sigma controls how close color wise pixels have to be to each other to be
    # blured togheter. A smaller value means they have to be closer.
    # A larger value is less strict.
    # color_sigma控制颜色明智的像素之间必须有多近的距离才能模糊
    # 更小的值意味着它们必须更接近。
    # 较大的值不那么严格。

    # space_sigma controls how close space wise pixels have to be to each other to be
    # blured togheter. A smaller value means they have to be closer.
    # A larger value is less strict.
    # space_sigma控制将空间明智的像素彼此模糊的距离。
    # 更小的值意味着它们必须更接近。
    # 较大的值不那么严格。

    # Run the kernel on every pixel of the image.
    # 在图像的每个像素上运行核
    img.bilateral(3, color_sigma=0.1, space_sigma=1)

    # 请注意，如果将color_sigma/space_sigma设置为聚合，双边过滤器可能会引入图像缺陷。
    # 如果你看到缺陷，增加sigma值直到缺陷消失。

    print(clock.fps()) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。

```

具体接口定义请参考 [bilateral](../../library/canmv/image.md#bilateral)
