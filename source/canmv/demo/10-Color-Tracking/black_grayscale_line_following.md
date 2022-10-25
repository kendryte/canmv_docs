Black Grayscale Line Following - 灰度巡线
================================================

```python
# 机器人巡线例程
#
# 跟随机器人做一条线需要很多努力。 本示例脚本显示了如何执行跟随机器人的
# 机器视觉部分。 您可以使用此脚本的输出来驱动差分驱动机器人遵循一条线。
# 这个脚本只是产生一个转动的值，告诉你的机器人向左或向右。
#
# 为了使这个脚本正常工作，你应该把摄像机指向45度左右的一条线。请确保只有线在相机的视野内。

import sensor, image, time, math

# 跟踪一条黑线。使用[(128,255)]来跟踪白线。
GRAYSCALE_THRESHOLD = [(0, 64)]

# 每个roi为(x, y, w, h)，线检测算法将尝试找到每个roi中最大的blob的质心。
# 然后用不同的权重对质心的x位置求平均值，其中最大的权重分配给靠近图像底部的roi，
# 较小的权重分配给下一个roi，以此类推。
ROIS = [ # [ROI, weight]
        (0, 100, 160, 20, 0.7), # 你需要为你的应用程序调整权重
        (0,  50, 160, 20, 0.3), # 取决于你的机器人是如何设置的。
        (0,   0, 160, 20, 0.1)
       ]

#roi代表三个取样区域，（x,y,w,h,weight）,代表左上顶点（x,y）宽高分别为w和h的矩形，
#weight为当前矩形的权值。注意本例程采用的QQVGA图像大小为160x120，roi即把图像横分成三个矩形。
#三个矩形的阈值要根据实际情况进行调整，离机器人视野最近的矩形权值要最大，
#如上图的最下方的矩形，即(0, 100, 160, 20, 0.7)

# Compute the weight divisor (we're computing this so you don't have to make weights add to 1).
weight_sum = 0 #权值和初始化
for r in ROIS: weight_sum += r[4] # r[4] is the roi weight.
#计算权值和。遍历上面的三个矩形，r[4]即每个矩形的权值。

# 初始化sensor
sensor.reset()
#设置图像色彩格式，有RGB565色彩图和GRAYSCALE灰度图两种
sensor.set_pixformat(sensor.GRAYSCALE) # use grayscale.
#设置图像像素大小
sensor.set_framesize(sensor.QQVGA) # use QQVGA for speed.
 # 让新的设置生效。
sensor.skip_frames(time = 2000) # Let new settings take affect.
# 颜色跟踪必须关闭自动增益
sensor.set_auto_gain(False) # must be turned off for color tracking
# 颜色跟踪必须关闭白平衡
sensor.set_auto_whitebal(False) # must be turned off for color tracking
 # 跟踪FPS帧率
clock = time.clock() # Tracks FPS.

while(True):
    clock.tick() # 追踪两个snapshots()之间经过的毫秒数.
    img = sensor.snapshot() # 拍照，获取一张图像

    centroid_sum = 0

    #利用颜色识别分别寻找三个矩形区域内的线段
    for r in ROIS:
        # 找到视野中的线,merge=true,将找到的图像区域合并成一个
        blobs = img.find_blobs(GRAYSCALE_THRESHOLD, roi=r[0:4], merge=True) # r[0:4] is roi tuple.

        # 目标区域找到直线
        if blobs:
            # 目标区域找到的颜色块（线段块）可能不止一个，找到最大的一个，作为本区域内的目标直线
            largest_blob = max(blobs, key=lambda b: b.pixels())

            # Draw a rect around the blob.
            img.draw_rectangle(largest_blob.rect())
            img.draw_cross(largest_blob.cx(),
                           largest_blob.cy())

            centroid_sum += largest_blob.cx() * r[4] # r[4] is the roi weight.

    center_pos = (centroid_sum / weight_sum) # Determine center of line.

    # 将center_pos转换为一个偏角。我们用的是非线性运算，所以越偏离直线，响应越强。
    # 非线性操作很适合用于这样的算法的输出，以引起响应“触发器”。
    deflection_angle = 0

    # 角度计算.80 60 分别为图像宽和高的一半，图像大小为QQVGA 160x120.    
    # 注意计算得到的是弧度值
    deflection_angle = -math.atan((center_pos-80)/60)

    # 将计算结果的弧度值转化为角度值
    deflection_angle = math.degrees(deflection_angle)

    # 现在你有一个角度来告诉你该如何转动机器人。
    # 通过该角度可以合并最靠近机器人的部分直线和远离机器人的部分直线，以实现更好的预测。
    print("Turn Angle: %f" % deflection_angle)

    # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。
    # 打印当前的帧率。
    print(clock.fps())

```

具体接口定义请参考 [find_blobs](../../library/canmv/image.md#find_blobs)
