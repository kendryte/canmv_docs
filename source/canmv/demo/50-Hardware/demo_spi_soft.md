Demo SPI SOFT - 软SPI
================================

```python
from machine import SPI
from maix import GPIO
from fpioa_manager import fm

mosi=25
miso=24
cs=23
clk=22

# 配置软件SPI
spi = SPI(SPI.SPI_SOFT, mode=SPI.MODE_MASTER, baudrate=400*1000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=clk, mosi=mosi, miso=miso)
fm.register(cs, fm.fpioa.GPIO6, force=True)
cs = GPIO(GPIO.GPIO6, GPIO.OUT)

# read spi flash id
while True:
    cs.value(0)
    write_data = bytearray([0x90, 0x00, 0x00, 0x00])
    spi.write(write_data)
    id_buf = bytearray(2)
    spi.readinto(id_buf, write=0xff)
    work_data = id_buf
    cs.value(1)
    print(work_data)
    
```

具体接口定义请参考 [SPI](../../library/micropython/spec/machine.SPI.md)
