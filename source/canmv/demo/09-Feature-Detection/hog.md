Histogram of Oriented Gradients (HoG)
===========================================

```python
# 这个例子演示HoG可视化。
#
# 注意：由于JPEG，HoG可视化看起来很模糊。要查看没有JPEG制品的图像，请取
# 消将图像保存到uSD的行的注释。

import sensor, image, time

sensor.reset()
# 设置摄像头
sensor.set_contrast(1)
sensor.set_gainceiling(8)
sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.skip_frames(time = 2000)

clock = time.clock()
while (True):
    clock.tick()
    img = sensor.snapshot()
    img.find_hog()

    # 取消注释将原始FB保存到文件并退出循环
    #img.save("/hog.pgm")
    #break

    print(clock.fps())

```

具体接口定义请参考 [find_hog](../../library/canmv/image.md#find_hog)
