Demo I2S - I2S 例程
================================

```python
from maix import GPIO, I2S
import image, lcd, math, audio
from fpioa_manager import fm

sample_rate = 22050     # 采样率
sample_points = 1024    # 采样点数

# 使用I2S0 进行数据采集，需要与上边引脚配置一致
rx = I2S(I2S.DEVICE_0)
# 配置通道0为接收
rx.channel_config(I2S.CHANNEL_0, rx.RECEIVER, resolution = I2S.RESOLUTION_16_BIT, cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.STANDARD_MODE)
# 设置采样率
rx.set_sample_rate(sample_rate)

# 开发板引脚配置
fm.fpioa.set_function(pin=9, func=fm.fpioa.I2S0_IN_D0)
fm.fpioa.set_function(pin=8, func=fm.fpioa.I2S0_WS)
fm.fpioa.set_function(pin=7, func=fm.fpioa.I2S0_SCLK)

# 使用I2S2进行数据发送
tx = I2S(I2S.DEVICE_2)

# 配置通道1进行发送数据
tx.channel_config(I2S.CHANNEL_1, I2S.TRANSMITTER, resolution = I2S.RESOLUTION_16_BIT, cycles = I2S.SCLK_CYCLES_32, align_mode = I2S.RIGHT_JUSTIFYING_MODE)
# 设置采样率
tx.set_sample_rate(sample_rate)

# 开发板引脚配置
fm.fpioa.set_function(pin=34, func=fm.fpioa.I2S2_OUT_D1)
fm.fpioa.set_function(pin=35, func=fm.fpioa.I2S2_SCLK)
fm.fpioa.set_function(pin=33, func=fm.fpioa.I2S2_WS)

# 播放录音采集到的数据
while True:
    tx.play(rx.record(sample_points))

```

具体接口定义请参考 [I2S](../../library/canmv/maix/maix.I2S.md)
