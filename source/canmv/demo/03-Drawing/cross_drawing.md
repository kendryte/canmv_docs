Cross Drawing - 画十字
============================

```python
# 这个例程展示如何在图片上画十字

import sensor, image, time, urandom

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick() # 更新计算帧率的clock

    img = sensor.snapshot() # 拍照，获取一张图像

    # 生成随机坐标值与RGB值
    for i in range(10):
        x = (urandom.getrandbits(30) % (2*img.width())) - (img.width()//2)
        y = (urandom.getrandbits(30) % (2*img.height())) - (img.height()//2)
        r = (urandom.getrandbits(30) % 127) + 128
        g = (urandom.getrandbits(30) % 127) + 128
        b = (urandom.getrandbits(30) % 127) + 128

        # 在图片上画十字
        img.draw_cross(x, y, color = (r, g, b), size = 10, thickness = 2)

    print(clock.fps()) # 打印帧率
```

具体接口定义请参考 [draw_cross](../../library/canmv/image.md#draw_cross)
