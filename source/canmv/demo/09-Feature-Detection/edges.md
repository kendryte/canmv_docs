Edge detection - 边缘检测
================================

```python
# 这个示例展示了使用 Canny 算法进行边缘检测

import sensor, image, time

sensor.reset()                          # 复位并初始化摄像头
sensor.set_pixformat(sensor.GRAYSCALE)  # 设置摄像头输出格式为 GRAYSCALE（也可以是RGB565）
sensor.set_framesize(sensor.QQVGA)      # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)         # 跳过2000帧
clock = time.clock()                    # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                        # 更新计算帧率的clock
    img = sensor.snapshot()             # 拍照，获取一张图像

    # 使用 Canny 边缘检测器（稍慢）
    img.find_edges(image.EDGE_CANNY, threshold=(50, 80))
    # 使用 simpler 边缘检测器 （更快）
    #img.find_edges(image.EDGE_SIMPLE, threshold=(100, 255))
    print(clock.fps()) # 打印帧率
```

具体接口定义请参考 [find_edges](../../library/canmv/image.md#find_edges)
