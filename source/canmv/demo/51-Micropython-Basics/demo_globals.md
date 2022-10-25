Globals - 全局变量
================================

```python

# 添加变量到全局变量中
def var_create(var):
    if var not in globals():
        globals()[var] = 1

# 从全局变量中移除变量
def var_remove(var):
    if var in globals():
        globals().pop(var)

var_create('global_var')

global_var = global_var + 1

print(global_var)

# It will be there until you turn it off (shutdown or restart)
# close()

var_remove('global_var')

print(global_var)

```
