Demo FFT Spectrum - FFT 频谱图
================================

```python
from maix import GPIO, I2S, FFT
import image, lcd, math

from fpioa_manager import fm

sample_rate = 38640         # 采样率
sample_points = 1024        # 采样点数
fft_points = 512            # FFT点数
hist_x_num = 50             # X轴步进

lcd.init(freq=15000000)     # 初始化屏幕显示

# 控制IO8输出低电平，关闭WiFi(在某些板子上需要这样配置)
fm.register(8,  fm.fpioa.GPIO0, force=True)
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
img = image.Image()
if hist_x_num > 320:
    hist_x_num = 320
hist_width = int(320 / hist_x_num)#changeable
x_shift = 0
while True:
    # 录音
    audio = rx.record(sample_points)
    # FFT计算
    fft_res = FFT.run(audio.to_bytes(),fft_points)
    # 转频谱
    fft_amp = FFT.amplitude(fft_res)
    # 清空上一次运行绘制的图像
    img = img.clear()
    x_shift = 0
    # 绘制频谱图并显示
    for i in range(hist_x_num):
        if fft_amp[i] > 240:
            hist_height = 240
        else:
            hist_height = fft_amp[i]
        img = img.draw_rectangle((x_shift,240-hist_height,hist_width,hist_height),[255,255,255],2,True)
        x_shift = x_shift + hist_width
    lcd.display(img)
    fft_amp.clear()

```

具体接口定义请参考 [FFT](../../library/canmv/maix/maix.FFT.md)
