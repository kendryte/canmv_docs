Demo I2C Slave - I2C 从机例程
================================

```python
from machine import I2C

count = 0

# 接收到数据
def on_receive(data):
    print("on_receive:",data)

# 发送数据
def on_transmit():
    global count
    count = count+1
    print("on_transmit, send:",count)
    return count

# 事件回调
def on_event(event):
    print("on_event:",event)

# 初始化I2C
i2c = I2C(I2C.I2C0, mode=I2C.MODE_SLAVE, scl=30, sda=31, addr=0x24, addr_size=7, on_receive=on_receive, on_transmit=on_transmit, on_event=on_event)

```

具体接口定义请参考 [I2C](../../library/micropython/spec/machine.I2C.md)
