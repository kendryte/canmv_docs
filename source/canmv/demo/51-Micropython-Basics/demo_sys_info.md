Sys Info - 系统信息
================================

```python
import sys

# 打印系统信息

for i in range(0, 2):
    print("hello canmv")
    print("hello ", end="canmv\n")

print("implementation:", sys.implementation)
print("platform:", sys.platform)
print("path:", sys.path)
print("Python version:", sys.version)

print("please input string, end with Enter")
r = sys.stdin.readline()
w_len = sys.stdout.write(r)

```

具体接口定义请参考 [sys](../../library/micropython/sys.md)
