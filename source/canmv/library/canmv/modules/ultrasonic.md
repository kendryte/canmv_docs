Ultrasonic
=================

Grove - Ultrasonic Ranger(超声波测距模块)，只需要单根数据线

# 类 `modules.ultrasonic`

## 构造函数

```python
ultrasonic(gpiohs)
```

### 参数

* `gpiohs`: gpiohs 编号，需要先使用`fm`注册引脚,比如

```python
from fpioa_manager import *
from modules import ultrasonic

fm.register(board_info.D[6], fm.fpioa.GPIOHS0, force = True)
device = ultrasonic(fm.fpioa.GPIOHS0)
```

### 返回值

返回对象

## 函数 

### `measure`

```python
measure(unit, timeout)
```

#### 参数

* `unit`： 单位， 在下面的常数中取值
* `timeout`: 超时时间，单位为微秒（us）

## 常数

### `ultrasonic.UNIT_CM`

返回的距离的单位，厘米

### `ultrasonic.UNIT_INCH`

返回的距离的单位，英尺

