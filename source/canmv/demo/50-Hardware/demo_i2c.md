Demo I2C - I2C 例程
================================

```python
from machine import I2C
from fpioa_manager import fm

# i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29) # hardware i2c
# 软件I2C
i2c = I2C(I2C.I2C3, freq=100000, scl=30, sda=31) # software i2c
#i2c = I2C(I2C.I2C_SOFT, freq=100000, scl=28, sda=29,
          #gscl = fm.fpioa.GPIOHS1, gsda = fm.fpioa.GPIOHS2) # software i2c for the latest firmware
# 扫描I2C设备
devices = i2c.scan()
print(devices)

# 写数据
for device in devices:
    i2c.writeto(device, b'123')
    i2c.readfrom(device, 3)
    # tmp = bytearray(6)
    # i2c.readfrom_into(device, tmp, True)
```

具体接口定义请参考 [I2C](../../library/micropython/spec/machine.I2C.md)
