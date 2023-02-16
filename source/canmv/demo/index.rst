`CanMV` 例程讲解
=======================

这里我们来讲解一下 `CanMV IDE` 中的例程


`Basics` - 基础示例
^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    01-Basics/helloworld.md

`Drawing` - 图像绘制元素
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    03-Drawing/arrow_drawing.md
    03-Drawing/circle_drawing.md
    03-Drawing/copy2fb.md
    03-Drawing/cross_drawing.md
    03-Drawing/ellipse_drawing.md
    03-Drawing/flood_fill.md
    03-Drawing/image_drawing.md
    03-Drawing/image_drawing_advanced.md
    03-Drawing/image_drawing_alpha_blending_test.md
    03-Drawing/keypoints_drawing.md
    03-Drawing/line_drawing.md
    03-Drawing/rectangle_drawing.md
    03-Drawing/text_drawing.md

`Image-Filters` - 图像滤波
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    04-Image-Filters/adaptive_histogram_equalization.md
    04-Image-Filters/blur_filter.md
    04-Image-Filters/cartoon_filter.md
    04-Image-Filters/color_bilateral_filter.md
    04-Image-Filters/color_binary_filter.md
    04-Image-Filters/color_light_removal.md
    04-Image-Filters/edge_filter.md
    04-Image-Filters/erode_and_dilate.md
    04-Image-Filters/gamma_correction.md
    04-Image-Filters/grayscale_bilateral_filter.md
    04-Image-Filters/grayscale_binary_filter.md
    04-Image-Filters/grayscale_light_removal.md
    04-Image-Filters/histogram_equalization.md
    04-Image-Filters/kernel_filters.md
    04-Image-Filters/lens_correction.md
    04-Image-Filters/linear_polar.md
    04-Image-Filters/log_polar.md
    04-Image-Filters/mean_filter.md
    04-Image-Filters/mean_adaptive_threshold_filter.md
    04-Image-Filters/median_filter.md
    04-Image-Filters/median_adaptive_threshold_filter.md
    04-Image-Filters/midpoint_filter.md
    04-Image-Filters/midpoint_adaptive_threshold_filter.md
    04-Image-Filters/mode_filter.md
    04-Image-Filters/mode_adaptive_threshold_filter.md
    04-Image-Filters/negative.md
    04-Image-Filters/perspective_correction.md
    04-Image-Filters/perspective_and_rotation_correction.md
    04-Image-Filters/rotation_correction.md
    04-Image-Filters/sharpen_filter.md
    04-Image-Filters/unsharp_filter.md
    04-Image-Filters/vflip_hmirror_transpose.md

`Snapshot` - 拍照
^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    05-Snapshot/snapshot.md
    05-Snapshot/emboss_snapshot.md

`Feature-Detection` - 特征检测
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    09-Feature-Detection/edges.md
    09-Feature-Detection/find_circles.md
    09-Feature-Detection/find_lines.md
    09-Feature-Detection/find_rects.md
    09-Feature-Detection/hog.md
    09-Feature-Detection/keypoints.md
    09-Feature-Detection/lbp.md
    09-Feature-Detection/linear_regression_fast.md
    09-Feature-Detection/linear_regression_robust.md
    09-Feature-Detection/selective_search.md
    09-Feature-Detection/template_matching.md

`Color-Tracking` - 颜色追踪
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    10-Color-Tracking/automatic_grayscale_color_tracking.md
    10-Color-Tracking/automatic_rgb565_color_tracking.md
    10-Color-Tracking/black_grayscale_line_following.md
    10-Color-Tracking/image_histogram_info.md
    10-Color-Tracking/image_statistics_info.md
    10-Color-Tracking/multi_color_code_tracking.md
    10-Color-Tracking/single_color_code_tracking.md


`Lcd` - 显示屏
^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    11-LCD-Shield/lcd.md

