Sensor Auto Gain Control - 摄像头自动增益控制
=====================================================

```python
# 感光元件自动增益控制
#
# 这个例子展示了如何使用自动增益控制算法来控制感光元件的增益

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

sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565（也可以是GRAYSCALE）
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)

# 对于OV7725传感器，增益db上限最大约为24 dB。
sensor.set_auto_gain(True, gain_db_ceiling = 16.0) # 默认增益

#注意！如果在不调整曝光控制目标值的情况下将增益上限设置为低，那么如果曝光控制打开，您将从曝光控制中获得大量振荡。

sensor.skip_frames(time = 2000)     # 等待设置生效。
clock = time.clock()                # 创建一个clock对象，用来计算帧率

while(True):
    clock.tick()                    # 更新计算帧率的clock
    img = sensor.snapshot()         # 拍照，获取一张图像
    print("FPS %f, Gain %f dB, Exposure %d us" % \
        (clock.fps(), sensor.get_gain_db(), sensor.get_exposure_us()))

```

具体接口定义请参考 [set_auto_gain](../../library/canmv/sensor.md#set_auto_gain)
