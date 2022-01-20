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
