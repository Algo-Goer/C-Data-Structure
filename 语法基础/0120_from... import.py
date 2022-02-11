# 当以from...import语句导入模块时，Python会在当前源码文件（模块）的命名空间中新建相应命名
# 例如from model01 import cal_Average相当于
import model01
cal_Average = model01.cal_Average