Face Mask Detect - 人脸口罩检测
================================

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

#人脸检测模型需要320*256图输入，这里初始化一个image
od_img = image.Image(size=(320,256), copy_to_fb=False)

anchor = (0.156250, 0.222548, 0.361328, 0.489583, 0.781250, 0.983133, 1.621094, 1.964286, 3.574219, 3.94000)
# 创建一个kpu对象，用于人脸检测
kpu = KPU()
print("ready load model")
# 加载模型
kpu.load_kmodel("/sd/KPU/face_mask_detect/detect_5.kmodel")
# yolo2初始化
kpu.init_yolo2(anchor, anchor_num=5, img_w=320, img_h=240, net_w=320 , net_h=256 ,layer_w=10 ,layer_h=8, threshold=0.7, nms_value=0.4, classes=2)

while True:
    #print("mem free:",gc.mem_free())
    clock.tick()                        # 更新计算帧率的clock
    img = sensor.snapshot()             # 拍照，获取一张图像
    a = od_img.draw_image(img, 0,0)     # 将img图像写到od_img图像的坐标（0,0）位置处
    od_img.pix_to_ai()                  # 对rgb565的image生成ai运算需要的r8g8b8格式存储
    kpu.run_with_output(od_img)         # 对输入图像进行kpu运算
    dect = kpu.regionlayer_yolo2()      # yolo2后处理
    fps = clock.fps()                   # 获取帧率
    # 画出人脸框，并判断是否带有口罩
    if len(dect) > 0:
        print("dect:",dect)
        for l in dect :
            if l[4] :
                a = img.draw_rectangle(l[0],l[1],l[2],l[3], color=(0, 255, 0))
                a = img.draw_string(l[0],l[1]-24, "with mask", color=(0, 255, 0), scale=2)
            else:
                a = img.draw_rectangle(l[0],l[1],l[2],l[3], color=(255, 0, 0))
                a = img.draw_string(l[0],l[1]-24, "without mask", color=(255, 0, 0), scale=2)

    a = img.draw_string(0, 0, "%2.1ffps" %(fps), color=(0, 60, 128), scale=2.0)
    lcd.display(img)
    gc.collect()

# 创建的kpu对象去初始化，释放模型内存
kpu.deinit()

```
