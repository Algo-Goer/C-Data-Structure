class Node(object):                        '''节点类'''
    def __init__(self, item):
        self.elem = elem
        self.next = None                   # 初始设置下一节点为空
class SingleLinkList(object):              '''创建单链表'''
    def __init__(self, node = None):
# 使用一个默认参数，传入头节点；没有传入参数时，默认头节点为空
        self.__head = node
    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None
    def length(self):                      '''链表长度'''
        cur = self.__head                  # cur游标，用来移动遍历节点
        count = 0                          # count记录数量
        while cur != None:
            count += 1
            cur = cur.next
            return count
    def travel(self):                      '''遍历整个列表'''
        cur = self.__head      
        while cur != None:
            print(cur.elem, end = '')
            cur = cur.next
        print("\n")
    def add(self. item):                   '''链表头部添加元素'''
        node = Node(item)
        node.next = self.__head
        self.__head = node
    def.append(self. item):                '''链表尾部添加元素'''
        node = Node(item)
        #特殊情况下，当链表为空时没有next，所以在前面要做个判断
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
                