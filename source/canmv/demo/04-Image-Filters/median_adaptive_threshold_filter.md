Median Adaptive Threshold Filter - 中值自适应阈值滤波
=======================================================

```python
# 中值自适应阈值滤波示例。
# 此示例显示了使用自适应阈值处理的中值滤波。 当median(threshold=True) 时，
# median()方法通过比较像素周围的像素的中值减去偏移量来自适应阈值图像。

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QQVGA)  # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像

    # 第一个参数是内核大小。N对应于((N * 2)+1)^ 2内核大小。 
    # 例如。 1 == 3x3内核，2 == 5x5内核等。

    # 第二个参数“percentile”是从NxN邻域中选择的百分位数。 
    # 0.5是中位数，0.25是下四分位数，0.75是上四分位数。
    img.median(1, percentile=0.5, threshold=True, offset=5, invert=True)

    print(clock.fps()) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。
```

具体接口定义请参考 [median](../../library/canmv/image.md#median)
