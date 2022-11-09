Robust Linear Regression - 鲁棒线性回归
================================

```python
# 鲁棒线性回归例程
#
# 这个例子展示了如何在CanMV Cam上使用get_regression（）方法来获得
# ROI的线性回归。 使用这种方法，你可以轻松地建立一个机器人，它可以
# 跟踪所有指向相同的总方向但实际上没有连接的线。 在线路上使用
# find_blobs（），以便更好地过滤选项和控制。
#
# 我们在这个脚本中使用get_regression（）的robust = True参数，该脚本使用更稳健的算法计算线性回归...但是可能慢得多。 鲁棒算法在图像上运行O（N ^ 2）时间。 所以，你需要限制像素的数量来使这个算法工作，它可能实际需要秒的时间给你一个结果...非常小心！

THRESHOLD = (0, 100) # Grayscale threshold for dark things...

# 首先二值化，所以你可以看到什么线性回归正在运行...虽然可能会降低FPS。
BINARY_VISIBLE = True

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQQVGA) # 80x60 (4,800 pixels) - O(N^2) max = 2,3040,000.
sensor.skip_frames(time = 2000)     # 警告：如果使用QQVGA，则有时可能需要几秒钟来处理一帧。
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot().binary([THRESHOLD]) if BINARY_VISIBLE else sensor.snapshot()

    # 返回类似于由find_lines（）和find_line_segments（）返回的线对象。 
    # 你有x1（），y1（），x2（），y2（），length（），
    # theta（）（以度为单位的旋转），rho（）和magnitude（）。
    #
    # magnitude() 表示线性回归的工作情况。这对于鲁棒的线性回归意味着不同
    # 的东西。一般来说，值越大越好...
    line = img.get_regression([(255,255) if BINARY_VISIBLE else THRESHOLD], robust = True)

    if (line): img.draw_line(line.line(), color = 127)
    print("FPS %f, mag = %s" % (clock.fps(), str(line.magnitude()) if (line) else "N/A"))

# 关于负rho值:
#
# A [theta+0:-rho] tuple is the same as [theta+180:+rho].
# A [theta+0:-rho]元组与[theta+180:+rho]相同

```

具体接口定义请参考 [get_regression](../../library/canmv/image.md#get_regression)
