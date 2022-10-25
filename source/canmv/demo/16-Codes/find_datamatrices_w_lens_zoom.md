Find Data Matrices w/ Lens Zoom - DM码识别 带缩放矫正
=========================================================

```python
# Find Data Matrices w/ Lens Zoom Example

import sensor, image, time, math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((320, 240)) # 2x Zoom
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)  # 必须关闭此功能，以防止图像冲洗…
sensor.set_auto_whitebal(False)  # 必须关闭此功能，以防止图像冲洗…
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()

    matrices = img.find_datamatrices()
    for matrix in matrices:
        img.draw_rectangle(matrix.rect(), color = (255, 0, 0))
        print_args = (matrix.rows(), matrix.columns(), matrix.payload(), (180 * matrix.rotation()) / math.pi, clock.fps())
        print("Matrix [%d:%d], Payload \"%s\", rotation %f (degrees), FPS %f" % print_args)
    if not matrices:
        print("FPS %f" % clock.fps())

```

具体接口定义请参考 [find_datamatrices](../../library/canmv/image.md#find_datamatrices)
