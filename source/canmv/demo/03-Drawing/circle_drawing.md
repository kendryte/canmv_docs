Circle Drawing - 画圆
=======================
本程序展示如何在图像上叠加绘制圆形。  

与绘制箭头的例程类似，它在初始化完成摄像头和显示屏模块后，先产生随机的坐标值和颜色值，利用 image.draw_circle 方法将箭头叠加绘制在显示屏上。

```python
# 这个例程展示如何在图片上画圆

import sensor, lcd, image, time, urandom

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

lcd.init()                          # Init lcd display
lcd.clear(lcd.RED)                  # Clear lcd screen.

while(True):
    clock.tick()                    # 更新计算帧率的clock

    img = sensor.snapshot()         # 拍照，获取一张图像
    
    # 生成随机坐标值与RGB值
    for i in range(10):
        x = (urandom.getrandbits(30) % (2*img.width())) - (img.width()//2)
        y = (urandom.getrandbits(30) % (2*img.height())) - (img.height()//2)
        radius = urandom.getrandbits(30) % (max(img.height(), img.width())//2)

        r = (urandom.getrandbits(30) % 127) + 128
        g = (urandom.getrandbits(30) % 127) + 128
        b = (urandom.getrandbits(30) % 127) + 128

        # 在图片上画圆
        img.draw_circle(x, y, radius, color = (r, g, b), thickness = 2, fill = False)

    lcd.display(img)                # Display image on lcd.
    print(clock.fps()) # 打印帧率
```

具体接口定义请参考 [draw_circle](../../library/canmv/image.md#draw_circle)
