from sqlalchemy import create_engine, Table, MetaData, select
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('db_host')
user = os.getenv('db_user')
password = os.getenv('db_password')
dbname = os.getenv('db_name')

def sqlengine():
    engine = create_engine(f'mysql+pymysql://%s:%s@{host}:3306/test' % (user,password))
    return engine


def fetchone(id):
    try:
        engine = sqlengine()
        conn = engine.connect()
        metadata = MetaData()
        sitemaps = Table('sitemaps', metadata, autoload_with=engine)

        query = select(sitemaps.c.url).where(sitemaps.c.id == id)
        result = conn.execute(query).fetchone()
        conn.close()
    except Exception as e:
        print(f'error: {e}')
        result = None
    return result

def fetchall():
    try:
        engine = sqlengine()
        conn = engine.connect()
        metadata = MetaData()
        sitemaps = Table('sitemaps', metadata, autoload_with=engine)

        query = select(sitemaps.c.url,sitemaps.c.id).where(sitemaps.c.is_scraped == 0).limit(10)
        result = conn.execute(query).fetchall()
        conn.close()
    except Exception as e:
        print(f'error: {e}')
        result = None
    return result

def updateDone(id):
    try:
        engine = sqlengine()
        conn = engine.connect()
        metadata = MetaData()
        sitemaps = Table('sitemaps', metadata, autoload_with=engine)

        upd = sitemaps.update().where(sitemaps.c.id == id).values(is_scraped=1)
        conn.execute(upd)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f'error: {e}')

def insert(data,id):
    try:
        engine = sqlengine()
        conn = engine.connect()
        metadata = MetaData()
        business_profiles = Table('bbb_companies', metadata, autoload_with=engine)

        ins = business_profiles.insert().values(data)
        conn.execute(ins)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f'error: {e}')
    finally:
        updateDone(id)