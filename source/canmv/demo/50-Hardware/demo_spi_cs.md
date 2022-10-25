Demo SPI - SPI 例程
================================

```python
import time
from machine import SPI
from fpioa_manager import fm

# 将IO25配置为GPIOHS10
fm.register(25,fm.fpioa.GPIOHS10, force=True)#cs

from maix import GPIO

# 配置CS脚为输出
cs = GPIO(GPIO.GPIOHS10, GPIO.OUT)

# SPI引脚配置
fm.register(24,fm.fpioa.SPI1_D0, force=True)#mosi
fm.register(23,fm.fpioa.SPI1_D1, force=True)#miso
fm.register(22,fm.fpioa.SPI1_SCLK, force=True)#sclk
# 配置SPI1
spi1 = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=10000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB)

# SPI读写数据
while True:
  w = b'\xFF'
  r = bytearray(1)
  cs.value(0)
  print(spi1.write_readinto(w, r))
  cs.value(1)
  print(w, r)
  time.sleep(0.1)

'''
from machine import SPI
spi1 = SPI(SPI.SPI1, mode=SPI.MODE_MASTER, baudrate=10000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=28, mosi=29, miso=30)
w = b'1234'
r = bytearray(4)
spi1.write(w)
spi1.write_readinto(w, r)
spi1.read(5, write=0x00)
spi1.readinto(r, write=0x00)
'''

```

具体接口定义请参考 [SPI](../../library/micropython/spec/machine.SPI.md)
