Find Circles - 圆形检测
================================

```python
# 这个例程展示如何进行圆形检测，
# 关于圆形检测，可以参考 https://en.wikipedia.org/wiki/Circle_Hough_Transform
#
# 请注意，find_circles() 这个方法只会检测在图像中完整的圆形

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE），GRAYSCALE运行速度更快
sensor.set_framesize(sensor.QQVGA)   # 设置摄像头输出大小为 QQVGA (160x120)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    
    # 拍照，获取一张图像，并进行矫正
    img = sensor.snapshot().lens_corr(1.8)         

    # 进行圆形检测，并绘制出圆形区域
    for c in img.find_circles(threshold = 2000, x_margin = 10, y_margin = 10, r_margin = 10,
            r_min = 2, r_max = 100, r_step = 2):
        img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))
        print(c)

    print("FPS %f" % clock.fps()) # 打印帧率
```

具体接口定义请参考 [find_circles](../../library/canmv/image.md#find_circles)
