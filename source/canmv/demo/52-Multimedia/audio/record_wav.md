record_wav
================================

```python
import image, lcd, time
import audio
from maix import GPIO, I2S
from fpioa_manager import fm

# user setting
sample_rate   = 16000
record_time   = 4  #s
# default seting
sample_points = 2048
wav_ch        = 2

# 控制IO8输出低电平，关闭WiFi(在某些板子上需要这样配置)
fm.register(8,  fm.fpioa.GPIO0, force=True)
wifi_en = GPIO(GPIO.GPIO0, GPIO.OUT)
wifi_en.value(0)

# I2S0 引脚配置
fm.register(20,fm.fpioa.I2S0_IN_D0, force=True)
fm.register(19,fm.fpioa.I2S0_WS, force=True)    # 19 on Go Board and Bit(new version)
fm.register(21,fm.fpioa.I2S0_SCLK, force=True)  # 18 on Go Board and Bit(new version)

# 使用I2S0 进行数据采集
rx = I2S(I2S.DEVICE_0)
# 配置通道0为接收
rx.channel_config(rx.CHANNEL_0, rx.RECEIVER, align_mode=I2S.STANDARD_MODE)
# 设置采样率
rx.set_sample_rate(sample_rate)
print(rx)

# 初始化WAV播放对象，录音保存到指定文件
recorder = audio.Audio(path="/sd/record.wav", is_create=True, samplerate=sample_rate)

queue = []

frame_cnt = record_time*sample_rate//sample_points

# 录音
for i in range(frame_cnt):
    tmp = rx.record(sample_points*wav_ch)
    if len(queue) > 0:
        ret = recorder.record(queue[0])
        queue.pop(0)
    rx.wait_record()
    queue.append(tmp)
    print(str(i) + ":" + str(time.ticks()))

recorder.finish()
```

具体接口定义请参考 [I2S](../../../library/canmv/maix/maix.I2S.md)
