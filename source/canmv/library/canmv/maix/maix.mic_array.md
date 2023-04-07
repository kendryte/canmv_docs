maix.mic_array
=============

## `maix.mic_array`

Mic-Array 麦克风阵列，麦克风阵列硬件上的 pin io 支持自定义配置。


| No. | MaixGo(mic.init()默认配置 IO) | 说明 |
| --- | --- | --- |
| MIC_D0 | 23 | --- |
| MIC_D1 | 22 | --- |
| MIC_D2 | 21 | --- |
| MIC_D3 | 20 | --- |
| MIC_WS | 19 | --- |
| MIC_SCLK | 18 | --- |
| --- | --- | --- |
| LED_DAT | 24 | SK9822 DAT |
| LED_CLK | 25 | SK9822 CLK |


### 例程

以下是适用于CanMV_K210开发板的声源定位

```python
from maix import mic_array as mic
import lcd

lcd.init()
#mic.init()  # 默认配置
mic.init(i2s_d0=12, i2s_d1=13, i2s_d2=14, i2s_d3=15, i2s_ws=24, i2s_sclk=25, sk9822_dat=11, sk9822_clk=10)# for CanMV_K210

#mic.init(i2s_d0=20, i2s_d1=21, i2s_d2=15, i2s_d3=8, i2s_ws=7, i2s_sclk=6, sk9822_dat=25, sk9822_clk=24)# for maix cube

while True:
    imga = mic.get_map()            # 获取声音源分布图像
    b = mic.get_dir(imga)           # 计算、获取声源方向
    a = mic.set_led(b,(0,0,255))    # 配置 RGB LED 颜色值
    imgb = imga.resize(160,160)
    imgc = imgb.to_rainbow(1)       # 将图像转换为彩虹图像
    a = lcd.display(imgc)
mic.deinit()
```
例程源码位于：[canmv_examples](https://github.com/kendryte/canmv_examples/blob/main/50-Hardware/demo_mic_array.py)

更详细的信息建议前往: [这里](https://wiki.sipeed.com/hardware/zh/modules/micarray.html?highlight=%E9%BA%A6%E5%85%8B%E9%A3%8E) 查看
