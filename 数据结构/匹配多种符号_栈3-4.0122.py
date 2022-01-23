from pythonds.basic import Stack

def parChecker(symbolString):
    s = Stack()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):  
                    # matches正则表达式语句
                    # 调用辅助函数来匹配符号
                    # 检测每一个从栈顶移除的符号是否与当前右括号相匹配
                    # 如果不匹配，balanced为False
                    balanced = False

        index = index + 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"

    return opens.index(open) == closers.index(close)
        