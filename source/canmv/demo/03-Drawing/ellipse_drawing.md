Ellipse Drawing - 画椭圆
=======================

```python
# 这个例程展示如何在图片上画椭圆

import sensor, image, time, urandom

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock

    img = sensor.snapshot()         # 拍照，获取一张图像

    # 生成随机坐标值与RGB值
    for i in range(10):
        x = (urandom.getrandbits(30) % (2*img.width())) - (img.width()//2)
        y = (urandom.getrandbits(30) % (2*img.height())) - (img.height()//2)
        radius_x = urandom.getrandbits(30) % (max(img.height(), img.width())//2)
        radius_y = urandom.getrandbits(30) % (max(img.height(), img.width())//2)
        rot = urandom.getrandbits(30)

        r = (urandom.getrandbits(30) % 127) + 128
        g = (urandom.getrandbits(30) % 127) + 128
        b = (urandom.getrandbits(30) % 127) + 128

        # 在图片上画椭圆
        img.draw_ellipse(x, y, radius_x, radius_y, rot,
                         color = (r, g, b), thickness = 2, fill = False)

    print(clock.fps())              # 打印帧率
```

具体接口定义请参考 [draw_ellipse](../../library/canmv/image.md#draw_ellipse)
