from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from SRC.util.settings import settings

Base=declarative_base()
engine=create_engine(url=settings.DB_Connection)
Session=sessionmaker(bind=engine)

def getdb():
    session=Session()
    try:
        yield session
    finally:
        session.close()