`Codes` - 扫码
^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    16-Codes/find_barcodes.md
    16-Codes/find_datamatrices.md
    16-Codes/find_datamatrices_w_lens_zoom.md
    16-Codes/qrcodes_with_lens_corr.md
    16-Codes/qrcodes_with_lens_zoom.md

`Frame-Differencing` - 图像比对
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    20-Frame-Differencing/in_memory_advanced_frame_differencing.md
    20-Frame-Differencing/in_memory_basic_frame_differencing.md
    20-Frame-Differencing/in_memory_shadow_removal.md
    20-Frame-Differencing/in_memory_structural_similarity.md

`Sensor-Control` - 摄像头控制
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    21-Sensor-Control/sensor_auto_gain_control.md
    21-Sensor-Control/sensor_exposure_control.md
    21-Sensor-Control/sensor_horizontal_mirror.md
    21-Sensor-Control/sensor_manual_whitebal_control.md
    21-Sensor-Control/sensor_vertical_flip.md
    21-Sensor-Control/sesnor_manual_gain_control.md

`April-Tags`
^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    26-April-Tags/find_apriltags.md
    26-April-Tags/find_apriltags_3d_pose.md
    26-April-Tags/find_apriltags_max_res.md
    26-April-Tags/find_apriltags_w_lens_zoom.md

`Hardware` - 硬件
^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    50-Hardware/demo_camera.md
    50-Hardware/demo_cpu.md
    50-Hardware/demo_fft_spectrum.md
    50-Hardware/demo_fft_waterfall.md
    50-Hardware/demo_gpio_intr.md
    50-Hardware/demo_gpio_led.md
    50-Hardware/demo_i2c.md
    50-Hardware/demo_i2c_oled.md
    50-Hardware/demo_i2c_slave.md
    50-Hardware/demo_i2s.md
    50-Hardware/demo_lcd.md
    50-Hardware/demo_mic_array.md
    50-Hardware/demo_onewire_ds18x20.md
    50-Hardware/demo_pwm.md
    50-Hardware/demo_spi_cs.md
    50-Hardware/demo_spi_soft.md
    50-Hardware/demo_timer.md
    50-Hardware/demo_touchscreen.md
    50-Hardware/demo_uart_loop.md
    50-Hardware/demo_uart_many.md
    50-Hardware/demo_wdt.md
    50-Hardware/fpioa_manager.md

`Micropython-Basics` - `Micropython` 基础示例
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    51-Micropython-Basics/demo_crc16.md
    51-Micropython-Basics/demo_files.md
    51-Micropython-Basics/demo_fs_info.md
    51-Micropython-Basics/demo_globals.md
    51-Micropython-Basics/demo_json.md
    51-Micropython-Basics/demo_logging.md
    51-Micropython-Basics/demo_ram_fs.md
    51-Micropython-Basics/demo_repl_to_read.md
    51-Micropython-Basics/demo_set_gc_heap_size.md
    51-Micropython-Basics/demo_sha256.md
    51-Micropython-Basics/demo_sys_info.md
    51-Micropython-Basics/demo_thread.md
    51-Micropython-Basics/demo_time.md
    51-Micropython-Basics/demo_view_mem.md
    51-Micropython-Basics/demo_yield.md
    51-Micropython-Basics/demo_yield_task.md

`Multimedia` - 多媒体
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    52-Multimedia/audio/play_wav.md
    52-Multimedia/audio/record_play.md
    52-Multimedia/audio/record_wav.md
    52-Multimedia/video/demo_video_capture.md
    52-Multimedia/video/demo_video_play.md
    52-Multimedia/video/demo_video_record.md

`Board` - 板子相关
^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    53-Board/board.md
    53-Board/config_maix_dock.md


`KPU` - 深度学习 (OLD)
^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    99-KPU/face_attribute.md
    99-KPU/face_detect_68lm.md
    99-KPU/face_mask_detect.md
    99-KPU/mnist.md
    99-KPU/self_learning.md
    99-KPU/voc20_object_detect.md
    99-KPU/yolo_face_detect.md
    99-KPU/yolo_hand_detect.md
