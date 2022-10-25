Mnist - 手写数字识别
================================

```python
import sensor, image, time, lcd
from maix import KPU
import gc


lcd.init()                          # 初始化LCD显示屏
sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.set_windowing((224, 224))    # 摄像头输出开窗
sensor.skip_frames(time = 500)      # 等待摄像头稳定
clock = time.clock()                # 创建一个clock对象，用来计算帧率

# 创建一个kpu对象
kpu = KPU()
# 加载模型
kpu.load_kmodel("/sd/KPU/mnist/uint8_mnist_cnn_model.kmodel")

while True:
    gc.collect()
    img = sensor.snapshot()                 # 拍照，获取一张图像
    img_mnist1=img.to_grayscale(1)          # 将图片转为灰度图
    img_mnist2=img_mnist1.resize(112,112)   # 将图片缩放为112x112
    a=img_mnist2.invert()                   # 反转图片
    a=img_mnist2.strech_char(1)             # 预处理图片
    a=img_mnist2.pix_to_ai()                # 对image处理生成ai运算需要的r8g8b8格式存储

    # 对输入图像进行kpu运算，并得出结果
    out = kpu.run_with_output(img_mnist2, getlist=True)
    max_mnist = max(out)
    index_mnist = out.index(max_mnist)
    #score = KPU.sigmoid(max_mnist)
    display_str = "num: %d" % index_mnist
    print(display_str)
    a=img.draw_string(4,3,display_str,color=(0,0,0),scale=2)
    lcd.display(img)

# 创建的kpu对象去初始化，释放模型内存
kpu.deinit()

```
