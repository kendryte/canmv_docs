Files - 文件操作
================================

```python
import uos

# 查看根目录下的文件以及文件夹
mount_points = uos.listdir("/")
for fs in mount_points:
    print("------------")
    print(" dir:", fs)
    uos.listdir("/"+fs)

# 读取main.py
with open('main.py', 'rb') as f:
# 	f.write('print(Hello, world!)\r\n')
    print(f.read())

```
