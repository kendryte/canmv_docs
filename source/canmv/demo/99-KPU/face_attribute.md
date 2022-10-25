Face Attribute - 人脸属性检测
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

anchor = (0.893, 1.463, 0.245, 0.389, 1.55, 2.58, 0.375, 0.594, 3.099, 5.038, 0.057, 0.090, 0.567, 0.904, 0.101, 0.160, 0.159, 0.255)
# 创建一个kpu对象，用于人脸检测
kpu = KPU()
print("ready load model")
kpu.load_kmodel("/sd/KPU/face_attribute/face_detect.kmodel") # 加载模型
# yolo2初始化
kpu.init_yolo2(anchor, anchor_num=9, img_w=320, img_h=240, net_w=320 , net_h=256 ,layer_w=10 ,layer_h=8, threshold=0.7, nms_value=0.2, classes=1)

ld5_kpu = KPU() # 创建一个kpu对象，用于人脸5关键点检测
print("ready load model")
ld5_kpu.load_kmodel("/sd/KPU/face_attribute/ld5.kmodel")

fac_kpu = KPU() # 创建一个kpu对象，用于人脸属性检测
print("ready load model")
fac_kpu.load_kmodel("/sd/KPU/face_attribute/fac.kmodel")

pos_face_attr = ["Male ", "Mouth Open ", "Smiling ", "Glasses"]
neg_face_attr = ["Female ", "Mouth Closed", "No Smile", "No Glasses"]

# 标准人脸关键点坐标
FACE_PIC_SIZE = 128
dst_point =[(int(38.2946 * FACE_PIC_SIZE / 112), int(51.6963 * FACE_PIC_SIZE / 112)),
            (int(73.5318 * FACE_PIC_SIZE / 112), int(51.5014 * FACE_PIC_SIZE / 112)),
            (int(56.0252 * FACE_PIC_SIZE / 112), int(71.7366 * FACE_PIC_SIZE / 112)),
            (int(41.5493 * FACE_PIC_SIZE / 112), int(92.3655 * FACE_PIC_SIZE / 112)),
            (int(70.7299 * FACE_PIC_SIZE / 112), int(92.2041 * FACE_PIC_SIZE / 112)) ]

RATIO = 0.08 # 人脸外接框放大比例
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

while 1:
    gc.collect()
    #print("mem free:",gc.mem_free())
    clock.tick()                        # 更新计算帧率的clock
    img = sensor.snapshot()             # 拍照，获取一张图像
    a = od_img.draw_image(img, 0,0)     # 将img图像写到od_img图像的坐标（0,0）位置处
    od_img.pix_to_ai()                  # 对rgb565的image生成ai运算需要的r8g8b8格式存储
    kpu.run_with_output(od_img)         # 对输入图像进行kpu运算
    dect = kpu.regionlayer_yolo2()      # yolo2后处理
    fps = clock.fps()                   # 获取帧率
    if len(dect) > 0:
        print("dect:",dect)
        for l in dect :
            # 对检测到的人脸框扩大RATIO倍后裁剪
            x1, y1, cut_img_w, cut_img_h = extend_box(l[0], l[1], l[2], l[3], scale=RATIO) # 扩大人脸框
            face_cut = img.cut(x1, y1, cut_img_w, cut_img_h) # 从img中裁剪出人脸图
            a = img.draw_rectangle(l[0],l[1],l[2],l[3], color=(0, 255, 0)) # 画人脸框
            face_cut_128 = face_cut.resize(128, 128) # 对人脸图调整大小到128*128
            face_cut_128.pix_to_ai() # 对rgb565格式的128人脸图生成ai运算需要的rgb888格式存储
            out = ld5_kpu.run_with_output(face_cut_128, getlist=True) # kpu运算并获取结果
            #print("out:",len(out))
            face_key_point = []
            for j in range(5): # 根据结果算出人脸5关键点，并在图中标出
                x = int(KPU.sigmoid(out[2 * j])*cut_img_w + x1)
                y = int(KPU.sigmoid(out[2 * j + 1])*cut_img_h + y1)
                a = img.draw_cross(x, y, size=5, color=(0, 0, 255))
                face_key_point.append((x,y))
            T = image.get_affine_transform(face_key_point, dst_point) #由关键点算出变换矩阵
            a = image.warp_affine_ai(img, face_cut_128, T) # 相似变换修正人脸图
            # face_cut_128.ai_to_pix()
            # img.draw_image(face_cut_128, 0,0)
            out2 = fac_kpu.run_with_output(face_cut_128, getlist=True) # 检测人脸属性获取结果
            del face_key_point
            if out2 is not None:
                for i in range(4):
                    th = KPU.sigmoid(out2[i])
                    if th >= 0.7:
                        a = img.draw_string(l[0]+l[2], l[1]+i*16, "%s" %(pos_face_attr[i]), color=(255, 0, 0), scale=1.5)
                    else:
                        a = img.draw_string(l[0]+l[2], l[1]+i*16, "%s" %(neg_face_attr[i]), color=(0, 0, 255), scale=1.5)
            del (face_cut_128)
            del (face_cut)

    a = img.draw_string(0, 0, "%2.1ffps" %(fps), color=(0, 60, 255), scale=2.0)
    lcd.display(img)

# 创建的kpu对象去初始化，释放模型内存
kpu.deinit()
ld5_kpu.deinit()
fac_kpu.deinit()

```
