Local Binary Patterns (LBP)
================================

```python
# Local Binary Patterns (LBP) 特征例程
#
# 这个例子展示了如何在CanMV Cam上使用LBP特征描述符。 LBP描述符像
# Freak特征描述符一样工作。
#
# 警告：LBP功能需要修改！到目前为止，这个功能需要做大量的工作才能有用。
# 这个脚本将表明功能的存在，但在目前的状态是不足的。

import sensor, time, image
sensor.reset()

sensor.reset()

# 设置摄像头
sensor.set_contrast(1)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.HQVGA)
sensor.set_pixformat(sensor.GRAYSCALE)

# 加载Haar算子
# 默认情况下，这将使用所有阶段，较低的阶段更快但不太准确。
face_cascade = image.HaarCascade("frontalface", stages=25)
print(face_cascade)

# 跳过几帧，让传感器稳定下来
# 注意：当从IDE执行时，这需要更多的时间。
for i in range(0, 30):
    img = sensor.snapshot()
    img.draw_string(0, 0, "Please wait...")

d0 = None
#d0 = image.load_descriptor("/desc.lbp")
clock = time.clock()

while (True):
    clock.tick()
    img = sensor.snapshot()

    objects = img.find_features(face_cascade, threshold=0.5, scale_factor=1.25)
    if objects:
        face = objects[0]
        d1 = img.find_lbp(face)
        if (d0 == None):
            d0 = d1
        else:
            dist = image.match_descriptor(d0, d1)
            img.draw_string(0, 10, "Match %d%%"%(dist))

        img.draw_rectangle(face)
    # 打印帧率
    img.draw_string(0, 0, "FPS:%.2f"%(clock.fps()))

```

具体接口定义请参考 [find_features](../../library/canmv/image.md#find_features)
