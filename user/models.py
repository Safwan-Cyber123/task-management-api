from sqlalchemy import Column,Integer,String
from SRC.util.db import Base
class UserModel(Base):
    __tablename__="user_table"
    id=Column(Integer,primary_key=True)
    username=Column(String,nullable=False)
    email=Column(String,nullable=False)
    hashed_password=Column(String,nullable=False)