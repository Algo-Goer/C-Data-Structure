"""
用Python实现栈。
假设列表的尾部是栈的顶端。
当栈增长时（push操作），新元素会被添加到列尾部。pop操作同样修改这一端
"""
class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)  # append()方法 # append(item) 

    def pop(self):
        return self.items.pop()  # pop()方法 # pop() 

    def peek(self):
        return self.items[len(self.items) - 1] # 返回顶端元素，也就是最后一个元素
    
    def size(self):
        return len(self.items)

