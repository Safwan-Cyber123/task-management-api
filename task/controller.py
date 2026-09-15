from SRC.task.dtos import TaskScheme
from sqlalchemy.orm import Session
from SRC.task.models import TaskModel
from SRC.user.models import UserModel
from fastapi import HTTPException
def create_task(body:TaskScheme,db:Session,user:UserModel):
    data=body.model_dump()
    new_task=TaskModel(title=data["title"],Description=data["Description"],is_complete=data["is_complete"],user_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
def gettask(db:Session,user:UserModel):
    tasks=db.query(TaskModel).filter(TaskModel.user_id==user.id).all()
    return tasks
def getid(id:int,db:Session,user:UserModel):
    task=db.query(TaskModel).get(id)
    if not task:
        raise HTTPException(status_code=404,detail="Task Not Found")
    if task.user_id!=user.id:
        raise HTTPException(status_code=404,detail="You are not allowed")
         
    
    
    return task
def update_task(body:TaskScheme,taskid:int,db:Session,user:UserModel):
     task=db.query(TaskModel).get(taskid)
     if not task:
            raise HTTPException(status_code=404,detail="Task Not Found")
          
     if task.user_id!=user.id:
            raise HTTPException(status_code=404,detail="You Are Not Allowed")
          
     body=body.model_dump()
     for key,value in body.items():
          setattr(task,key,value)

     db.add(task)
     db.commit()
     db.refresh(task)
     return task

def delete_task(id:int,db:Session,user:UserModel):
      task=db.query(TaskModel).get(id)
      if not task:
            raise HTTPException(status_code=404,detail="Task Not Found") 
      if task.user_id!=user.id:    
            raise HTTPException(status_code=404,detail="You Are Not Found") 
      db.delete(task)
      db.commit()
      return None
