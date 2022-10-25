Play WAV - WAV 播放
================================

```python
from fpioa_manager import *
from maix import I2S, GPIO
import audio

########### settings ############
WIFI_EN_PIN = 8
# AUDIO_PA_EN_PIN = None  # Bit Dock and old MaixGo
AUDIO_PA_EN_PIN = 32
# AUDIO_PA_EN_PIN = 2     # Maixduino

# 控制IO8输出低电平，关闭WiFi(在某些板子上需要这样配置)
fm.register(WIFI_EN_PIN, fm.fpioa.GPIO0, force=True)
wifi_en = GPIO(GPIO.GPIO0, GPIO.OUT)
wifi_en.value(0)

# 如果音频输出有PA控制，则控制打开
if AUDIO_PA_EN_PIN:
    fm.register(AUDIO_PA_EN_PIN, fm.fpioa.GPIO1, force=True)
    wifi_en = GPIO(GPIO.GPIO1, GPIO.OUT)
    wifi_en.value(1)

# I2S0 引脚配置
fm.register(34, fm.fpioa.I2S0_OUT_D1, force=True)
fm.register(35, fm.fpioa.I2S0_SCLK, force=True)
fm.register(33, fm.fpioa.I2S0_WS, force=True)

# 初始化I2S0
wav_dev = I2S(I2S.DEVICE_0)

# 初始化WAV播放对象
player = audio.Audio(path="/sd/6.wav")
# 设置音量
player.volume(40)

# 解析WAV头部信息
wav_info = player.play_process(wav_dev)
print("wav file head information: ", wav_info)

# 配置I2S0 通道1为输出
wav_dev.channel_config(wav_dev.CHANNEL_1, I2S.TRANSMITTER, resolution=I2S.RESOLUTION_16_BIT,
                       cycles=I2S.SCLK_CYCLES_32, align_mode=I2S.RIGHT_JUSTIFYING_MODE)
# 设置I2S0采样率
wav_dev.set_sample_rate(wav_info[1])

# 循环播放WAV
while True:
    ret = player.play()
    if ret == None:
        print("format error")
        break
    elif ret == 0:
        print("end")
        break
player.finish()

```

具体接口定义请参考 [WDT](../../../library/canmv/audio.md)
