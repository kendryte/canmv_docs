Object tracking with keypoints - 特征点检测
================================================

```python
# 利用特征点检测特定物体例程。
# 向相机显示一个对象，然后运行该脚本。 一组关键点将被提取一次，然后
# 在以下帧中进行跟踪。 如果您想要一组新的关键点，请重新运行该脚本。
# 注意：请参阅文档以调整find_keypoints和match_keypoints。

import sensor, time, image

sensor.reset() # 复位并初始化摄像头

# 设置摄像头
sensor.set_contrast(3)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.VGA)
sensor.set_windowing((320, 240))
sensor.set_pixformat(sensor.GRAYSCALE)

sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False, value=100)

def draw_keypoints(img, kpts):
    if kpts:
        print(kpts)
        img.draw_keypoints(kpts)
        img = sensor.snapshot()
        time.sleep_ms(1000)

kpts1 = None
#kpts1保存目标物体的特征，可以从文件导入特征，但是不建议这么做。
#kpts1 = image.load_descriptor("/desc.orb")
#img = sensor.snapshot()
#draw_keypoints(img, kpts1)

clock = time.clock()
while (True):
    clock.tick()
    img = sensor.snapshot()
    if (kpts1 == None):
        #如果是刚开始运行程序，提取最开始的图像作为目标物体特征，kpts1保存目标物体的特征
        #默认会匹配目标特征的多种比例大小，而不仅仅是保存目标特征时的大小，比模版匹配灵活。
        kpts1 = img.find_keypoints(max_keypoints=150, threshold=10, scale_factor=1.2)
        draw_keypoints(img, kpts1)
    else:
        # 当与最开始的目标特征进行匹配时，默认设置normalized=True，只匹配目标特征的一种大小。
        kpts2 = img.find_keypoints(max_keypoints=150, threshold=10, normalized=True)
        if (kpts2):
            match = image.match_descriptor(kpts1, kpts2, threshold=85)
            if (match.count()>10):
                #在匹配到的目标特征中心画十字和矩形框。
                img.draw_rectangle(match.rect())
                img.draw_cross(match.cx(), match.cy(), size=10)

            print(kpts2, "matched:%d dt:%d"%(match.count(), match.theta()))
            # 不建议draw_keypoints画出特征关键点。
            # 注意:如果你想绘制关键点，取消注释
            #img.draw_keypoints(kpts2, size=KEYPOINTS_SIZE, matched=True)

    img.draw_string(0, 0, "FPS:%.2f"%(clock.fps())) #打印帧率。
```

具体接口定义请参考 [find_keypoints](../../library/canmv/image.md#find_keypoints)
