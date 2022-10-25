Yolo Hand Detect - Yolo 手掌检测
====================================

```python
import sensor, image, time, lcd
from maix import KPU
import gc


lcd.init()                          # 初始化LCD显示屏
sensor.reset()                      # 复位并初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 设置摄像头输出格式为 RGB565
sensor.set_framesize(sensor.QVGA)   # 设置摄像头输出大小为 QVGA (320x240)
sensor.skip_frames(time = 1000)      # 等待摄像头稳定
clock = time.clock()                # 创建一个clock对象，用来计算帧率

#检测模型需要320*256图输入，这里初始化一个image
od_img = image.Image(size=(320,256))

anchor = (0.8125, 0.4556, 1.1328, 1.2667, 1.8594, 1.4889, 1.4844, 2.2000, 2.6484, 2.9333)
# 创建一个kpu对象，用于人脸检测
kpu = KPU()
print("ready load model")
# 加载模型
kpu.load_kmodel("/sd/KPU/yolo_hand_detect/hand_detect.kmodel")
# yolo2初始化
kpu.init_yolo2(anchor, anchor_num=5, img_w=320, img_h=240, net_w=320 , net_h=256 ,layer_w=10 ,layer_h=8, threshold=0.7, nms_value=0.3, classes=1)

while True:
    gc.collect()
    clock.tick()                        # 更新计算帧率的clock
    img = sensor.snapshot()             # 拍照，获取一张图像
    a = od_img.draw_image(img, 0,0)     # 将img图像写到od_img图像的坐标（0,0）位置处
    od_img.pix_to_ai()                  # 对rgb565的image生成ai运算需要的r8g8b8格式存储
    kpu.run_with_output(od_img)         # 对输入图像进行kpu运算
    dect = kpu.regionlayer_yolo2()      # yolo2后处理
    fps = clock.fps()                   # 获取帧率
    # 画出结果
    if len(dect) > 0:
        print("dect:",dect)
        for l in dect :
            a = img.draw_rectangle(l[0],l[1],l[2],l[3], color=(0, 255, 0))

    a = img.draw_string(0, 0, "%2.1ffps" %(fps), color=(0, 60, 128), scale=2.0)
    lcd.display(img)

# 创建的kpu对象去初始化，释放模型内存
kpu.deinit()

```
