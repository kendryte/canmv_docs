maix.KPU - OLD
===========================

> 本文档接口定义与[V1.0.5](https://github.com/kendryte/canmv/releases/tag/v1.0.5)及其之前的固件对应，新版本固件请参考 [maix.KPU - NEW](./maix.KPU_NEW.md)

KPU是通用的神经网络处理器，它可以在低功耗的情况下实现卷积神经网络计算，时时获取被检测目标的大小、坐标和种类，对人脸或者物体进行检测和分类。

* KPU 具备以下几个特点：
  * 支持主流训练框架按照特定限制规则训练出来的定点化模型
  * 对网络层数无直接限制，支持每层卷积神经网络参数单独配置，包括输入输出通道数目、输入输 出行宽列高
  * 支持两种卷积内核 1x1 和 3x3
  * 支持任意形式的激活函数
  * 实时工作时最大支持神经网络参数大小为 5.5MiB 到 5.9MiB
  * 非实时工作时最大支持网络参数大小为（Flash 容量-软件体积）

## 类 `maix.KPU`

### 构造函数

```python
kpu = KPU() 
```

创建一个KPU类

### 函数

#### `load_kmodel`

```python
kpu.load_kmodel(file_path)
kpu.load_kmodel(flash_offset, size)
```

从文件系统或者flash中加载模型

##### 参数

`文件系统加载` 和 `flash地址加载` 方式只能二选一，不需要关键词，直接传参即可

文件系统加载方式：
* `file_path`: 模型在文件系统中为文件名， 如 `“/sd/xxx.kmodel”`

flash地址加载方式：
* `flash_offset`: 模型在 flash 中的偏移大小，如 `0xd00000` 表示模型烧录在13M起始的地方, `0x300000`表示在 `Flash` `3M`的地方
* `size` : 模型大小

##### 返回值

* 无

##### 例子

```python
from maix import KPU
kpu = KPU()
## kpu.load_kmodel(0x300000, 1536936)
kpu.load_kmodel("/sd/voc20_detect.kmodel")
```

#### `init_yolo2`

```python
kpu.init_yolo2(anchor, anchor_num=5, 
                img_w=320, img_h=240, 
                net_w=320 , net_h=240,
                layer_w=10 ,layer_h=8, 
                threshold=0.7, 
                nms_value=0.4, 
                classes=1)
```

为`yolo2`网络模型传入初始化参数， 只有使用`yolo2`时使用

##### 参数

必须参数：
* `anchor`: 锚点参数与模型参数一致，同一个模型这个参数是固定的，和模型绑定的（训练模型时即确定了）， 不能改成其它值。

可选参数：
* `anchor_num`:  anchor 的锚点数， 这里固定为 `len(anchors)//2`，默认值为5
* `img_w`: 输入图像的宽，决定了画框边界，如果送入kpu的图是由一张小尺寸图扩充而来，该值可以设为原图宽，默认值为320
* `img_h`: 输入图像的高，决定了画框边界，如果送入kpu的图是由一张小尺寸图扩充而来，该值可以设为原图高，默认值为240
* `net_w`: 模型需要的图的宽，该值由训好的模型所决定，默认值为320
* `net_h`: 模型需要的图的高，该值由训好的模型所决定，默认值为240
* `layer_w`:模型层宽，该值由训好的模型所决定，默认值为10
* `layer_h`:模型层高，该值由训好的模型所决定，默认值为8
* `threshold`: 概率阈值， 只有是这个物体的概率大于这个值才会输出结果， 取值范围：[0, 1]，默认值为0.7
* `nms_value`: box_iou 门限, 为了防止同一个物体被框出多个框，当在同一个物体上框出了两个框，这两个框的交叉区域占两个框总占用面积的比例 如果小于这个值时， 就取其中概率最大的一个框，默认值为0.4
* `classes`: 要分辨的目标类数量，该值由训好的模型所决定，默认值为1

##### 返回值

* 无

##### 例子

```python
from maix import KPU
kpu = KPU()
kpu.load_kmodel("/sd/voc20_detect.kmodel")
anchor = (1.3221, 1.73145, 3.19275, 4.00944, 5.05587, 8.09892, 9.47112, 4.84053, 11.2364, 10.0071)
kpu.init_yolo2(anchor, anchor_num=5, img_w=320,img_h=240, net_w=320,net_h=256, layer_w=10,layer_h=8, threshold=0.5, nms_value=0.2, classes=20)
```

#### `run_with_output`

```python
kpu.run_with_output(img [,getlist=False [, get_feature=False]])
```

将输入图像送入kpu运算，并获取结果

##### 参数

必须参数：
* `img`: 可以是从 sensor 采集到`Image`图像类，也可以传入图片文件路径。

可选参数：
* `getlist`:  为True则返回浮点数列表，默认False
* `get_feature`: 为True则返回L2归一化后的浮点特征值（最大允许256），默认False

注意：`getlist`与`get_feature`参数是二选一的关系，决定了最后返回什么样的数据。

##### 返回值

`getlist`与`get_feature`为Flase时返回None

##### 例子

```python
from maix import KPU
kpu = KPU()
kpu.load_kmodel("/sd/voc20_detect.kmodel")
anchor = (1.3221, 1.73145, 3.19275, 4.00944, 5.05587, 8.09892, 9.47112, 4.84053, 11.2364, 10.0071)
kpu.init_yolo2(anchor, anchor_num=5, img_w=320,img_h=240, net_w=320,net_h=256, layer_w=10,layer_h=8, threshold=0.5, nms_value=0.2, classes=20)
img = sensor.snapshot()
kpu.run_with_output(img)
```

以上为节选代码，并不是完整部分，详细请看20物体分类具体的代码

#### `regionlayer_yolo2`

```python
dect = kpu.regionlayer_yolo2()
```

yolo2运算，并获取结果

##### 参数

* 无

##### 返回值

返回一个二维列表，每个子列表代表一个识别到的目标物体，目标物体信息列表包含以下6个数据：
- `x`, `y`, `w`, `h`：代表目标框的左上角x,y坐标，以及框的宽w高h
- `class`: 类别序号
- `prob` : 概率值，范围：[0, 1]

##### 例子

```python
from maix import KPU
kpu = KPU()
kpu.load_kmodel("/sd/voc20_detect.kmodel")
anchor = (1.3221, 1.73145, 3.19275, 4.00944, 5.05587, 8.09892, 9.47112, 4.84053, 11.2364, 10.0071)
kpu.init_yolo2(anchor, anchor_num=5, img_w=320,img_h=240, net_w=320,net_h=256, layer_w=10,layer_h=8, threshold=0.5, nms_value=0.2, classes=20)
img = sensor.snapshot()
kpu.run_with_output(img)
dect = kpu.regionlayer_yolo2()
print("dect:",dect)
```

以上为节选代码，并不是完整部分，详细请看20物体分类具体的代码

#### `feature_compare`

```python
score = kpu.feature_compare(feature_0, feature_1)
```

特征比对，比对两个特征数据并给出相似度分数

##### 参数

* `feature_0`: 特征数据0，浮点列表, 最大允许256
* `feature_1`: 特征数据1，浮点列表, 最大允许256

##### 返回值

* `score`: 相似度分数

##### 例子

```python
feature = kpu.run_with_output(img, get_feature = True)
score = kpu.feature_compare(record_feature, feature)
print(score)
```

以上为节选代码，并不是完整部分，详细请看自分类具体的代码

#### `deinit`

```python
kpu.deinit()
```

KPU去初始化函数，释放模型占用的内存， 立即释放， 但是变量还在，可以使用`del kpu_object` 的方式删除，
另外也可以直接只使用`del kpu_object`来标记对象已被删除，下一次`GC`进行内存回收或者手动调用`gc.collect()`时，会自动释放内存

##### 例子

```python
from maix import KPU
import gc
kpu = KPU()
kpu.load_kmodel("/sd/voc20_detect.kmodel")
kpu.deinit()
del kpu
gc.collect()
```

#### `sigmoid`

```python
KPU.sigmoid(f)
```

将数据归一化到[0, 1]范围

##### 参数

* `f`: 浮点数

##### 返回值

* 浮点数

#### `softmax`

```python
KPU.softmax(f)
```

激活函数`softmax`，计算最大值

##### 参数

* `f`: 浮点数数组

##### 返回值

* 浮点数数组