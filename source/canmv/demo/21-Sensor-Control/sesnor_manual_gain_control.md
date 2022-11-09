Sensor Manual Gain Control - 摄像头增益控制
================================================

```python
# 感光元件手动增益控制
#
# 此示例展示了如何手动控制相机传感器的增益，而不是让自动增益控制运行。

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

# 更改此值以调整增益。尝试10.0 / 0 / 0.1 /等。
GAIN_SCALE = 1.0

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)

# 打印出初始增益以进行比较。
print("Initial gain == %f db" % sensor.get_gain_db())

sensor.skip_frames(time = 2000)     # 跳过2000帧
clock = time.clock()                # 创建一个clock对象，用来计算帧率

# 您必须关闭自动曝光控制和自动白平衡，否则他们将更改图像曝光以撤消您放置的任何增益设置...
sensor.set_auto_exposure(False)
sensor.set_auto_whitebal(False)
# 需要让以上设置生效
sensor.skip_frames(time = 500)

current_gain_in_decibels = sensor.get_gain_db()
print("Current Gain == %f db" % current_gain_in_decibels)

# 默认情况下启用自动增益控制（AGC）。 调用以下功能可禁用传感器自动增益控制。 
# 额外的“gain_db”参数在AGC被禁用后覆盖自动增益值。
sensor.set_auto_gain(False, \
    gain_db = current_gain_in_decibels * GAIN_SCALE)

print("New gain == %f db" % sensor.get_gain_db())
# sensor.get_gain_db()返回精确的相机传感器增益分贝。
# 但是，这可能与命令的数量不同，因为传感器代码将增益转换为小的和大的增益值，这些值不能接受所有可能的值...

# 如果你想重新开启自动增益，请执行：sensor.set_auto_gain(True) 
# 请注意，相机传感器将根据需要更改增益。

# 执行：sensor.set_auto_gain(False)。禁用增益值更新但不更改相机传感器确定的增益值。

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像
    print(clock.fps())  # 打印帧率

```

具体接口定义请参考 [set_auto_gain](../../library/canmv/sensor.md#set_auto_gain)
