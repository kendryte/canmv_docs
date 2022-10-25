Demo UART - UART 例程
================================

```python
from fpioa_manager import fm
from machine import UART
import time

# 引脚配置
fm.register(35, fm.fpioa.UART1_TX, force=True)
fm.register(34, fm.fpioa.UART1_RX, force=True)
fm.register(33, fm.fpioa.UART2_TX, force=True)
fm.register(32, fm.fpioa.UART2_RX, force=True)

# 初始化UART1和UART2
uart_A = UART(UART.UART1, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)
uart_B = UART(UART.UART2, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)

# 测试串口收发
write_bytes = b'hello world'
for i in range(20):
    uart_A.write(write_bytes)
    time.sleep_ms(1)
    if uart_B.any():
        read_data = uart_B.read()
        if read_data:
            print("write_bytes = ", write_bytes)
            print("read_data = ", read_data)
            if read_data == write_bytes:
                print("baudrate:115200 bits:8 parity:0 stop:0 ---check Successfully")

uart_A.deinit()
uart_B.deinit()
del uart_A
del uart_B

```

具体接口定义请参考 [UART](../../library/micropython/spec/machine.UART.md)
