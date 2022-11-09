Demo MIC Array - MIC 阵列
================================

```python
from maix import mic_array as mic
import lcd

lcd.init()          # 初始化LCD显示屏
mic.init()          # 初始化MIC阵列
#mic.init(i2s_d0=23, i2s_d1=22, i2s_d2=21, i2s_d3=20, i2s_ws=19, i2s_sclk=18, sk9822_dat=24, sk9822_clk=25)

#mic.init(i2s_d0=20, i2s_d1=21, i2s_d2=15, i2s_d3=8, i2s_ws=7, i2s_sclk=6, sk9822_dat=25, sk9822_clk=24)# for maix cube

while True:
    imga = mic.get_map()        # 获取声谱图
    b = mic.get_dir(imga)       # 对声谱图进行分析
    a = mic.set_led(b,(0,0,255)) # 对LED进行更新
    # 显示声谱图到LCD
    imgb = imga.resize(160,160)
    imgc = imgb.to_rainbow(1)
    a = lcd.display(imgc)
mic.deinit()

```
