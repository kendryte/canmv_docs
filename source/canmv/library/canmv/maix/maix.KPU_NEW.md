maix.KPU - NEW
===========================

> 本文档接口定义与[V1.0.5](https://github.com/kendryte/canmv/releases/tag/v1.0.5)之后的固件对应，旧版本固件请参考 [maix.KPU - OLD](./maix.KPU.md)


KPU是通用的神经网络处理器，它可以在低功耗的情况下实现卷积神经网络计算，时时获取被检测目标的大小、坐标和种类，对人脸或者物体进行检测和分类。

* KPU 具备以下几个特点：
  * 支持主流训练框架按照特定限制规则训练出来的定点化模型
  * 对网络层数无直接限制，支持每层卷积神经网络参数单独配置，包括输入输出通道数目、输入输 出行宽列高
  * 支持两种卷积内核 1x1 和 3x3
  * 支持任意形式的激活函数
  * 实时工作时最大支持神经网络参数大小为 5.5MiB 到 5.9MiB
  * 非实时工作时最大支持网络参数大小为（Flash 容量-软件体积）


## 类 `KPU`

```python
kpu = maix.KPU()
```

创建一个`KPU`类，可进行图像计算，并获取计算结果

### 函数 `load`

```python
kpu.load(model_path)    # string
kpu.load(model_offset)  # int
```

从文件系统或者`Flash`加载模型

#### 参数

 和 `flash加载` 方式只能二选一，不需要关键词，直接传参即可

文件系统加载：

* `model_path`: 模型文件在文件系统中的存放路径， 如 `"/sd/xxx.kmodel"`

`Flash`加载：

* `model_offset`: 模型在 `Flash` 中的偏移，如 `0xd00000` 表示模型烧录在 `13M` 起始的地方, `0x300000` 表示模型烧录在 `3M` 起始的地方

#### 返回值

* 无

#### 例子

```python
from maix import KPU
kpu = KPU()
## kpu.load(0x300000)
kpu.load("/sd/xxx.kmodel")
```

### 函数 `run`

```python
kpu.run(img)
```

加载模型之后，对输入图像进行推理计算

#### 参数

* `img`： 等待计算的图像

若图像不是由`sensor.snapshot()`获得，则需要执行`img.pix_to_ai()`进行转换

如果图像大小与模型输入要求不一致，会返回`OsError`

#### 返回值

* 无

#### 例子

* 无

### 函数 `get_outputs`

```python
result = kpu.get_outputs([index = 0])
```

获取模型运行结果

#### 参数

* index: 可选参数，指定获取第 `N` 个输出，从 `0` 开始

#### 返回值

返回与模型输出相同大小的`List`

若模型有[Yolo2](#类-yolo2)或者[Lpr](#类-lpr)等后处理，则不需要手动获取输出

#### 例子

* 无

### 函数 `deinit`

```python
kpu.deinit()
```

释放类`KPU`相关资源

#### 参数

* 无

#### 返回值

* 无

#### 例子

* 无


## 类 `Act`

`Act`类主要是对[get_outputs](#函数-get_outputs)输出结果进行后处理

### 函数 `sigmoid`

```python
kpu = KPU()
result = kpu.Act.sigmoid(kpu_result)
```

将数据归一化到[0, 1]范围

#### 参数

* `kpu_result`: `KPU`获取到的运行结果

#### 返回值

* `result`: 浮点数, [0, 1]

#### 例子

```python
from maix import KPU
kpu = KPU()
kpu.load('/sd/xxx.kmodel')
img = sensor.snapshot()
kpu.run(img)
r = kpu.get_outputs()
result = kpu.Act.sigmoid(r)
```

### 函数 `softmax`

```python
kpu = KPU()
result = kpu.Act.softmax(kpu_result)
```

激活函数`softmax`，计算最大值

#### 参数

* `kpu_result`: `KPU`获取到的运行结果

#### 返回值

* `result`: 浮点数数组

#### 例子

```python
from maix import KPU
kpu = KPU()
kpu.load('/sd/xxx.kmodel')
img = sensor.snapshot()
kpu.run(img)
r = kpu.get_outputs()
result = kpu.Act.softmax(r)
```

## 类 `Feat`

`Feat`是为特征值计算与比对封装的类，请按需使用~

### 函数 `calculate`

```python
kpu = KPU()
img = sensor.snapshot()
kpu.run(img)
feature = kpu.Feat.calculate(kpu)
```

#### 参数

* `kpu`: `KPU` 类

#### 返回值

* `feature`: 计算得到的特征值

#### 例子

```python
from maix import KPU
kpu = KPU()
kpu.load('/sd/xxx.kmodel')
img = sensor.snapshot()
kpu.run(img)
feature = kpu.Feat.calculate(kpu)
```

### 函数 `compare`

```python
kpu = KPU()
kpu_result = kpu.get_outputs()
feature1 = kpu.Feat.calculate(kpu_result)

feature2 = [xxxxxx]
score = kpu.Feat.compare(feature1, feature2)
```

#### 参数

* `feature1`: 人脸特征值1
* `feature2`: 人脸特征值2

#### 返回值

* `score`: 两个特征值的相似度

#### 例子

```python
kpu = KPU()
kpu_result = kpu.get_outputs()
feature1 = kpu.Feat.calculate(kpu_result)

feature2 = [xxxxxx]
score = kpu.Feat.compare(feature1, feature2)
```

## 类 `Yolo2`

`Yolo2` 是对`yolo`网络模型所以须的一系列操作的封装

### 函数 `init`

```python
from maix import KPU
kpu = KPU()
kpu.load('/sd/xxx.kmodel')
yolo = kpu.Yolo2()
anchor = [xx,xx,xx,xx,xx...]
threshold = 0.5
nms = 0.3
yolo.init(anchor, threshold, nms)
```

#### 参数

`anchor`: 锚点参数与模型参数一致，同一个模型这个参数是固定的，和模型绑定的（训练模型时即确定了）， 不能改成其它值。

`threshold`: 概率阈值， 只有是这个物体的概率大于这个值才会输出结果， 取值范围：[0, 1]，默认值为0.5

`nms`: box_iou 门限, 为了防止同一个物体被框出多个框，当在同一个物体上框出了两个框，这两个框的交叉区域占两个框总占用面积的比例 如果小于这个值时， 就取其中概率最大的一个框，默认值为0.3

#### 返回值

* 无

#### 例子

* 无

### 函数 `deinit`

```python
from maix import KPU
kpu = KPU()
kpu.load('/sd/xxx.kmodel')
yolo = kpu.Yolo2()
anchor = [xx,xx,xx,xx,xx...]
threshold = 0.5
nms = 0.3
yolo.init(anchor, threshold, nms)
yolo.deinit()
```

释放类`Yolo2`申请的资源

#### 参数

* 无

#### 返回值

* 无

#### 例子

* 无

### 函数 `run`

```python
from maix import KPU
kpu = KPU()
kpu.load('/sd/xxx.kmodel')
yolo = kpu.Yolo2()
anchor = [xx,xx,xx,xx,xx...]
threshold = 0.5
nms = 0.3
yolo.init(anchor, threshold, nms)

img = sensor.snapshot()
kpu.run(img)
dect = yolo.run()

```

#### 参数

* 无

#### 返回值

返回一个二维列表，每个子列表代表一个识别到的目标物体，目标物体信息列表包含以下6个数据：
- `x`, `y`, `w`, `h`：代表目标框的左上角x,y坐标，以及框的宽w高h
- `class`: 类别序号
- `prob` : 概率值，范围：[0, 1]

#### 例子

* 无

### 例子

```python
import sensor, image, time, lcd, gc, cmath
from maix import KPU

lcd.init()                          # Init lcd display
lcd.clear(lcd.RED)                  # Clear lcd screen.

# sensor.reset(dual_buff=True)      # improve fps
sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.set_vflip(True)              # 翻转摄像头
sensor.set_hmirror(True)            # 镜像摄像头
sensor.skip_frames(time = 1000)     # Wait for settings take effect.
clock = time.clock()                # Create a clock object to track the FPS.

labels = ["face", "bike"] #类名称，按照label.txt顺序填写
anchor = (1.24, 1.12, 2.66, 2.64, 6.45, 2.81, 4.69, 4.38, 7.14, 4.06, 5.38, 6.60, 7.90, 5.80, 9.65, 5.74, 8.90, 6.86) # anchors,使用anchor.txt中第二行的值

kpu = KPU()
kpu.load(0x300000)

yolo = kpu.Yolo2()
yolo.init(anchor, 0.5, 0.3)

while(True):
    gc.collect()

    clock.tick()
    img = sensor.snapshot()

    kpu.run(img)
    dect = yolo.run()

    fps = clock.fps()

    if len(dect) > 0:
        for l in dect :
            a = img.draw_rectangle(l[0],l[1],l[2],l[3],color=(0,255,0))

            info = "%s %.3f" % (labels[l[4]], l[5])
            a = img.draw_string(l[0],l[1],info,color=(255,0,0),scale=2.0)
            print(info)
            del info

    a = img.draw_string(0, 0, "%2.1ffps" %(fps),color=(0,60,255),scale=2.0)
    lcd.display(img)
```

## 类 `Lpr`

`Lpr` 是对车牌识别模型所以须的一系列操作的封装

### 函数 `load`

```python
from maix import KPU
kpu = KPU()
kpu.load('/sd/xxx.kmodel')
lpr = kpu.Lpr()
#lpr.load(weight_path)
lpr.load(weight_offset, weight_size)
```

从文件系统或者`Flash`加载权重

#### 参数

文件系统加载 和 `flash加载` 方式只能二选一，不需要关键词，直接传参即可

文件系统加载：

* `weight_path`: 权重在文件系统中的存放路径， 如 `"/sd/xxx.bin"`

`Flash`加载：

* `weight_offset`: 权重文件在`Flash`中的偏移

* `weight_size`: 权重文件的大小

#### 返回值

* 无

#### 例子

* 无


### 函数 `deinit`

```python
from maix import KPU
kpu = KPU()
kpu.load('/sd/xxx.kmodel')
lpr = kpu.Lpr()
#lpr.load(weight_path)
lpr.load(weight_offset, weight_size)
lpr.deinit()
```

释放类`Lpr`申请的资源

#### 参数

* 无

#### 返回值

* 无

#### 例子

* 无

### 函数 `run`

```python
from maix import KPU
kpu = KPU()
kpu.load('/sd/xxx.kmodel')
lpr = kpu.Lpr()
#lpr.load(weight_path)
lpr.load(weight_offset, weight_size)
img = sensor.snapshot()
kpu.run(img)
List = lpr.run()
```

#### 参数

* 无

#### 返回值

* `List`: 车牌结果列表
    - List[0]: 省份id

    ("Wan", "Hu", "Jin", "Yu^", "Ji", "Sx", "Meng", "Liao", "Jl", "Hei", "Su", "Zhe", "Jing", "Min", "Gan", "Lu", "Yu", "E^", "Xiang", "Yue", "Gui^", "Qiong", "Cuan", "Gui", "Yun", "Zang", "Shan", "Gan^", "Qing", "Ning", "Xin")

    - List[1 ... 6]: 车牌号码
    
    ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

#### 例子

* 无

### 例子

```python
import sensor, image, time, lcd
from maix import KPU, utils
import gc

lcd.init()
sensor.reset()                      # Reset and initialize the sensor. It will
                                    # run automatically, call sensor.run(0) to stop
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 1000)     # Wait for settings take effect.
#sensor.set_hmirror(1)
#sensor.set_vflip(1)
clock = time.clock()                # Create a clock object to track the FPS.

province = ("Wan", "Hu", "Jin", "Yu^", "Ji", "Sx", "Meng", "Liao", "Jl", "Hei", "Su", "Zhe", "Jing", "Min", "Gan", "Lu", "Yu", "E^", "Xiang", "Yue", "Gui^", "Qiong", "Cuan", "Gui", "Yun", "Zang", "Shan", "Gan^", "Qing", "Ning", "Xin")
ads = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

anchor = (8.30891522166988, 2.75630994889035, 5.18609903718768, 1.7863757404970702, 6.91480529053198, 3.825771881004435, 10.218567655549439, 3.69476690620971, 6.4088204258368195, 2.38813526350986)
kpu = KPU()
kpu.load("/sd/KPU/licenseplate_recognization/lp_detect.kmodel")

yolo = kpu.Yolo2()
yolo.init(anchor, 0.7, 0.3)


lp_recog_kpu = KPU()
lp_recog_kpu.load("/sd/KPU/licenseplate_recognization/lp_recog.kmodel")

lpr = lp_recog_kpu.Lpr()
lpr.load("/sd/KPU/licenseplate_recognization/lp_weight.bin")


RATIO = 0.16
def extend_box(x, y, w, h, scale):
    x1_t = x - scale*w
    x2_t = x + w + scale*w
    y1_t = y - scale*h
    y2_t = y + h + scale*h
    x1 = int(x1_t) if x1_t>1 else 1
    x2 = int(x2_t) if x2_t<320 else 319
    y1 = int(y1_t) if y1_t>1 else 1
    y2 = int(y2_t) if y2_t<256 else 255
    cut_img_w = x2-x1+1
    cut_img_h = y2-y1+1
    return x1, y1, cut_img_w, cut_img_h

lp_index_list = []

while 1:
    clock.tick()
    img = sensor.snapshot()
    kpu.run(img)
    dect = yolo.run()
    fps = clock.fps()
    if len(dect) > 0:
        for l in dect :
            x1, y1, cut_img_w, cut_img_h= extend_box(l[0], l[1], l[2], l[3], scale=RATIO)
            lp_cut = img.cut(x1, y1, cut_img_w, cut_img_h)
            a=img.draw_rectangle(l[0],l[1],l[2],l[3], color=(255, 0, 0))
            lp_resize = lp_cut.resize(208,64)
            a=lp_resize.replace(vflip=0, hmirror=1)
            lp_resize.pix_to_ai()
            lp_recog_kpu.run(lp_resize)
            out = lpr.run()
            lp_index_list.clear()
            for n in out:
                max_score = max(n)
                index = n.index(max_score)
                lp_index_list.append(index)
            del (lp_cut)
            del (lp_resize)
            show_lp_str = "%s %s-%s%s%s%s%s" %(province[lp_index_list[0]], ads[lp_index_list[1]], ads[lp_index_list[2]],
                ads[lp_index_list[3]], ads[lp_index_list[4]], ads[lp_index_list[5]], ads[lp_index_list[6]])
            print(show_lp_str)
            a=img.draw_string(l[0], l[1]-20, show_lp_str, color=(255, 128, 0), scale=2.0)
    a=img.draw_string(0, 0, "%2.1ffps" %(fps), color=(255, 255, 0), scale=2.0)
    lcd.display(img)
    gc.collect()

kpu.deinit()
lp_recog_kpu.deinit()
```
