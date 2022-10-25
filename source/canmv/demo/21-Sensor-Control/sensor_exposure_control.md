Sensor Exposure Control - 摄像头曝光控制
==================================================

```python
# 感光元件曝光控制
#
# 此示例显示如何手动控制相机传感器的曝光，而不是让自动曝光控制运行。
# 增益和曝光控制之间有什么区别？
#
# 通过增加图像的曝光时间，您可以在相机上获得更多光线。这为您提供了最佳的信噪比。
# 您通常总是希望增加曝光时间...除非，当您增加曝光时间时，您会降低最大可能的帧速率，
# 如果图像中有任何移动，它将在更长的曝光时间内开始模糊。 
# 增益控制允许您使用模拟和数字乘法器增加每像素的输出......但是，它也会放大噪声。 
# 因此，最好尽可能让曝光增加，然后使用增益控制来弥补任何剩余的地画面。

# 我们可以通过在自动增益控制算法上设置增益上限来实现上述目的。 
# 一旦设置完毕，算法将不得不增加曝光时间以满足任何增益需求，而不是使用增益。 
# 然而，当照明变化相对于曝光恒定且增益变化时，这是以曝光时间的变化为代价的。

import sensor, image, time

# 更改此值以调整曝光。试试10.0 / 0.1 /等。
EXPOSURE_TIME_SCALE = 1.0

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)

# 打印出初始曝光时间以进行比较。
print("Initial exposure == %d" % sensor.get_exposure_us())

sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

# 您必须关闭自动增益控制和自动白平衡，否则他们将更改图像增益以撤消您放置的任何曝光设置...
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
# 需要让以上设置生效
sensor.skip_frames(time = 500)

current_exposure_time_in_microseconds = sensor.get_exposure_us()
print("Current Exposure == %d" % current_exposure_time_in_microseconds)

# 默认情况下启用自动曝光控制（AEC）。调用以下功能可禁用传感器自动曝光控制。 
# 另外“exposure_us”参数在AEC被禁用后覆盖自动曝光值。
sensor.set_auto_exposure(False, \
    exposure_us = int(current_exposure_time_in_microseconds * EXPOSURE_TIME_SCALE))

print("New exposure == %d" % sensor.get_exposure_us())
# sensor.get_exposure_us()以微秒为单位返回精确的相机传感器曝光时间。 
# 然而，这可能与命令的数量不同，因为传感器代码将曝光时间以微秒转换为行/像素/时钟时间，这与微秒不完全匹配...

# 如果要重新打开自动曝光，请执行以下操作：sensor.set_auto_exposure(True)
# 请注意，相机传感器将根据需要更改曝光时间。

# 执行：sensor.set_auto_exposure(False)，只是禁用曝光值更新，但不会更改相机传感器确定的曝光值。

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像
    print(clock.fps())              # 注意: 当连接电脑后，CanMV会变成一半的速度。当不连接电脑，帧率会增加。

```
