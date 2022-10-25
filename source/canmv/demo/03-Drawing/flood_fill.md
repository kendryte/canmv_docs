Flood Fill - 填充图像
==========================

```python
# 这个例程展示如何在图片部分区域填充数据

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock

    img = sensor.snapshot()         # 拍照，获取一张图像

    x = sensor.width() // 2
    y = sensor.height() // 2

    # 填充图像
    img.flood_fill(x, y, \
        seed_threshold=0.05, floating_thresholds=0.05, \
        color=(255, 0, 0), invert=False, clear_background=False)

    print(clock.fps())              # 打印帧率
```

具体接口定义请参考 [flood_fill](../../library/canmv/image.md#flood_fill)
