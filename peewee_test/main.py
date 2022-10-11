import peewee

from config import MYSQL_CONFIG

# =========================================== 数据库链接 ==================================================

# 声明数据库
db = peewee.MySQLDatabase(**MYSQL_CONFIG)
# 连接数据库
db.connect()


# ========================================== 实体类声明 =======================================================
class Person(peewee.Model):
    # 常用字段映射
    # IntegerField - int
    # BigIntegerField - bigint
    # SmallIntegerField - smallint
    # CharField - varchar
    # FixedCharField - char
    # DateTimeField - datetime
    # TimestampField - timestamp
    # BooleanField - bool

    name = peewee.CharField(verbose_name='姓名', max_length=10, null=False, index=True)
    # 属性值
    # null = False – 可否为空
    # index = False – index索引
    # unique = False – unique索引
    # column_name = None – string representing the underlying column to use if different, useful for legacy databases
    # default = None – 默认值，如果callable, 会调用生成！
    # primary_key = False – 主键
    # constraints = None - a list of one or more constraints, e.g. [Check('price > 0')]
    # sequence = None – sequence to populate field (if backend supports it)
    # collation = None – collation to use for ordering the field / index
    # unindexed = False – indicate field on virtual table should be unindexed (SQLite-only)
    # choices = None – an optional iterable containing 2-tuples of value, display
    # help_text = None – string representing any helpful text for this field
    # verbose_name = None – string representing the “user-friendly” name of this field

    passwd = peewee.CharField(verbose_name='密码', max_length=20, null=False, default='123456')
    email = peewee.CharField(verbose_name='邮件', max_length=50, null=True, unique=True)
    gender = peewee.IntegerField(verbose_name='姓别', null=False, default=1)
    birthday = peewee.DateField(verbose_name='生日', null=True, default=None)
    is_admin = peewee.BooleanField(verbose_name='是否是管理员', default=True)

    class Meta:
        database = db  # 这里是数据库链接，为了方便建立多个表，可以把这个部分提炼出来形成一个新的类
        table_name = 'persons'  # 这里可以自定义表名


# 为了方便建立多个表，可以把这个部分提炼出来形成一个新的类
"""
class BaseModel(peewee.Model):
    class Meta:
        database = db


class Person(BaseModel):
    name = peewee.CharField()
"""

# ================================================ 创建表 =======================================================

# 创建多表, 如果数据表已经存在，执行create_table的时候，将会抛出异常。
# db.create_tables([Person])
# 创建单表
# Person.create_table()


# ================================================ 增 ===========================================================
# 单条插入
# p = Person(name='master')
# p.save()

# Person.insert(name='test').execute()

# 批量插入
# Person.insert_many([('111'), ('222')]).execute()

# ================================================ 删 ===============================================================
# Person.delete().where(Person.name=='1').execute()

# ============================================== 改 ==========================================================
# Person.update({Person.passwd: 123}).where(Person.name == 'master').execute()


# ================================================= 查 ===================================================
# 查询单条所有字段
# res = Person.get(Person.name == 'master')
# print(res.name)

# 查询单条指定字段
# res = Person.select(Person.name).where(Person.name == 'master').get()
# print(res.name)

# 查询多条数据
# res = Person.select(Person.name).where(Person.is_admin == True)
# for item in res:
#     print(item.name)

# ============================================ 原生SQL =====================================
res = Person.raw('select * from persons').execute()
print(res)


# ================================================ 数据库关闭 ============================================================
# 判断数据库是否关闭
# print(db.is_closed())

# 关闭数据库
db.close()
