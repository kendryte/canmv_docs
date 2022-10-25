Video Capture - 视频分帧播放（AVI）
================================

```python
import lcd
import video
import image

# 初始化屏幕显示
lcd.init()
# 打开视频
v = video.open("/sd/badapple_320_240_15fps.avi")
print(v)
# 新建图片对象
img = image.Image()
while True:
    # 从视频中采集一帧并显示
    status = v.capture(img)
    if status != 0:
        lcd.display(img)
    else:
        print("end")
        break
v.__del__()
```

具体接口定义请参考 [Video](../../../library/canmv/video.md)
