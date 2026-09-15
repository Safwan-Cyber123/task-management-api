from fastapi import APIRouter,Depends,status
from SRC.task.dtos import TaskScheme,TaskResponseScheme
from SRC.task import controller
from SRC.util.db import getdb
from typing import List
from SRC.util.helpers import is_auth
from SRC.user.models import UserModel

task_routers=APIRouter(prefix="/tasks")
@task_routers.post("/createtask",response_model=TaskResponseScheme,status_code=status.HTTP_201_CREATED)
def create_task(body:TaskScheme,db=Depends(getdb),user:UserModel=Depends(is_auth)):
    return controller.create_task(body,db,user)

@task_routers.get("/gettasks",response_model=List[TaskResponseScheme],status_code=status.HTTP_200_OK)
def get_tasks(db=Depends(getdb),user:UserModel=Depends(is_auth)):
    return controller.gettask(db,user)

@task_routers.get("/gettasks/{id}",response_model=TaskResponseScheme,status_code=status.HTTP_200_OK)
def get_onetask(id:int,db=Depends(getdb),user:UserModel=Depends(is_auth)):
    return controller.getid(id,db,user)

@task_routers.put("/updatetask/{id}",response_model=TaskResponseScheme,status_code=status.HTTP_201_CREATED)
def update_task(body:TaskScheme,id:int,db=Depends(getdb),user:UserModel=Depends(is_auth)):
    return controller.update_task(body,id,db,user)

@task_routers.delete("/deletetask/{id}",response_model=None,status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int,db=Depends(getdb),user:UserModel=Depends(is_auth)):
    return controller.delete_task(id,db,user)
    