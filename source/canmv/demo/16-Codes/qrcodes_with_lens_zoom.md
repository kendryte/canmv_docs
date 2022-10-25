QRCode - 二维码识别  带缩放矫正
================================

```python
# QRCode Example

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
# sensor.set_windowing((240, 240)) # look at center 240x240 pixels of the VGA resolution.
# sensor.set_hmirror(True)
# sensor.set_vflip(True)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # 必须关闭此功能，以防止图像冲洗…
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    for code in img.find_qrcodes():
        img.draw_rectangle(code.rect(), color = 127)
        print(code)
    print(clock.fps())

```

具体接口定义请参考 [find_qrcodes](../../library/canmv/image.md#find_qrcodes)
