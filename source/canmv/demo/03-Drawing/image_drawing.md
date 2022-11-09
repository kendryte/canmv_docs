Draw Image - 画图
==================================

```python
# 这个例程展示如何将图像粘贴到另一个图像上

import sensor, image, time

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock

    img = sensor.snapshot()         # 拍照，获取一张图像

    small_img = img.mean_pooled(4, 4) # 从原图生成一个新的图像

    x = (img.width()//2)-(small_img.width()//2)
    y = (img.height()//2)-(small_img.height()//2)
    
    # 在图像上画另一个图像
    img.draw_image(small_img, x, y, x_scale=1, y_scale=1)

    print(clock.fps()) # 打印帧率
```

具体接口定义请参考 [draw_image](../../library/canmv/image.md#draw_image)
