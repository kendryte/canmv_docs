Color Light Removal - 彩图光线去除
================================

```python
# 彩图光线去除例程
# 此示例显示如何从图像中删除明亮的灯光。
# 您可以使用带有“zero =”参数的binary()方法执行此操作。

# 从图像中删除明亮的光线允许您在图像上使用histeq()，
# 而不会使图像的过饱和部分的异常值破坏算法...

import sensor, image, time

sensor.reset()                          # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QQVGA)      # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)         # 跳过2000帧
clock = time.clock()                    # 创建一个clock对象，用来计算帧率

thresholds = (90, 100, -128, 127, -128, 127)

while(True):
    clock.tick() # 更新计算帧率的clock
    img = sensor.snapshot().binary([thresholds], invert=False, zero=True)

    print(clock.fps()) # 打印帧率

```

具体接口定义请参考 [binary](../../library/canmv/image.md#binary)
