`CanMV`
===========

`CanMV` 扩展库是在标准`Micropython`基础上扩展的关于机器视觉的一系列模块，可以让用户方便快捷的实现机器视觉相关的功能。

* [maix](./maix/README.md): `k210`芯片相关的一些功能模块，比如`KPU`,`FPIOA`等
* [sensor](./sensor.md): 摄像头图像采集以及控制
* [image](./image.md): `CPU`图像处理算法，比如找圆，找正方形，识别二维码等等
* [lcd](./lcd.md): 屏幕显示控制
* [touchscreen](./touchscreen.md): 触摸屏触摸数据读取
* [audio](./audio.md): 录音和播放音频
* [video](./video.md): 录制和播放`avi`视频
* [modules](./modules/README.md): 外挂的一些外设模块驱动

> 第三方库

* [ulab](./third-party/ulab.md): `numpy`的`Micropython`实现

> 冻结的`py`脚本

为方便用户使用，我们写了一些辅助脚本冻结到固件中

* [board](./built-in/board.md): 描述板子信息
* [fpioa_manager](./built-in/fpioa_manager.md): `FPIOA`管理模块
