Video Record - 视频录制 （AVI）
================================

```python
import sensor, image, lcd, time

lcd.init(freq=15000000)                 # 初始化屏幕显示
sensor.reset()                          # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565)     # 设置摄像头输出格式为 RGB565
sensor.set_framesize(sensor.QVGA)       # 设置摄像头输出大小为 QVGA (320x240)

sensor.set_hmirror(1)                   # 设置摄像头水平镜像
sensor.set_vflip(1)                     # 设置摄像头垂直翻转

sensor.run(1)
sensor.skip_frames(30)                  # 跳过30帧等待出图稳定

import video

# 新建视频文件
v = video.open("/sd/capture.avi", audio = False, record=1, interval=200000, quality=50)

# 拍照并进行avi录制
tim = time.ticks_ms()
for i in range(50):
    tim = time.ticks_ms()
    img = sensor.snapshot()
    lcd.display(img)
    img_len = v.record(img)
    # print("record",time.ticks_ms() - tim)

print("record_finish")
v.record_finish()
v.__del__()
```

```python
import sensor, image, lcd, time
# 播放录制的视频
v = video.open("/sd/capture.avi")
print(v)
v.volume(50)
while True:
    if v.play() == 0:
        print("play end")
        break

print("play finish")
v.__del__()

lcd.clear()

```

具体接口定义请参考 [Video](../../../library/canmv/video.md)
