In Memory Basic Frame Differencing - 简单帧差分
======================================================

```python
# 简单帧差分例程
#
# 此示例演示了如何在CanMV Cam中使用帧差异。 它被称为基本帧差异，因为没有背景图像更新。 
# 因此，随着时间的推移，背景图像可能会发生变化而导致问题。

import sensor, image, os, time

TRIGGER_THRESHOLD = 5

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
sensor.set_auto_whitebal(False)     # 关掉自动白平衡
clock = time.clock()                # 创建一个clock对象，用来计算帧率

# 从主帧缓冲区的RAM中取出以分配第二帧缓冲区。
# 帧缓冲区中的RAM比MicroPython堆中的RAM多得多。
# 但是，在执行此操作后，您的某些算法的RAM会少得多......
# 所以，请注意现在摆脱RAM问题要容易得多。
# 然而，帧差分不会占用帧缓冲区中的大量额外空间。
# 但是，如果你这样做，像AprilTags这样的东西会起作用，也可能不会起作用...
extra_fb = image.Image(size=(sensor.width(), sensor.height()))

print("About to save background image...")
sensor.skip_frames(time = 2000) # Give the user time to get ready.
# extra_fb.replace(sensor.snapshot())
extra_fb.draw_image(sensor.snapshot(), 0, 0)
print("Saved background image - Now frame differencing!")

while(True):
    clock.tick()                # 更新计算帧率的clock
    img = sensor.snapshot()     # 拍照，获取一张图像

    # 用 "abs(NEW-OLD)" 帧差替换图像。
    img.difference(extra_fb)

    hist = img.get_histogram()
    # 下面的代码通过比较第99百分位值（例如，非离群值最大值与第90百分位值（例如非最大值）来工作。
    # 两个值之间的差异将随着差异图像看起来像素变化而增大。
    diff = hist.get_percentile(0.99).l_value() - hist.get_percentile(0.90).l_value()
    triggered = diff > TRIGGER_THRESHOLD

    print(clock.fps(), triggered) # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。

```
