# coding=gbk
import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB


DATABASE_URL = 'mysql://%s:%s@%s:%s/%s' % (DB.get('user'),
                                           DB.get('pass'),
                                           DB.get('host'),
                                           DB.get('port', '3306'),
                                           DB.get('db'))

ENGINE_DATABASE_URL = 'mysql+pymysql://%s:%s@%s:%s/%s' % (DB.get('user'),
                                                          DB.get('pass'),
                                                          DB.get('host'),
                                                          DB.get('port', '3306'),
                                                          DB.get('db'))

database = databases.Database(DATABASE_URL)

# 初始化数据库连接:
engine = create_engine(ENGINE_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = sessionmaker(bind=engine)


async def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()