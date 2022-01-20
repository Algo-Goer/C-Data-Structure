**目录**
[toc]

**106APrimer写**
- 快速入门仅仅指知识密度由于在时间轴中被压缩而变大，并知晓语法规则和常用库，会用面向对象设计代码，看得懂无复杂算法的代码
- 门槛低的东西意味着红海，所以不太可能一天学精Python
- 唯手熟尔，以一万行代码为能力值度量单位

## 1. 完整的代码文件
```Python
#encoding=utf8

"""
这个模块可以打印出指定年月的日历
模块名称：model01.py
"""

# 引入日历模块

# noinspection PyUnresolvedReferences
import calendar

# 定义全局变量
g_iYear = 2022
g_iMonth = 1
g_strMsg = "----------------------"


# 定义函数
def showCalendar():
    # 定义局部变量
    strtip = "输出" + str(g_iYear) + "年" + str(g_iMonth) + "月的日历："

    cal = calendar.month(g_iYear, g_iMonth)

    # 输出信息
    print(strtip)
    print(g_strMsg)
    print(cal)


# main函数，程序入口
if __name__ == "__main__":
    showCalendar()

```

<br>

![](https://files.mdnice.com/user/19687/edc8c418-c486-4fad-97d7-2ad9e307fb5a.png)


<br>

## 2. 解读
- Python程序第一行用来指定解释器，例如`#!E:\DevSys\python\python`，用`#!`特殊表示符开头。如果不指定解释器（本代码无），则Python用默认解释器
- 第二行用来指定本源代码文件所用的编码格式，大部分编辑器默认用UTF-8编码格式
- 连续三个双引号之后的是文档说明部分。也可以用连续三个单引号开始。文档说明非必需，但强烈建议关键地方给代码以清晰描述，利人利己
- import语句导入Python模块。一个模块是一段已写好的可执行代码，可以用Python或第三方语言例如C/C++等编写。在Python程序文件中，可随时随地用import语句导入Python的内置函数模块，例如calendar是一个内置函数模块
- 之后定义了三个全局变量。可以看出，Python在定义变量时无需声明变量类型，它会自动根据变量内容设定其类型
- 之后定义了无参数函数showCalendar()，函数没有return
- 之后__name__是一个标识模块名称的系统内建变量（可认为一个源代码文件就是一个模块）。这两行意思是：若当前源代码文件(model01.py)作为被调用模块导入到其他文件，则__name__的值为"model01.py"，此时语句`if__name__=="__main__"`后面的部分会跳过，不被执行；如果model01.py是主模块（调用其他模块的模块），那么__name__值为`"__main__"`，解释器便会执行`if __name__=="__main__"`语句后面部分。这两行可写可不写，但写上是好习惯

<br>

## 3. 基础语法
### 3.1 文件编码格式
```Python
#encoding=utf8
#encoding:utf8
#coding=utf8
#-*- coding:utf8 -*-
```
源代码编码格式设置必须在其他代码之前进行。没设置默认UTF-8编码
### 3.2 代码注释
以#开头，可以独立一行，也可以放在语句后面。
```Python
# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
```
在使用三个连续单引号或双引号时，需配对用。

### 3.3 标识符命名规则
标识符是用来标识源代码中的变量、函数、类等对象的字符串。规则如下：
- 标识符大小写敏感
- 第一个字符必须是字母或下划线_,不能以数字开头，其他部分可由字母、数字和下划线组成
- 长度不限
- 不能与关键字同名
- 不能使用Python内置函数名或内置数据类型作为标识符名，如不能用int、float等命名其他变量，因为它们是内置数据类型的名称
- 在3.x版本中，只要属于Unicode编码的字符，都可以充当标识符的组成部分，如“身高”也可以作为一个变量的名称
- 以下划线(_)开头的标识符有特殊含义，如下：
  - 源代码文件中，以单下划线开始的变量`_var`属于`本模块的私有变量`，其他模块不能调用
  - 在类的定义中，以单下划线开始的成员变量`_var`是保护变量，只有类和子类能访问，外部模块需通过类提供的接口进行访问，不能通过from import等方式导入。不过对于目前版本的Python（作者用3.6版本），这还只是一条约定，
  - 在类的定义中，以连续两个或以上  下划线开始，且没有以两个或以上  下划线结尾的成员变量(__var/___var)叫做`私有变量`，只有类本身自己能访问，连子类也不能访问这个变量
  - 以连续两个下划线开头和结尾的变量`__var__`，代表特殊方法或特定用途的标识，如__init__()代表了类的构造函数。
- 常量名应为大写加下划线（如MAX_OVERFLOW）
  <BR>
  

Python中有一个机制：私有变量矫直(Private name mangling)——私有变量会在代码生成之前被转换为公有，转换规则是在变量前端插入类名，再在类名前端加入一个下划线，如类A里的__private标识符将被转换为_A__private

### 3.4 代码缩进

```Python
age = 18
if age < 21:
    print("学生")
    print("好好学习Python")
print("***跳出if***")
```
在Python中，利用缩进表示语句块开始和退出，而非用花括号或某种关键字。增加缩进表示语句块开始，减少缩进表示语句块退出。
            
根据PEP 8(Python Enhancement Proposals)规定，建议用4个空格表示每级缩进，不过实际编写中可以自定义空格数。不建议用Tab设定缩进，更不建议Tab和空格混合用。
            
虽然缩进的空格数可自定义，**但同一个代码块的语句必须包含相同缩进空格数**。Python对代码缩进要求非常严格，如果不采用合理的代码缩进，将有语法异常错误。
            
### 3.5 语句与行
一般一行写一条，语句后不需要分号。也可以一行写多条，语句之间用分号分隔。如果一条语句很长，可以每行之间用反斜杠`\`拼接：
```Python
varOne = 11
varTwo = 22
varThree = 33
total = varOne + \
    varTwo + \
    varThree

print(total); # 不加分号也可输出66
```
![](https://files.mdnice.com/user/19687/89414557-8c69-4cac-94c0-ecc79f1aff87.png)

实际开发中，这种一条语句写在多行的情况比较常见，特别是对字符串进行多行拼接时。比如数据库查询用到SQL语句，由于SQL语句一般非常长，为阅读方便，需要换行书写：
```Python
# 字符串的换行

# 方法一
strSql = "SELECT uid, uname \
    FROM tuser \
    WHERE uname = 'zhangsan'"
print(strSql)

# 方法二
strSql = "SELECT uid, uname " \
    "FROM tuser " \
    "WHERE uname = 'zhangsan'"
print(strSql)
```

![](https://files.mdnice.com/user/19687/58356afd-26ee-4072-9441-c2d21aa34309.png)

方法一只用了一堆双引号，方法二用了三对双引号。方法一输出的空格更多且非必需。所以实践中，**强烈建议用方法二**，不仅可读性更强，而且可用空格对齐语句，使代码更工整。
            
特别地，在()、[]或{}中的多行语句，不需要使用反斜杠\。
```Python
items = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five'] 
```

一段代码在一行中有多条语句，用于多个简单变量赋值:    
```Python            
var1= 5; var2= 66; var3 = 77
vi = vj = vk = "LILOVEU" 
```

### 3.6 模块导入
#### 3.6.1 import语句
import或者from...import语句。
            
在Python中，模块是一个包含已经定义的函数和变量以及可执行语句的源代码文件，后缀名为.py。模块可以被别的程序导入，以便使用该模块中的函数等对象。
        
一条import语句可以同时导入多个模块。
           
import语句可以放在代码文件任何地方，只要在使用被导入模块的对象前导入即可。当解释器遇到import语句时，会按照一定搜索路径导入指定的模块。

比如有一个源文件model01.py:
```Python
# Filename:model01.py
from numpy import average


def print_Info( par ):
    print ("Output: ", par)
    return

def cal_Average(num1, num2):
    average = (num1 + num2) / 2;
    return(average)
```

另外一个文件Test.py需要引用model01.py中的函数print_Info()：
```Python
# Filename:Test.py

# 导入模块
import model01

# 调用model01模块中的函数
model01.print_Info("Hello")
```

![](https://files.mdnice.com/user/19687/90dc4982-cb79-4caf-a43a-d1859be0c423.png)
一个模块只会被导入一次，不管执行了多少次import。如果导入模块名称太长，可以通过as子句为导入的模块指定一个别名，注意别名不要与系统关键字或其他变量重名，格式：
```Python
import module1 as alias1, module2 as alias2, ... moduleN as aliasN
```
#### 3.6.2 from...import语句
这个语句允许Python从模块中只导入指定的部分到当前命名空间中
            