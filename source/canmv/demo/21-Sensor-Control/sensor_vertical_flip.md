Sensor Vertical Flip - 摄像头垂直翻转控制
=================================================

```python
# 感光元件纵向翻转
#
# 这个例子展示了在感光元件的硬件上纵向翻转图像

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

# 把True改成False就可以关闭纵向翻转
sensor.set_vflip(True)

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像
    print(clock.fps())  # 打印帧率

```

具体接口定义请参考 [set_vflip](../../library/canmv/sensor.md#set_vflip)
