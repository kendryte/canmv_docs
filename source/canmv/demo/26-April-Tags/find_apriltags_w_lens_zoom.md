AprilTags w/Lens Zomm - AprilTags识别 带缩放矫正
=========================================================

```python
# AprilTags 标记追踪例程

import sensor, image, time, math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA) # 如果分辨率大得多，内存就不够用了……
#sensor.set_windowing((160, 120)) # 看中间160x120像素的VGA分辨率。
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)  # 必须关闭此功能，以防止图像冲洗…
sensor.set_auto_whitebal(False)  # 必须关闭此功能，以防止图像冲洗…
clock = time.clock()

# 注意！与find_qrcodes不同，find_apriltags方法不需要对镜像进行镜头校正。

#标签系列有什么区别？ 那么，例如，TAG16H5家族实际上是一个4x4的方形标签。 
#所以，这意味着可以看到比6x6的TAG36H11标签更长的距离。 
#然而，较低的H值（H5对H11），意味着4x4标签的假阳性率远高于6x6标签。 
#所以，除非你有理由使用其他标签系列，否则使用默认族TAG36H11。

while(True):
    clock.tick()
    img = sensor.snapshot()
    for tag in img.find_apriltags(): # defaults to TAG36H11
        img.draw_rectangle(tag.rect(), color = (255, 0, 0))
        img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
        print_args = (tag.id(), (180 * tag.rotation()) / math.pi)
        print("Tag Family TAG36H11, Tag ID %d, rotation %f (degrees)" % print_args)
    print(clock.fps())

```

具体接口定义请参考 [find_apriltags](../../library/canmv/image.md#find_apriltags)
