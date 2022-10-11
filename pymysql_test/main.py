import pymysql

from config import MYSQL_CONFIG

# 连接数据库
db = pymysql.connect(**MYSQL_CONFIG)
# 可以直接指定某个数据库
# db = pymysql.connect(database='test', **MYSQL_CONFIG)
# connect参数
"""
host=None	数据库连接地址
user=None	数据库用户名
password=‘’	数据库用户密码
database=None	要连接的数据库名称
port=3306	端口号，默认为3306
charset=‘’	要连接的数据库的字符编码（可以在终端登陆mysql后使用 \s 查看，如下图）
connect_timeout=10	连接数据库的超时时间，默认为10
port=3306	端口号，默认为3306
"""
# db对象方法
"""
close()	关闭数据库的连接
commit()	提交事务
rollback()	回滚事务
cursor()	获取游标对象，操作数据库，如执行DML操作，调用存储过程等
"""

# 创建游标对象
cursor = db.cursor()
# cursor对象方法
"""
close()	关闭当前游标
execute(operation,[,parameters])	执行数据库操作，sql语句或者数据库命令
executemany(operation, seq_of_params)	用于批量操作
fetchone()	获取查询结果集合中的下一条记录
fetchmany(size)	获取指定数量的记录
fetchall()	获取查询结果集合所有记录
nextset()	跳至下一个可用的数据集
arraysize	指定使用fetchmany()获取的行数，默认为1
setinputsizes(size)	设置调用execute*()方法时分配的内存区域大小
setoutputsizes(size)	设置列缓冲区大小，对大数据列尤其有用
"""

# sql语句
sql = 'show databases'
# 执行sql语句
cursor.execute(sql)
# 批量执行sql语句
cursor.executemany(sql)
# 获取一条数据
one = cursor.fetchone()
# 获取指定条数的数据，不写默认为1
many = cursor.fetchmany(3)
# 获取全部数据
all = cursor.fetchall()

# 关闭游标
cursor.close()
# 关闭数据库的连接
db.close()
