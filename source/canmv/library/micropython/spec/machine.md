machine
================

## 函数
### machine.unique_id()

获取唯一 ID

#### 返回值

32 字节的唯一ID

### machine.reset()

重启板子

### machine.reset_cause()

获取重启原因

#### 返回值

参考 [重启原因](#重启原因)

## 常量

### 重启原因

* machine.PWRON_RESET
* machine.HARD_RESET
* machine.WDT_RESET
* machine.WDT1_RESET
* machine.SOFT_RESET
