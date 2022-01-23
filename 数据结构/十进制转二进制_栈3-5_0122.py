# 除以2算法
# 第一个余数就是个位数
from pythonds.basic import Stack
def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())  # 最后进的最先出，所以位数最高
    
    return binString