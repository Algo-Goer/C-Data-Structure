"""
将列表头部作为栈顶端。
不过在这种情况下，便无法使用pop方法和append方法，
而必须要用`pop方法`和`insert方法`显式地访问下标为0的元素
"""
from importlib_metadata import re


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == [] # 判断是否为空数组
    
    def push(self, item):
        self.items.insert(0, item)  # 不用append()，而是用insert()方法
    
    def pop(self):
        return self.items.pop[0]    # pop[0]
    
    def peek(self):
        return self.items[0]   # 返回头部元素

    def size(self):
        return len(self.items)