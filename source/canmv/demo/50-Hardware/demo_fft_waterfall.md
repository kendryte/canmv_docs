Demo FFT Waterfull - FFT 瀑布图
================================

```python
from maix import GPIO, I2S,  FFT
import image, lcd, math
from fpioa_manager import fm
import KPU as kpu

sample_rate = 11025     # 采样率
sample_points = 1024    # 采样点数
fft_points = 512        # FFT点数
hist_x_num = 128        # X轴步进

lcd.init()              # 初始化屏幕显示

# 控制IO8输出低电平，关闭WiFi(在某些板子上需要这样配置)
fm.register(8,  fm.fpioa.GPIO0)
wifi_en=GPIO(GPIO.GPIO0,GPIO.OUT)
wifi_en.value(0)

# CanMV 开发板引脚配置
fm.register(9,fm.fpioa.I2S0_IN_D0, force=True)
fm.register(8,fm.fpioa.I2S0_WS, force=True)
fm.register(7,fm.fpioa.I2S0_SCLK, force=True)
# SipeedDock 开发吧引脚配置
#fm.register(20,fm.fpioa.I2S0_IN_D0, force=True)
#fm.register(30,fm.fpioa.I2S0_WS, force=True)    # 19 on Go Board and Bit(new version)
#fm.register(32,fm.fpioa.I2S0_SCLK, force=True)  # 18 on Go Board and Bit(new version)

# 使用I2S0 进行数据采集，需要与上边引脚配置一致
rx = I2S(I2S.DEVICE_0)
# 配置通道0为接收，标准对齐模式
rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode = I2S.STANDARD_MODE)
# 设置采样率
rx.set_sample_rate(sample_rate)
# 新建一个图像用来显示
img = image.Image(size=(128,128))
# 图片转为灰度图
img=img.to_grayscale()

while True:
    # 录音
    audio = rx.record(sample_points)
    # FFT计算
    fft_res = FFT.run(audio.to_bytes(),fft_points)
    # 转频谱
    fft_amp = FFT.amplitude(fft_res)
    # 裁切图片
    img_tmp = img.cut(0,0,128,127)
    # 画图
    img.draw_image(img_tmp, 0,1)
    # 绘制频谱图
    for i in range(hist_x_num):
        img[i] = fft_amp[i]
    del(img_tmp)
    # 转瀑布图
    imgc = img.to_rainbow(1)
    # 显示
    lcd.display(imgc)
    del(imgc)
    fft_amp.clear()
```

具体接口定义请参考 [FFT](../../library/canmv/maix/maix.FFT.md)
