Structural Similarity (SSIM) - 结构相似性帧差分
==================================================

```python
# 结构相似性（SSIM）示例
#
# 此示例展示了如何在CanMV Cam上使用SSIM算法来检测两个图像之间的差异。 
# SSIM算法比较两个图像之间的8×8像素块以确定两个图像之间的相似性得分。

import sensor, image, os, time

# 如果sim.min() 低于此值，则图像可能已更改。
MIN_TRIGGER_THRESHOLD = -0.4

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
print("Saved background image!")

while(True):
    clock.tick()                # 更新计算帧率的clock
    img = sensor.snapshot()     # 拍照，获取一张图像
    sim = img.get_similarity(extra_fb)
    change = "- Change -" if sim.min() < MIN_TRIGGER_THRESHOLD else "- No Change -"

    print(clock.fps(), change, sim)

```

具体接口定义请参考 [get_similarity](../../library/canmv/image.md#get_similarity)
