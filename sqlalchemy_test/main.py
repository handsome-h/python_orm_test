from sqlalchemy import create_engine

from config import MYSQL_CONFIG

engine = create_engine(
    f"mysql+pymysql://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}@{MYSQL_CONFIG['host']}:{MYSQL_CONFIG['port']}/{MYSQL_CONFIG.get('database', 'python_orm_test')}?charset={MYSQL_CONFIG.get('charset', 'utf8')}",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
conn = engine.raw_connection()
cursor = conn.cursor()
cursor.execute("select * from persons")
result = cursor.fetchall()
print(result)
cursor.close()
conn.close()
