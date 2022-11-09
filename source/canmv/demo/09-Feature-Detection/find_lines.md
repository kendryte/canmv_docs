Find Lines - 直线检测
================================

```python
# 识别直线例程
#
# 这个例子展示了如何在图像中查找线条。对于在图像中找到的每个线对象，
# 都会返回一个包含线条旋转的线对象。

# 注意：线条检测是通过使用霍夫变换完成的：
# http://en.wikipedia.org/wiki/Hough_transform
# 请阅读以上关于“theta”和“rho”的更多信息。

# find_lines（）找到无限长度的线。使用find_line_segments（）
# 来查找非无限线。

enable_lens_corr = False # 打开以获得更直的线条…

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565) # 灰度更快
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

# 所有的线对象都有一个`theta（）`方法来获取它们的旋转角度。
# 您可以根据旋转角度来过滤线条。

min_degree = 0
max_degree = 179

# 所有线段都有 `x1()`, `y1()`, `x2()`, and `y2()` 方法来获得他们的终点
# 一个 `line()` 方法来获得所有上述的四个元组值，可用于 `draw_line()`.

while(True):
    clock.tick()
    img = sensor.snapshot()
    if enable_lens_corr: img.lens_corr(1.8) # for 2.8mm lens...

    # `threshold` controls how many lines in the image are found. Only lines with
    # edge difference magnitude sums greater than `threshold` are detected...

    # `threshold`控制从霍夫变换中监测到的直线。只返回大于或等于阈值的
    # 直线。应用程序的阈值正确值取决于图像。注意：一条直线的大小是组成
    # 直线所有索贝尔滤波像素大小的总和。

    # `theta_margin`和`rho_margin`控件合并相似的直线。如果两直线的
    # theta和ρ值差异小于边际，则它们合并。

    for l in img.find_lines(threshold = 1000, theta_margin = 25, rho_margin = 25):
        if (min_degree <= l.theta()) and (l.theta() <= max_degree):
            img.draw_line(l.line(), color = (255, 0, 0))
            # print(l)

    print("FPS %f" % clock.fps())

# About negative rho values:
# 关于负rho值:
#
# A [theta+0:-rho] tuple is the same as [theta+180:+rho].
# A [theta+0:-rho]元组与[theta+180:+rho]相同。
```

具体接口定义请参考 [find_lines](../../library/canmv/image.md#find_lines)
