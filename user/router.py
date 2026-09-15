from fastapi import APIRouter,Depends,status,Request
from SRC.user.dtos import UserScheme
from sqlalchemy.orm import Session
from SRC.user.models import UserModel
from SRC.user.dtos import UserScheme,UserResponseScheme,UserLoginScheme
from SRC.util.db import getdb
from SRC.user import controller
from fastapi import BackgroundTasks

user_routers=APIRouter(prefix="/users")
@user_routers.post("/register",response_model=UserResponseScheme,status_code=status.HTTP_201_CREATED)
async def register(body:UserScheme,bg_task:BackgroundTasks,db:Session=Depends(getdb)):
    return await controller.register(body,db,bg_task)
@user_routers.post("/login",status_code=status.HTTP_200_OK)
def login(body:UserLoginScheme ,db:Session=Depends(getdb)):
    return controller.login(body,db)

