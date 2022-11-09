Negative - 像素值反转
================================

```python
# 像素值反转例程
#
# 此示例显示像素值反转图像。
# 这不是一个特别有用的方法，但它偶尔会派上用场。

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot().negate()

    print(clock.fps()) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。
```

具体接口定义请参考 [negate](../../library/canmv/image.md#negate)
