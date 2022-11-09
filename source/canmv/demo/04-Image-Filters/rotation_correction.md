Rotation Correction - 旋转矫正
================================

```python
# 旋转校正
#
# 这个例子展示了如何使用rotation_corr（）在图像上放大和缩小三维的视角旋转。 虽然
# 此演示为了好玩旋转图像，但您可以使用此功能来修复与CanMV的安装相关的透视问题。

import sensor, image, time

# 每帧旋转的角度…
X_ROTATION_DEGREE_RATE = 5
Y_ROTATION_DEGREE_RATE = 0.5
Z_ROTATION_DEGREE_RATE = 0
X_OFFSET = 0
Y_OFFSET = 0

ZOOM_AMOUNT = 1 # 较低的值缩小-较高的放大
FOV_WINDOW = 60 # 在0和180之间。表示在三维空间中旋转图像时场景窗口的视场。
                # 当接近于0时，随着窗口远离在三维空间中旋转的图像，直线会变得更直。
                # 在三维空间中，较大的值会使窗口更靠近图像，从而导致更多的透视畸变，
                # 有时会导致三维图像与场景窗口相交。

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

x_rotation_counter = 0
y_rotation_counter = 0
z_rotation_counter = 0

while(True):
    clock.tick()

    img = sensor.snapshot().rotation_corr(x_rotation = x_rotation_counter, \
                                          y_rotation = y_rotation_counter, \
                                          z_rotation = z_rotation_counter, \
                                          x_translation = X_OFFSET, \
                                          y_translation = Y_OFFSET, \
                                          zoom = ZOOM_AMOUNT, \
                                          fov = FOV_WINDOW)

    x_rotation_counter += X_ROTATION_DEGREE_RATE
    y_rotation_counter += Y_ROTATION_DEGREE_RATE
    z_rotation_counter += Z_ROTATION_DEGREE_RATE

    print(clock.fps())

```


具体接口定义请参考 [rotation_corr](../../library/canmv/image.md#rotation_corr)
