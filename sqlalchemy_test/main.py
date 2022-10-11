from sqlalchemy import create_engine

from config import MYSQL_CONFIG

engine = create_engine(f"mysql+pymysql://{MYSQL_CONFIG['user']}:{MYSQL_CONFIG['password']}@{MYSQL_CONFIG['host']}:{MYSQL_CONFIG['port']}/{MYSQL_CONFIG.get('database', 'python_orm_test')}?charset={MYSQL_CONFIG.get('charset', 'utf8')}")

cur = engine.execute("select * from USER ")
result = cur.fetchall()
cur.close()
