Snapshot - 拍照保存
================================

```python
# 这个例程展示如何拍照然后保存到文件系统中

import sensor, image

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

print("You're on camera!")
img = sensor.snapshot()             # 拍照，获取一张图像

# 保存图片为jpg，或者是bmp，或者是其他格式
img.save("example.jpg") # or "example.bmp" (or others)

print("Done! Reset the camera to see the saved image.")

```

具体接口定义请参考 [save](../../library/canmv/image.md#save)
