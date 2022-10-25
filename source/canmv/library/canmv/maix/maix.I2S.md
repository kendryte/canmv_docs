maix.I2S
=============

I2S模块主要用于驱动I2S设备，k210一共有3个I2S设备，每个设备一共有4个通道，在使用前需要对引脚进行映射管理


## 类 `maix.I2S`

### 构造函数

```python
from maix import I2S
i2s_dev = I2S(device_num)
```

新建一个 I2S 对象

#### 参数

`device_num` I2S号，使用指定的 I2S，可以通过 `I2S.` 按tab键来补全

#### 返回值

返回一个`I2S` 对象

### 函数

#### `channel_config`

```python
i2s_dev.channel_config(channel, mode, resolution, cycles, align_mode)
```

用于配置 I2S 通道，在此之前需要对引脚进行映射

##### 参数

* `channel`:    I2S通道编号

* `mode`:       通道传输模式，一共有接收和发送模式，录音为接受，播放为发送

* `resolution`: 通道分辨率，即接收数据位数

* `cycles`:     单个数据时钟数

* `align_mode`: 通道对齐模式

##### 返回值

无

#### `set_sample_rate`

```python
i2s_dev.set_sample_rate(sample_rate)
```

配置 I2S 采样率

##### 参数

`sample_rate`: int 类型，采样率

##### 返回值

无

#### `record`

```python
audio = i2s_dev.record(points)
```

使用I2S接收音频数据

##### 参数

* `points`: 一次采集的音频点数

##### 返回值

`audio`: 一个`audio`音频对象

#### `play`

```python
i2s_dev.play(audio)
```

使用I2S发送音频数据

##### 参数

* `audio`: 发送的音频对象

##### 返回值
无
