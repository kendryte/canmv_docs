Sensor Manual Whitebal Control - 摄像头白平衡控制
====================================================

```python
# 感光元件手动白平衡控制
#
# 此示例显示如何手动控制相机传感器的白平衡增益，而不是让自动白平衡控制运行。

# 通过调整R/G/B增益值使得图像的平均颜色为灰色来实现白平衡。 
# 自动白平衡（AWB）算法可以为您完成此操作，但每次打开相机时通常会得到不同的结果，这使得难以正确地进行颜色跟踪设置。 
# 通过手动记录您喜欢的增益值，然后在启动时强制它们到传感器，您可以控制相机看到的颜色。

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

# 您可以在此处控制白平衡增益。 第一个值是db中的R增益，然后是db中的G增益，然后是db中的B增益。
#
# 取消注释以下行使用您喜欢的增益值（从打印输出中获取）。
#
# sensor.set_auto_whitebal(False, rgb_gain_db = (0.0, 0.0, 0.0))

# 注意：为增益设置（0.0,0.0,0.0）会产生接近于零的值。不要指望进入的确切值等于出来的值。

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像
    print(clock.fps(), \
        sensor.get_rgb_gain_db())   # 输出AWB当前RGB增益。

```
