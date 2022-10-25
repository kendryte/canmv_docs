Video Play - 视频播放 （AVI)
================================

```python
from maix import GPIO, I2S

from fpioa_manager import fm
import lcd
import video
import time

# AUDIO_PA_EN_PIN = None  # Bit Dock and old MaixGo
AUDIO_PA_EN_PIN = 32
# AUDIO_PA_EN_PIN = 2     # Maixduino

# 初始化屏幕显示
lcd.init()

# 初始化I2S0
i2s = I2S(I2S.DEVICE_0)

# 配置I2S通道1为输出，用来播放视频剩余
i2s.channel_config(i2s.CHANNEL_1, I2S.TRANSMITTER, resolution=I2S.RESOLUTION_16_BIT,
                       cycles=I2S.SCLK_CYCLES_32, align_mode=I2S.RIGHT_JUSTIFYING_MODE)

# 如果音频输出有PA控制，则控制打开
if AUDIO_PA_EN_PIN:
    fm.register(AUDIO_PA_EN_PIN, fm.fpioa.GPIO1, force=True)
    wifi_en = GPIO(GPIO.GPIO1, GPIO.OUT)
    wifi_en.value(1)

# I2S0 引脚配置
fm.register(34,  fm.fpioa.I2S0_OUT_D1, force=True)
fm.register(35,  fm.fpioa.I2S0_SCLK, force=True)
fm.register(33,  fm.fpioa.I2S0_WS, force=True)

# 打开视频文件
v = video.open("/sd/badapple.avi")
print(v)
# 设置音量
v.volume(50)
# 播放视频
while True:
    if v.play() == 0:
        print("play end")
        break
v.__del__()

```

具体接口定义请参考 [Video](../../../library/canmv/video.md)
