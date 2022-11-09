Gamma Correction - Gamma 矫正
================================

```python
# gamma矫正
#
# 此示例显示关闭伽玛校正以使图像更亮。
# 伽马校正方法也可以固定对比度和亮度。

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

while(True):
    clock.tick()

    # 伽玛，对比度和亮度校正应用于每个颜色通道。
    # v这些值按比例缩放到每个图像类型的每个颜色通道的范围...
    img = sensor.snapshot().gamma_corr(gamma = 0.5, contrast = 1.0, brightness = 0.0)

    print(clock.fps())

```
