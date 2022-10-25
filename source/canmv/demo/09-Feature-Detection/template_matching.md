Template Matching - 模板匹配
==========================================

```python
# NCC模板匹配示例-Normalized Cross Correlation (NCC)
#
# 这个例子展示了如何使用CanMV的NCC功能将小部分图像与图像的各个部分
# 进行匹配...期望获得极其可控的环境 NCC并不总是有用的。
#
# 警告：NCC支持需要重做！到目前为止，这个功能需要做大量的工作才能有用。
# 这个脚本将重新表明功能的存在，但在目前的状态是不足的。

import time, sensor, image
from image import SEARCH_EX, SEARCH_DS

sensor.reset()      # 复位并初始化摄像头

sensor.set_contrast(1)
sensor.set_gainceiling(16)
# 模板与SEARCH_EX匹配的最大分辨率是QQVGA
sensor.set_framesize(sensor.QQVGA)
# 你可以设置windowing窗口来减少搜索图片。
#sensor.set_windowing(((640-80)//2, (480-60)//2, 80, 60))
sensor.set_pixformat(sensor.GRAYSCALE)

# 加载模板。
# 模板应该是一个小的(例如。32x32像素)灰度图像。
template = image.Image("/sd/template.bmp")
template.to_grayscale()

clock = time.clock()

# 运行模板匹配
while (True):
    clock.tick()
    img = sensor.snapshot()

# find_template(template, threshold, [roi, step, search])
    # ROI: 感兴趣区域元组 (x, y, w, h).
    # Step:使用的循环步长(y+= Step, x+= Step) 使用更大的步长使其更快。
    # search 为image.SEARCH_EX进行详尽搜索，或者为image.SEARCH_DS进行菱形搜索
    #
    # Note1: ROI必须比图像小，比模板大。
    # Note2:在菱形diamond搜索中，step和ROI都被忽略。
    r = img.find_template(template, 0.70, step=4, search=SEARCH_EX) #, roi=(10, 0, 60, 60))
    # find_template(template, threshold, [roi, step, search]),
    # threshold中的0.7是相似度阈值,roi是进行匹配的区域（左上顶点为（10，0），长80宽60的矩形），
    # 注意roi的大小要比模板图片大，比frambuffer小。
    # 把匹配到的图像标记出来
    if r:
        img.draw_rectangle(r)

    print(clock.fps())

```

具体接口定义请参考 [find_template](../../library/canmv/image.md#find_template)
