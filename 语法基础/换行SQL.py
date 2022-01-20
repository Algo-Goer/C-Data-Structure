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