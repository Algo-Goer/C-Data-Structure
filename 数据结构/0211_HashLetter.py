# 下面是散列表的Python版本的完整实现（没有用Python内置字典）
# 这个散列表将只允许用大写字母来作为键，而且每种方法的运行时间都是O(1)
# HashLetter.py
class HashLetter(object):
    def __init__(self):
        '''
        post: initializes simplified hash table
        '''
        self.table = 26 * [None,]
    def __getitem__(self, key):
        '''
        post: returns value for specified key
        '''
        assert 'A' <= key <= 'Z'
        pos = ord(key) - ord('A')
        if self.table[pos] == None:
            raise KeyError(key)
        else:
            return self.table[pos]
    def __setitem__(self, key, value):
        '''
        post: value for specified key is inserted into hash table
        '''
        assert 'A' <= key <= 'Z'
        pos = ord(key) - ord('A')
        self.table[pos] = value
    def __delitem__(self, key):
        '''
        specified key is removed from hash table
        '''
        assert 'A' <= key <= 'Z'
        pos = ord(key) - ord('A')
        self.table[pos] = None
d = HashLetter()