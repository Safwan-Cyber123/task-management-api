from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from SRC.util.db import Base
class TaskModel(Base):
    __tablename__="user_tasks"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    Description=Column(String)
    is_complete=Column(Boolean,default=False)
    user_id=Column(Integer,ForeignKey("user_table.id",ondelete="CASCADE"))