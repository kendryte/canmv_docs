Sensor Horizontal Mirror - 摄像头水平镜像
================================================

```python
# 感光元件水平镜像
#
# 这个例子展示了在感光元件的硬件上水平镜像图像

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

# 把True改成False就可以关闭水平镜像
sensor.set_hmirror(True)

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像
    print(clock.fps())              # 打印帧率

```

具体接口定义请参考 [set_hmirror](../../library/canmv/sensor.md#set_hmirror)
