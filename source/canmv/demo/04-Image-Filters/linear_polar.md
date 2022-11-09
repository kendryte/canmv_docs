Linear Polar Mapping - 线性极坐标映射
==========================================

```python
# 线性极坐标映射示例
# 此示例显示使用线性极坐标变换重新投影图像。 线性极化图像是有用的，
# 因为旋转变为X方向上的平移，并且标度的线性变化变为Y方向上的线性平移。

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QQVGA)  # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot().linpolar(reverse=False)

    print(clock.fps()) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。
```

具体接口定义请参考 [linpolar](../../library/canmv/image.md#linpolar)
