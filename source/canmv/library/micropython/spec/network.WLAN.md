network.WLAN
===============

CanMV 的 wifi模块，适用于canmv_k1板上自带的esp32c3 wifi芯片，默认编译固件未启用，可以自行编译配置开启。
配置编译选项` Components configuration → Enbale micropython component → Micropython configurations → Modules configurations`下 `Enable esp32xx hosted driver`，并关闭`Enable WIZNET5K`

## 类 `network.WLAN` 或 `network.ESP32C3`

### 构造函数

```python
import network
nic = network.WLAN(network.STA_IF)
```

通过指定的参数新建一个 wifi station 对象。

#### 参数

* `network.STA_IF` : 站又名客户端，连接到上游WiFi接入点
* `network.AP_IF` : 接入点，允许其他WiFi客户端连接。

以下方法的可用性取决于接口类型。例如，只有STA接口可以`WLAN.connect()`连接到接入点。

### 函数

#### `active([is_active])`

```python
nic.active(is_active)
```

激活或停用网络接口。

##### 参数

* `is_active`: 0或1，`True`或 `False`。

##### 返回值

无

### 函数

#### `connect(ssid=None, key=None, *, bssid=None)`

```python
nic.connect('your-ssid', 'your-key')
```

使用指定的密钥连接到指定的无线网络。如果给定了*bssid*，则连接将被限制为具有该MAC地址的接入点（在这种情况下还必须指定*ssid*）。

##### 参数

* `ssid`: wifi网络名称字符串。
* `key`: wifi密码字符串。
* `auth`: `True`，支持wpa3加密。
* `bssid`: wifi接入点网络mac地址。

##### 返回值

无

### 函数

#### `disconnect`

```python
nic.disconnect()
```

断开与当前连接的无线网络的连接。

##### 参数

无

##### 返回值

无

### 函数

#### `scan`

```python
nic.scan()
```

扫描可用的无线网络。如果WLAN接口允许，隐藏网络（SSID未广播）也将被扫描。只能在STA接口上进行扫描。

##### 参数

无

##### 返回值

返回包含WiFi接入点信息的元组列表：  
(ssid, bssid, channel, RSSI, security, hidden)

*bssid*是访问点的硬件地址，二进制形式，返回为字节对象。

几种加密（security）方式:  
* 0 -- open
* 1 -- WEP
* 2 -- WPA-PSK
* 3 -- WPA2-PSK
* 4 -- WPA/WPA2-PSK
* 5 -- WPA2_ENTERPRISE
* 6 -- WPA3_PSK
* 7 -- WPA2_WPA3_PSK

可见性（hidden）参数:  
* 0 -- 可见
* 1 -- 隐藏

### 函数

#### `isconnected`

```python
nic.isconnected()
```

##### 参数

无

##### 返回值

在STA模式下，如果连接到WiFi接入点并且具有有效的IP地址，则返回`True`。  
在AP模式下，当站点连接时，返回`True`，否则返回`False `。

### 函数

#### `ifconfig([(ip, subnet, gateway, dns)])`

```python
nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
```

获取/设置IP级网络接口参数：IP地址、子网掩码、网关和DNS服务器。当在没有参数的情况下调用时，此方法返回具有上述信息的4元组。要设置上述值，请传递具有所需信息的4元组。

##### 参数

* `ip_tuple`: 设置ip信息的4元组参数
* `"dhcp"`: 传入`"dhcp"`字符串参数，用来主动申请dhcp。

##### 返回值

无传参调用则返回4元组的ip信息

### 函数

#### `config`

```python
nic.config('param')
nic.config(param=value, ...)
```

获取或设置常规网络接口参数。这些方法允许使用标准IP配置之外的其他参数（如“WLAN.ifconfig()”所处理的）。这些参数包括网络特定参数和硬件特定参数。对于设置参数，应使用关键字参数语法，可以同时设置多个参数。对于查询，参数名称应引用为字符串，一次只能查询一个参数。

```python
    # Set WiFi access point name (formally known as SSID) and WiFi channel
    ap.config(ssid='My AP', channel=11)
    # Query params one by one
    print(ap.config('ssid'))
    print(ap.config('mac'))
```

以下是通常支持的参数（特定参数的可用性取决于网络技术类型、驱动程序）。

| 参数      | 说明 | 
| :--       | :-- |
|mac        |MAC地址(bytes)         |
|ssid       |wifi接入点名称(string)     |
|channel    |wifi信道(int)             |
|hidden     |wifi ssid是否隐藏(boolean) |
|security   |支持的安全协议  |
|password   |访问密钥(string) |
|hostname   |将发送到DHCP（STA接口）和mDNS（如果支持，STA和AP）的主机名 |
|reconnects |尝试重新连接的次数（int，0=无，-1=无限制）  |
|txpower    |最大发射功率（dBm）(int)   |


##### 参数

支持设置的参数：channel, ssid, password, txpower

##### 返回值

支持获取的参数：ssid, mac, txpower


### 例程
wifi的使用例程请查看 [canmv_examples--esp32c3_wifi](https://github.com/kendryte/canmv_examples/tree/main/54-Network/esp32c3_wifi)