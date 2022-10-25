Copy image to framebuffer - 加载图片到IDE的图像预览
=========================================================

```python
# 这个例程展示如何加载自定义图片在IDE的图像预览框中显示

import sensor, image, time

# 虽然不需要拍照，但是依然需要初始化摄像头
sensor.reset()

# 摄像头设置
sensor.set_contrast(1)
sensor.set_gainceiling(16)

# 设置摄像头输出格式
sensor.set_framesize(sensor.QQVGA)
sensor.set_pixformat(sensor.GRAYSCALE)

# 加载图片
img = image.Image("/example.bmp", copy_to_fb=True)

# 添加一个延时，让IDE能够读取到图像
time.sleep_ms(500)
```
